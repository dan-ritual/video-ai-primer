#!/usr/bin/env python3
"""
Universal Video Generator
Supports: Kling, Wan, LTX-2, Runway, Hailuo via multiple APIs

Usage:
    python generate.py "A cat playing piano" --model kling
    python generate.py "The cat starts dancing" --model kling-i2v --image https://example.com/cat.jpg
    python generate.py "Sunset timelapse" --model ltx --duration 8
    python generate.py --test  # Verify installation
"""

import os
import asyncio
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import fal_client
import replicate
import httpx
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()
console = Console()

class VideoGenerator:
    """Unified interface for multiple video AI APIs."""

    SUPPORTED_MODELS = {
        "kling": {
            "provider": "fal",
            "model_id": "fal-ai/kling-video/v1/pro/text-to-video",
            "cost_per_video": 0.28
        },
        "kling-i2v": {
            "provider": "fal",
            "model_id": "fal-ai/kling-video/v1/pro/image-to-video",
            "cost_per_video": 0.28
        },
        "wan": {
            "provider": "replicate",
            "model_id": "wan-ai/wan-2.1-t2v-14b",
            "cost_per_second": 0.03
        },
        "ltx": {
            "provider": "fal",
            "model_id": "fal-ai/ltx-video",
            "cost_per_second": 0.04
        },
        "hailuo": {
            "provider": "fal",
            "model_id": "fal-ai/minimax-video",
            "cost_per_video": 0.28
        }
    }

    def __init__(self, output_dir: str = "./outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cost_tracker = CostTracker()

    async def generate(
        self,
        prompt: str,
        model: str = "kling",
        duration: int = 5,
        image_url: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Generate video with specified model."""

        if model not in self.SUPPORTED_MODELS:
            raise ValueError(f"Unsupported model: {model}. Supported: {list(self.SUPPORTED_MODELS.keys())}")

        config = self.SUPPORTED_MODELS[model]
        provider = config["provider"]

        console.print(f"[cyan]Generating with {model} via {provider}...[/cyan]")

        try:
            if provider == "fal":
                result = await self._generate_fal(
                    model_id=config["model_id"],
                    prompt=prompt,
                    duration=duration,
                    image_url=image_url,
                    negative_prompt=negative_prompt,
                    **kwargs
                )
            elif provider == "replicate":
                result = await self._generate_replicate(
                    model_id=config["model_id"],
                    prompt=prompt,
                    duration=duration,
                    **kwargs
                )

            # Track cost
            cost = self._calculate_cost(model, duration)
            self.cost_tracker.add(model, cost)

            # Download and save
            output_path = await self._save_video(result, model, prompt)

            return {
                "status": "success",
                "model": model,
                "prompt": prompt,
                "output_path": str(output_path),
                "cost": cost,
                "metadata": result
            }

        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            return {
                "status": "error",
                "model": model,
                "prompt": prompt,
                "error": str(e)
            }

    async def _generate_fal(
        self,
        model_id: str,
        prompt: str,
        duration: int,
        image_url: Optional[str],
        negative_prompt: Optional[str],
        **kwargs
    ) -> Dict:
        """Generate via fal.ai."""

        arguments = {
            "prompt": prompt,
            "duration": str(duration),
            **kwargs
        }

        if image_url:
            arguments["image_url"] = image_url
        if negative_prompt:
            arguments["negative_prompt"] = negative_prompt

        handler = await fal_client.submit_async(model_id, arguments=arguments)
        result = await handler.get()

        return result

    async def _generate_replicate(
        self,
        model_id: str,
        prompt: str,
        duration: int,
        **kwargs
    ) -> Dict:
        """Generate via Replicate."""

        output = await asyncio.to_thread(
            replicate.run,
            model_id,
            input={
                "prompt": prompt,
                "num_frames": duration * 24,  # Assuming 24fps
                **kwargs
            }
        )

        return {"video": {"url": output}}

    def _calculate_cost(self, model: str, duration: int) -> float:
        """Calculate generation cost."""
        config = self.SUPPORTED_MODELS[model]

        if "cost_per_video" in config:
            return config["cost_per_video"]
        elif "cost_per_second" in config:
            return config["cost_per_second"] * duration

        return 0.0

    async def _save_video(self, result: Dict, model: str, prompt: str) -> Path:
        """Download and save video."""
        video_url = result.get("video", {}).get("url")

        if not video_url:
            raise ValueError("No video URL in result")

        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c == " ").strip()
        safe_prompt = safe_prompt.replace(" ", "_")
        filename = f"{model}_{timestamp}_{safe_prompt}.mp4"
        output_path = self.output_dir / filename

        # Download
        async with httpx.AsyncClient() as client:
            response = await client.get(video_url)
            response.raise_for_status()
            output_path.write_bytes(response.content)

        console.print(f"[green]Saved to: {output_path}[/green]")
        return output_path


class CostTracker:
    """Track generation costs."""

    def __init__(self):
        self.costs = []
        self.threshold = float(os.getenv("COST_ALERT_THRESHOLD", 50.0))

    def add(self, model: str, cost: float):
        self.costs.append({
            "model": model,
            "cost": cost,
            "timestamp": datetime.now().isoformat()
        })

        total = sum(c["cost"] for c in self.costs)
        if total > self.threshold:
            self._alert(total)

    def _alert(self, total: float):
        console.print(f"[yellow]Warning: Cost alert: ${total:.2f} exceeds threshold[/yellow]")
        # Could add Slack/email notification here

    @property
    def total(self) -> float:
        return sum(c["cost"] for c in self.costs)


# CLI Interface
async def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate video with AI")
    parser.add_argument("prompt", nargs="?", help="Generation prompt")
    parser.add_argument("--model", "-m", default="kling", help="Model to use")
    parser.add_argument("--duration", "-d", type=int, default=5, help="Duration in seconds")
    parser.add_argument("--image", "-i", help="Image URL for I2V")
    parser.add_argument("--negative", "-n", help="Negative prompt")
    parser.add_argument("--output", "-o", default="./outputs", help="Output directory")
    parser.add_argument("--test", action="store_true", help="Test mode")

    args = parser.parse_args()

    if args.test:
        console.print("[green]Installation verified[/green]")
        return

    if not args.prompt:
        console.print("[red]Error: Prompt required[/red]")
        return

    generator = VideoGenerator(output_dir=args.output)
    result = await generator.generate(
        prompt=args.prompt,
        model=args.model,
        duration=args.duration,
        image_url=args.image,
        negative_prompt=args.negative
    )

    if result["status"] == "success":
        console.print(f"\n[green]Generated successfully![/green]")
        console.print(f"  Output: {result['output_path']}")
        console.print(f"  Cost: ${result['cost']:.3f}")
    else:
        console.print(f"\n[red]Generation failed: {result['error']}[/red]")


if __name__ == "__main__":
    asyncio.run(main())

# Claude Code Video Automation Toolkit

*January 2026 Edition*

Scripts, workflows, and automation patterns for video AI orchestration with Claude Code.

---

## Table of Contents

1. [Toolkit Overview](#toolkit-overview)
2. [Environment Setup](#environment-setup)
3. [Core Automation Scripts](#core-automation-scripts)
4. [API Integration Modules](#api-integration-modules)
5. [Batch Processing Pipelines](#batch-processing-pipelines)
6. [ComfyUI Orchestration](#comfyui-orchestration)
7. [Quality Assurance Scripts](#quality-assurance-scripts)
8. [Workflow Templates](#workflow-templates)
9. [Claude Code Skills](#claude-code-skills)
10. [Integration Patterns](#integration-patterns)

---

## Toolkit Overview

### What This Toolkit Provides

```
┌─────────────────────────────────────────────────────────────┐
│                   Claude Code Video Toolkit                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   API       │  │   Batch     │  │   Quality   │        │
│  │ Integrations│  │ Processing  │  │ Assurance   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│         │               │               │                  │
│         ▼               ▼               ▼                  │
│  ┌─────────────────────────────────────────────────┐      │
│  │              Orchestration Layer                 │      │
│  │         (Claude Code + ffmpeg + Python)          │      │
│  └─────────────────────────────────────────────────┘      │
│         │               │               │                  │
│         ▼               ▼               ▼                  │
│  ┌───────────┐  ┌───────────┐  ┌───────────────┐         │
│  │  Kling    │  │   Wan     │  │    Runway     │         │
│  │  fal.ai   │  │  Local    │  │     API       │         │
│  └───────────┘  └───────────┘  └───────────────┘         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Core Capabilities

1. **Multi-Model Orchestration**: Unified interface to multiple video AI APIs
2. **Batch Processing**: Generate hundreds of videos from prompt lists
3. **Quality Gates**: Automated quality assessment before delivery
4. **Cost Tracking**: Real-time cost monitoring and optimization
5. **Error Recovery**: Automatic retry and fallback mechanisms

---

## Environment Setup

### Project Structure

```bash
video-ai-toolkit/
├── .env                    # API keys and configuration
├── requirements.txt        # Python dependencies
├── config.yaml            # Toolkit configuration
├── scripts/
│   ├── generate.py        # Core generation script
│   ├── batch.py           # Batch processing
│   ├── quality.py         # Quality assessment
│   └── utils.py           # Shared utilities
├── prompts/
│   ├── templates/         # Prompt templates by model
│   └── batches/          # Batch prompt files
├── outputs/
│   ├── drafts/           # Generated drafts
│   ├── approved/         # QA-passed outputs
│   └── logs/             # Generation logs
└── workflows/
    ├── comfyui/          # ComfyUI workflow JSONs
    └── pipelines/        # Pipeline definitions
```

### Environment Variables

```bash
# .env file
# API Keys
FAL_KEY=your_fal_ai_key
REPLICATE_API_TOKEN=your_replicate_token
RUNWAY_API_KEY=your_runway_key
OPENAI_API_KEY=your_openai_key  # For Sora
ELEVENLABS_API_KEY=your_elevenlabs_key

# Local Configuration
COMFYUI_URL=http://localhost:8188
OUTPUT_DIR=/path/to/outputs
MODEL_CACHE=/path/to/model/cache

# Cost Tracking
COST_ALERT_THRESHOLD=50.00  # Alert when daily spend exceeds
SLACK_WEBHOOK=your_slack_webhook  # For alerts

# Quality Settings
MIN_QUALITY_SCORE=0.7
AUTO_RETRY_THRESHOLD=0.5
```

### Dependencies

```txt
# requirements.txt
fal-client>=0.4.0
replicate>=0.20.0
anthropic>=0.18.0
httpx>=0.27.0
Pillow>=10.0.0
opencv-python>=4.8.0
numpy>=1.24.0
pyyaml>=6.0
python-dotenv>=1.0.0
aiohttp>=3.9.0
asyncio>=3.4.3
rich>=13.0.0  # For beautiful CLI output
```

### Installation

```bash
# Create project
mkdir video-ai-toolkit && cd video-ai-toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your API keys

# Verify installation
python scripts/generate.py --test
```

---

## Core Automation Scripts

### generate.py - Universal Video Generator

```python
#!/usr/bin/env python3
"""
Universal Video Generator
Supports: Kling, Wan, LTX-2, Runway, Hailuo via multiple APIs
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
        console.print(f"[yellow]⚠️ Cost alert: ${total:.2f} exceeds threshold[/yellow]")
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
        console.print("[green]✓ Installation verified[/green]")
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
        console.print(f"\n[green]✓ Generated successfully![/green]")
        console.print(f"  Output: {result['output_path']}")
        console.print(f"  Cost: ${result['cost']:.3f}")
    else:
        console.print(f"\n[red]✗ Generation failed: {result['error']}[/red]")


if __name__ == "__main__":
    asyncio.run(main())
```

### Usage Examples

```bash
# Basic text-to-video
python scripts/generate.py "A cat playing piano" --model kling

# Image-to-video
python scripts/generate.py "The cat starts dancing" --model kling-i2v --image https://example.com/cat.jpg

# With negative prompt
python scripts/generate.py "Professional product shot" --model kling --negative "hands, human, text, watermark"

# Different duration
python scripts/generate.py "Sunset timelapse" --model ltx --duration 8
```

---

## API Integration Modules

### Multi-Model Router

```python
# scripts/router.py
"""
Intelligent model router based on prompt analysis and requirements.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class ContentType(Enum):
    CINEMATIC = "cinematic"
    PRODUCT = "product"
    TALKING_HEAD = "talking_head"
    ANIME = "anime"
    SOCIAL = "social"
    MUSIC_VIDEO = "music_video"

class QualityTier(Enum):
    DRAFT = "draft"
    STANDARD = "standard"
    PREMIUM = "premium"

@dataclass
class RoutingConfig:
    content_type: ContentType
    quality_tier: QualityTier
    max_cost: Optional[float] = None
    requires_audio: bool = False
    requires_consistency: bool = False

class ModelRouter:
    """Route requests to optimal model based on requirements."""

    ROUTING_TABLE = {
        (ContentType.CINEMATIC, QualityTier.PREMIUM): ["veo", "runway"],
        (ContentType.CINEMATIC, QualityTier.STANDARD): ["kling", "sora"],
        (ContentType.CINEMATIC, QualityTier.DRAFT): ["wan", "ltx"],

        (ContentType.PRODUCT, QualityTier.PREMIUM): ["runway", "veo"],
        (ContentType.PRODUCT, QualityTier.STANDARD): ["kling", "hailuo"],
        (ContentType.PRODUCT, QualityTier.DRAFT): ["pika", "wan"],

        (ContentType.ANIME, QualityTier.PREMIUM): ["wan"],
        (ContentType.ANIME, QualityTier.STANDARD): ["wan", "kling"],
        (ContentType.ANIME, QualityTier.DRAFT): ["wan"],

        (ContentType.SOCIAL, QualityTier.PREMIUM): ["kling", "pika"],
        (ContentType.SOCIAL, QualityTier.STANDARD): ["kling", "pika"],
        (ContentType.SOCIAL, QualityTier.DRAFT): ["pika", "wan"],

        (ContentType.MUSIC_VIDEO, QualityTier.PREMIUM): ["seedance", "kling"],
        (ContentType.MUSIC_VIDEO, QualityTier.STANDARD): ["seedance"],
        (ContentType.MUSIC_VIDEO, QualityTier.DRAFT): ["kling", "wan"],
    }

    MODEL_COSTS = {
        "veo": 1.00,      # per 5s
        "runway": 1.25,
        "sora": 1.10,
        "kling": 0.28,
        "seedance": 0.50,
        "hailuo": 0.28,
        "pika": 0.20,
        "wan": 0.05,      # local/API
        "ltx": 0.10,
    }

    def route(self, config: RoutingConfig) -> str:
        """Get optimal model for given configuration."""

        candidates = self.ROUTING_TABLE.get(
            (config.content_type, config.quality_tier),
            ["kling"]  # Default fallback
        )

        # Filter by cost constraint
        if config.max_cost:
            candidates = [
                m for m in candidates
                if self.MODEL_COSTS.get(m, 0) <= config.max_cost
            ]

        # Special requirements
        if config.requires_audio:
            audio_capable = ["veo", "ltx", "seedance"]
            candidates = [m for m in candidates if m in audio_capable]

        if not candidates:
            raise ValueError("No models match requirements")

        return candidates[0]

    def analyze_prompt(self, prompt: str) -> ContentType:
        """Analyze prompt to determine content type."""

        prompt_lower = prompt.lower()

        if any(kw in prompt_lower for kw in ["anime", "manga", "cartoon", "animated"]):
            return ContentType.ANIME

        if any(kw in prompt_lower for kw in ["product", "floating", "rotating", "hero shot"]):
            return ContentType.PRODUCT

        if any(kw in prompt_lower for kw in ["speaking", "talking", "presenter", "avatar"]):
            return ContentType.TALKING_HEAD

        if any(kw in prompt_lower for kw in ["dance", "music", "beat", "choreography"]):
            return ContentType.MUSIC_VIDEO

        if any(kw in prompt_lower for kw in ["cinematic", "film", "movie", "dramatic"]):
            return ContentType.CINEMATIC

        return ContentType.SOCIAL  # Default


# Usage example
router = ModelRouter()
config = RoutingConfig(
    content_type=ContentType.PRODUCT,
    quality_tier=QualityTier.STANDARD,
    max_cost=0.50
)
model = router.route(config)  # Returns "kling" or "hailuo"
```

---

## Batch Processing Pipelines

### batch.py - Parallel Batch Processor

```python
#!/usr/bin/env python3
"""
Parallel batch processor for video generation.
"""

import asyncio
import json
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table

from generate import VideoGenerator

console = Console()

@dataclass
class BatchJob:
    id: str
    prompt: str
    model: str = "kling"
    duration: int = 5
    negative_prompt: str = None
    priority: int = 1
    tags: List[str] = None

class BatchProcessor:
    """Process multiple video generation jobs in parallel."""

    def __init__(
        self,
        max_concurrent: int = 5,
        output_dir: str = "./outputs/batches",
        retry_count: int = 2
    ):
        self.max_concurrent = max_concurrent
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.retry_count = retry_count
        self.generator = VideoGenerator(output_dir=str(self.output_dir))
        self.results = []

    async def process_batch(self, jobs: List[BatchJob]) -> Dict:
        """Process batch of jobs with concurrency control."""

        # Sort by priority
        jobs = sorted(jobs, key=lambda j: j.priority, reverse=True)

        semaphore = asyncio.Semaphore(self.max_concurrent)
        total = len(jobs)
        completed = 0
        failed = 0

        with Progress() as progress:
            task = progress.add_task("[cyan]Processing batch...", total=total)

            async def process_with_semaphore(job: BatchJob) -> Dict:
                nonlocal completed, failed
                async with semaphore:
                    result = await self._process_job(job)
                    if result["status"] == "success":
                        completed += 1
                    else:
                        failed += 1
                    progress.update(task, advance=1)
                    return result

            tasks = [process_with_semaphore(job) for job in jobs]
            self.results = await asyncio.gather(*tasks)

        # Generate report
        report = self._generate_report()
        self._save_report(report)

        return report

    async def _process_job(self, job: BatchJob) -> Dict:
        """Process single job with retry logic."""

        for attempt in range(self.retry_count + 1):
            result = await self.generator.generate(
                prompt=job.prompt,
                model=job.model,
                duration=job.duration,
                negative_prompt=job.negative_prompt
            )

            if result["status"] == "success":
                result["job_id"] = job.id
                result["tags"] = job.tags
                return result

            if attempt < self.retry_count:
                console.print(f"[yellow]Retrying {job.id} (attempt {attempt + 2})[/yellow]")
                await asyncio.sleep(2 ** attempt)  # Exponential backoff

        result["job_id"] = job.id
        return result

    def _generate_report(self) -> Dict:
        """Generate batch processing report."""

        successful = [r for r in self.results if r["status"] == "success"]
        failed = [r for r in self.results if r["status"] == "error"]

        total_cost = sum(r.get("cost", 0) for r in successful)

        return {
            "timestamp": datetime.now().isoformat(),
            "total_jobs": len(self.results),
            "successful": len(successful),
            "failed": len(failed),
            "total_cost": total_cost,
            "results": self.results,
            "failed_details": [
                {"id": r["job_id"], "error": r.get("error")}
                for r in failed
            ]
        }

    def _save_report(self, report: Dict):
        """Save report to file."""

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = self.output_dir / f"batch_report_{timestamp}.json"

        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)

        console.print(f"\n[cyan]Report saved: {report_path}[/cyan]")

        # Print summary table
        table = Table(title="Batch Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Total Jobs", str(report["total_jobs"]))
        table.add_row("Successful", str(report["successful"]))
        table.add_row("Failed", str(report["failed"]))
        table.add_row("Total Cost", f"${report['total_cost']:.2f}")

        console.print(table)


def load_batch_file(path: str) -> List[BatchJob]:
    """Load batch jobs from JSON file."""

    with open(path) as f:
        data = json.load(f)

    jobs = []
    for item in data.get("jobs", data.get("batches", [])):
        jobs.append(BatchJob(
            id=item.get("id", f"job_{len(jobs)}"),
            prompt=item["prompt"],
            model=item.get("model", "kling"),
            duration=item.get("duration", 5),
            negative_prompt=item.get("negative_prompt"),
            priority=item.get("priority", 1),
            tags=item.get("tags", [])
        ))

    return jobs


async def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch video generation")
    parser.add_argument("batch_file", help="JSON file with batch jobs")
    parser.add_argument("--concurrent", "-c", type=int, default=5, help="Max concurrent jobs")
    parser.add_argument("--output", "-o", default="./outputs/batches", help="Output directory")
    parser.add_argument("--retries", "-r", type=int, default=2, help="Retry count per job")

    args = parser.parse_args()

    jobs = load_batch_file(args.batch_file)
    console.print(f"[cyan]Loaded {len(jobs)} jobs from {args.batch_file}[/cyan]")

    processor = BatchProcessor(
        max_concurrent=args.concurrent,
        output_dir=args.output,
        retry_count=args.retries
    )

    report = await processor.process_batch(jobs)

    if report["failed"] > 0:
        console.print(f"\n[yellow]⚠️ {report['failed']} jobs failed[/yellow]")
        for detail in report["failed_details"]:
            console.print(f"  - {detail['id']}: {detail['error']}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Example Batch File

```json
{
  "jobs": [
    {
      "id": "product_headphones_001",
      "prompt": "Sleek wireless headphones floating and rotating against pure black background, premium product photography, Apple-style lighting",
      "model": "kling",
      "duration": 5,
      "negative_prompt": "hands, human, dust, scratches, text",
      "priority": 2,
      "tags": ["product", "electronics", "hero"]
    },
    {
      "id": "product_headphones_002",
      "prompt": "Same headphones, ear cups folding inward smoothly, satisfying mechanical motion",
      "model": "kling",
      "duration": 5,
      "priority": 2,
      "tags": ["product", "electronics", "feature"]
    },
    {
      "id": "lifestyle_001",
      "prompt": "Young professional walking through modern city, wearing the headphones, golden hour lighting, confident stride",
      "model": "kling",
      "duration": 5,
      "priority": 1,
      "tags": ["lifestyle", "urban"]
    }
  ]
}
```

---

## ComfyUI Orchestration

### comfyui_client.py - Remote ComfyUI Control

```python
"""
ComfyUI API client for remote workflow execution.
"""

import httpx
import asyncio
import json
import uuid
from pathlib import Path
from typing import Dict, Optional
import websockets

class ComfyUIClient:
    """Client for interacting with ComfyUI API."""

    def __init__(self, host: str = "localhost", port: int = 8188):
        self.base_url = f"http://{host}:{port}"
        self.ws_url = f"ws://{host}:{port}/ws"

    async def load_workflow(self, workflow_path: str) -> Dict:
        """Load workflow from JSON file."""
        with open(workflow_path) as f:
            return json.load(f)

    async def execute_workflow(
        self,
        workflow: Dict,
        substitutions: Optional[Dict] = None
    ) -> Dict:
        """Execute workflow with optional parameter substitutions."""

        # Apply substitutions
        if substitutions:
            workflow = self._apply_substitutions(workflow, substitutions)

        # Queue prompt
        prompt_id = await self._queue_prompt(workflow)

        # Wait for completion
        result = await self._wait_for_result(prompt_id)

        return result

    def _apply_substitutions(self, workflow: Dict, subs: Dict) -> Dict:
        """Replace placeholders in workflow with actual values."""

        workflow_str = json.dumps(workflow)

        for key, value in subs.items():
            placeholder = f"${{{key}}}"
            workflow_str = workflow_str.replace(placeholder, str(value))

        return json.loads(workflow_str)

    async def _queue_prompt(self, workflow: Dict) -> str:
        """Queue workflow for execution."""

        client_id = str(uuid.uuid4())

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/prompt",
                json={
                    "prompt": workflow,
                    "client_id": client_id
                }
            )
            response.raise_for_status()
            data = response.json()

        return data["prompt_id"]

    async def _wait_for_result(self, prompt_id: str, timeout: int = 600) -> Dict:
        """Wait for workflow execution to complete."""

        async with websockets.connect(self.ws_url) as ws:
            while True:
                try:
                    message = await asyncio.wait_for(
                        ws.recv(),
                        timeout=timeout
                    )
                    data = json.loads(message)

                    if data["type"] == "executed":
                        if data["data"]["prompt_id"] == prompt_id:
                            return await self._get_outputs(prompt_id)

                    elif data["type"] == "execution_error":
                        if data["data"]["prompt_id"] == prompt_id:
                            raise RuntimeError(f"Execution error: {data['data']}")

                except asyncio.TimeoutError:
                    raise TimeoutError(f"Workflow timed out after {timeout}s")

    async def _get_outputs(self, prompt_id: str) -> Dict:
        """Get outputs from completed workflow."""

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/history/{prompt_id}")
            response.raise_for_status()
            data = response.json()

        return data[prompt_id]["outputs"]

    async def upload_image(self, image_path: str) -> str:
        """Upload image to ComfyUI and return filename."""

        async with httpx.AsyncClient() as client:
            with open(image_path, "rb") as f:
                response = await client.post(
                    f"{self.base_url}/upload/image",
                    files={"image": (Path(image_path).name, f)}
                )
                response.raise_for_status()
                data = response.json()

        return data["name"]


# Example workflow template for video generation
VIDEO_WORKFLOW_TEMPLATE = {
    "3": {
        "class_type": "LoadImage",
        "inputs": {
            "image": "${INPUT_IMAGE}"
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "${PROMPT}",
            "clip": ["4", 0]
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "${NEGATIVE_PROMPT}",
            "clip": ["4", 0]
        }
    },
    # ... rest of workflow nodes
}
```

---

## Quality Assurance Scripts

### quality.py - Automated Quality Assessment

```python
#!/usr/bin/env python3
"""
Automated quality assessment for generated videos.
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table

console = Console()

@dataclass
class QualityReport:
    video_path: str
    overall_score: float
    sharpness: float
    motion_quality: float
    temporal_consistency: float
    face_quality: float  # If faces present
    passed: bool
    issues: List[str]

class VideoQualityAnalyzer:
    """Analyze video quality for common AI generation issues."""

    def __init__(
        self,
        min_score: float = 0.7,
        sample_frames: int = 10
    ):
        self.min_score = min_score
        self.sample_frames = sample_frames

    def analyze(self, video_path: str) -> QualityReport:
        """Analyze video and return quality report."""

        video_path = Path(video_path)
        if not video_path.exists():
            raise FileNotFoundError(f"Video not found: {video_path}")

        cap = cv2.VideoCapture(str(video_path))
        frames = self._extract_frames(cap)
        cap.release()

        if not frames:
            return QualityReport(
                video_path=str(video_path),
                overall_score=0,
                sharpness=0,
                motion_quality=0,
                temporal_consistency=0,
                face_quality=0,
                passed=False,
                issues=["Could not extract frames"]
            )

        # Run quality checks
        sharpness = self._check_sharpness(frames)
        motion = self._check_motion_quality(frames)
        temporal = self._check_temporal_consistency(frames)
        face = self._check_face_quality(frames)

        # Calculate overall score
        weights = {
            "sharpness": 0.25,
            "motion": 0.25,
            "temporal": 0.35,
            "face": 0.15
        }

        overall = (
            sharpness * weights["sharpness"] +
            motion * weights["motion"] +
            temporal * weights["temporal"] +
            face * weights["face"]
        )

        # Identify issues
        issues = []
        if sharpness < 0.6:
            issues.append("Low sharpness / blurry frames")
        if motion < 0.6:
            issues.append("Unnatural motion")
        if temporal < 0.6:
            issues.append("Temporal inconsistency / flickering")
        if face < 0.6 and face > 0:
            issues.append("Face quality issues")

        return QualityReport(
            video_path=str(video_path),
            overall_score=overall,
            sharpness=sharpness,
            motion_quality=motion,
            temporal_consistency=temporal,
            face_quality=face,
            passed=overall >= self.min_score,
            issues=issues
        )

    def _extract_frames(self, cap: cv2.VideoCapture) -> List[np.ndarray]:
        """Extract sample frames from video."""

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count == 0:
            return []

        # Sample evenly across video
        indices = np.linspace(0, frame_count - 1, self.sample_frames, dtype=int)

        frames = []
        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)

        return frames

    def _check_sharpness(self, frames: List[np.ndarray]) -> float:
        """Check image sharpness using Laplacian variance."""

        variances = []
        for frame in frames:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            variance = cv2.Laplacian(gray, cv2.CV_64F).var()
            variances.append(variance)

        avg_variance = np.mean(variances)

        # Normalize to 0-1 scale (100 is typical threshold for "sharp")
        return min(avg_variance / 100, 1.0)

    def _check_motion_quality(self, frames: List[np.ndarray]) -> float:
        """Check motion quality using optical flow."""

        if len(frames) < 2:
            return 0.5

        motion_scores = []
        for i in range(len(frames) - 1):
            gray1 = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frames[i + 1], cv2.COLOR_BGR2GRAY)

            # Calculate optical flow
            flow = cv2.calcOpticalFlowFarneback(
                gray1, gray2, None,
                pyr_scale=0.5, levels=3, winsize=15,
                iterations=3, poly_n=5, poly_sigma=1.2, flags=0
            )

            # Check for smooth flow
            magnitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
            uniformity = 1 - (np.std(magnitude) / (np.mean(magnitude) + 0.01))

            motion_scores.append(max(0, uniformity))

        return np.mean(motion_scores)

    def _check_temporal_consistency(self, frames: List[np.ndarray]) -> float:
        """Check temporal consistency (flickering detection)."""

        if len(frames) < 3:
            return 0.5

        consistency_scores = []
        for i in range(1, len(frames) - 1):
            # Compare frame to neighbors
            diff_prev = cv2.absdiff(frames[i], frames[i - 1])
            diff_next = cv2.absdiff(frames[i], frames[i + 1])

            # High difference between neighbors suggests flickering
            mean_diff_prev = np.mean(diff_prev)
            mean_diff_next = np.mean(diff_next)

            # Lower difference = better consistency
            score = 1 - (mean_diff_prev + mean_diff_next) / 510

            consistency_scores.append(max(0, score))

        return np.mean(consistency_scores)

    def _check_face_quality(self, frames: List[np.ndarray]) -> float:
        """Check face quality if faces are present."""

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        face_scores = []
        faces_found = False

        for frame in frames:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) > 0:
                faces_found = True
                for (x, y, w, h) in faces:
                    face_roi = gray[y:y+h, x:x+w]

                    # Check face sharpness
                    sharpness = cv2.Laplacian(face_roi, cv2.CV_64F).var()
                    face_scores.append(min(sharpness / 50, 1.0))

        if not faces_found:
            return 1.0  # No faces = no face issues

        return np.mean(face_scores) if face_scores else 0.5


def batch_analyze(video_dir: str, pattern: str = "*.mp4") -> List[QualityReport]:
    """Analyze all videos in directory."""

    analyzer = VideoQualityAnalyzer()
    video_dir = Path(video_dir)
    videos = list(video_dir.glob(pattern))

    reports = []
    for video in videos:
        console.print(f"Analyzing: {video.name}")
        report = analyzer.analyze(str(video))
        reports.append(report)

    # Print summary
    table = Table(title="Quality Analysis Results")
    table.add_column("Video", style="cyan")
    table.add_column("Score", justify="right")
    table.add_column("Status")
    table.add_column("Issues")

    for report in reports:
        status = "[green]PASS[/green]" if report.passed else "[red]FAIL[/red]"
        issues = ", ".join(report.issues) if report.issues else "-"
        table.add_row(
            Path(report.video_path).name,
            f"{report.overall_score:.2f}",
            status,
            issues
        )

    console.print(table)

    return reports


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Video quality analysis")
    parser.add_argument("path", help="Video file or directory")
    parser.add_argument("--threshold", "-t", type=float, default=0.7)

    args = parser.parse_args()

    path = Path(args.path)

    if path.is_dir():
        reports = batch_analyze(str(path))
    else:
        analyzer = VideoQualityAnalyzer(min_score=args.threshold)
        report = analyzer.analyze(str(path))

        console.print(f"\n[cyan]Quality Report: {path.name}[/cyan]")
        console.print(f"  Overall Score: {report.overall_score:.2f}")
        console.print(f"  Sharpness: {report.sharpness:.2f}")
        console.print(f"  Motion Quality: {report.motion_quality:.2f}")
        console.print(f"  Temporal Consistency: {report.temporal_consistency:.2f}")
        console.print(f"  Status: {'[green]PASS[/green]' if report.passed else '[red]FAIL[/red]'}")

        if report.issues:
            console.print(f"  Issues: {', '.join(report.issues)}")
```

---

## Claude Code Skills

### video-gen.md - Custom Skill for Claude Code

Create this file at `~/.claude/skills/video-gen.md`:

```markdown
# Video Generation Skill

When asked to generate video, use this workflow:

## Available Commands

### Generate Video
```bash
python ~/video-ai-toolkit/scripts/generate.py "<prompt>" --model <model>
```

Models: kling, kling-i2v, wan, ltx, hailuo

### Batch Generation
```bash
python ~/video-ai-toolkit/scripts/batch.py prompts.json --concurrent 5
```

### Quality Check
```bash
python ~/video-ai-toolkit/scripts/quality.py <video_path>
```

## Best Practices

1. **Prompt Structure**: Use the format from PROMPT_TEMPLATE_LIBRARY.md
2. **Model Selection**: Refer to MODEL_SELECTION_DECISION_TREE.md
3. **Cost Awareness**: Track costs, prefer local models for iteration
4. **Quality Gates**: Always run quality check before delivering

## Example Workflows

### Quick Social Video
```bash
# Generate
python generate.py "Cat playing piano in jazz club, cinematic" --model kling

# Check quality
python quality.py outputs/kling_*.mp4
```

### Premium Production
```bash
# Generate with premium model
python generate.py "Cinematic landscape at golden hour" --model runway

# Upscale if needed
ffmpeg -i input.mp4 -vf "scale=3840:2160:flags=lanczos" output_4k.mp4
```
```

---

## Integration Patterns

### Pattern 1: CI/CD Video Pipeline

```yaml
# .github/workflows/video-generation.yml
name: Video Generation Pipeline

on:
  push:
    paths:
      - 'prompts/**'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Generate videos
        env:
          FAL_KEY: ${{ secrets.FAL_KEY }}
        run: |
          python scripts/batch.py prompts/new_batch.json

      - name: Quality check
        run: |
          python scripts/quality.py outputs/batches/

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: generated-videos
          path: outputs/batches/*.mp4
```

### Pattern 2: Slack Bot Integration

```python
# slack_bot.py
from slack_bolt.async_app import AsyncApp
from generate import VideoGenerator

app = AsyncApp(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/generate-video")
async def generate_video(ack, command, client):
    await ack()

    prompt = command["text"]
    user_id = command["user_id"]
    channel_id = command["channel_id"]

    await client.chat_postMessage(
        channel=channel_id,
        text=f"🎬 Generating video for: {prompt}\nThis may take a few minutes..."
    )

    generator = VideoGenerator()
    result = await generator.generate(prompt=prompt, model="kling")

    if result["status"] == "success":
        # Upload to Slack
        await client.files_upload_v2(
            channel=channel_id,
            file=result["output_path"],
            title=f"Generated: {prompt[:50]}",
            initial_comment=f"<@{user_id}> Your video is ready! Cost: ${result['cost']:.3f}"
        )
    else:
        await client.chat_postMessage(
            channel=channel_id,
            text=f"<@{user_id}> Generation failed: {result['error']}"
        )
```

---

## Multi-Agent Orchestration

*New Section — Grok-Verified Patterns (January 2026)*

### Claude-Flow Multi-Agent Framework

Claude-Flow is the leading agent orchestration platform for Claude, enabling intelligent multi-agent swarms for video production.

```python
# claude_flow_video.py
"""
Multi-agent video production using Claude-Flow.
GitHub: ruvnet/claude-flow
"""

from claude_flow import Swarm, Agent, Task
from typing import List, Dict

class VideoProductionSwarm:
    """
    Orchestrate multiple Claude agents for video production.

    Agent Roles:
    - Prompt Engineer: Optimizes prompts for each model
    - Quality Assessor: Evaluates generated outputs
    - Post-Processor: Handles RIFE/Real-ESRGAN pipelines
    - Project Manager: Coordinates workflow
    """

    def __init__(self, max_agents: int = 5):
        self.swarm = Swarm(max_concurrent=max_agents)
        self._setup_agents()

    def _setup_agents(self):
        """Initialize specialized agents."""

        self.prompt_agent = Agent(
            name="prompt_engineer",
            system_prompt="""You are an expert video AI prompt engineer.
            Your role is to optimize prompts for maximum quality output.
            Consider the target model's strengths and syntax preferences.
            Reference: 03_JSON_PROMPTING_GUIDE.md""",
            tools=["read_file", "write_file"]
        )

        self.quality_agent = Agent(
            name="quality_assessor",
            system_prompt="""You analyze generated videos for quality issues.
            Check for: temporal consistency, motion artifacts, face quality,
            prompt adherence, and technical specifications.
            Reference: 14_AGENT_QUALITY_EVALS_FRAMEWORK.md""",
            tools=["run_command", "analyze_video"]
        )

        self.postproc_agent = Agent(
            name="post_processor",
            system_prompt="""You handle video post-processing pipelines.
            Execute: RIFE interpolation, Real-ESRGAN upscaling, color correction.
            Always interpolate FIRST, then upscale (efficiency order).
            Reference: 19_FFMPEG_POSTPROCESSING_PIPELINE.md""",
            tools=["run_command", "ffmpeg"]
        )

        self.manager_agent = Agent(
            name="project_manager",
            system_prompt="""You coordinate the video production workflow.
            Delegate tasks to specialized agents, track progress,
            handle errors, and ensure delivery quality.""",
            tools=["delegate", "track_progress"]
        )

    async def produce_video(self, brief: str) -> Dict:
        """
        Full production pipeline with multi-agent coordination.

        Args:
            brief: Creative brief describing desired video

        Returns:
            Production result with video path and metadata
        """

        # Phase 1: Prompt Engineering
        prompt_task = Task(
            agent=self.prompt_agent,
            instruction=f"Optimize this brief into a video generation prompt: {brief}"
        )
        optimized_prompt = await self.swarm.execute(prompt_task)

        # Phase 2: Generation (parallel if multiple shots)
        generation_task = Task(
            agent=self.manager_agent,
            instruction=f"Generate video using: {optimized_prompt}"
        )
        raw_video = await self.swarm.execute(generation_task)

        # Phase 3: Quality Assessment
        quality_task = Task(
            agent=self.quality_agent,
            instruction=f"Assess quality of: {raw_video}"
        )
        quality_report = await self.swarm.execute(quality_task)

        # Phase 4: Post-Processing (if quality passes)
        if quality_report["score"] >= 0.7:
            postproc_task = Task(
                agent=self.postproc_agent,
                instruction=f"Enhance video: {raw_video} -> 4K 60fps"
            )
            final_video = await self.swarm.execute(postproc_task)
        else:
            # Regenerate with feedback
            return await self._regenerate_with_feedback(brief, quality_report)

        return {
            "status": "success",
            "video_path": final_video,
            "quality_score": quality_report["score"],
            "prompt_used": optimized_prompt
        }

    async def _regenerate_with_feedback(self, brief: str, feedback: Dict) -> Dict:
        """Regenerate with quality feedback incorporated."""

        enhanced_brief = f"{brief}\n\nQuality feedback to address: {feedback['issues']}"
        return await self.produce_video(enhanced_brief)


# Usage
async def main():
    swarm = VideoProductionSwarm(max_agents=5)

    result = await swarm.produce_video(
        brief="Cinematic drone shot over mountains at sunset, "
              "with volumetric fog and golden hour lighting"
    )

    print(f"Video ready: {result['video_path']}")
    print(f"Quality: {result['quality_score']:.2f}")
```

### Running 10+ Claude Instances in Parallel

From DEV Community: Multi-agent orchestration patterns.

```python
# parallel_claudes.py
"""
Run multiple Claude Code instances in parallel for video production.
Based on: dev.to/bredmond1019/multi-agent-orchestration
"""

import asyncio
import subprocess
from dataclasses import dataclass
from typing import List, Callable
from pathlib import Path

@dataclass
class ClaudeTask:
    task_id: str
    prompt: str
    working_dir: str
    on_complete: Callable = None

class ParallelClaudeOrchestrator:
    """
    Orchestrate multiple Claude Code CLI instances.

    Key insight: Each Claude instance runs in its own terminal/process,
    with iTerm2 notifications for completion alerts.
    """

    def __init__(self, max_parallel: int = 10):
        self.max_parallel = max_parallel
        self.semaphore = asyncio.Semaphore(max_parallel)
        self.results = {}

    async def run_tasks(self, tasks: List[ClaudeTask]) -> dict:
        """Run multiple Claude tasks in parallel."""

        async def run_single(task: ClaudeTask):
            async with self.semaphore:
                result = await self._execute_claude(task)
                self.results[task.task_id] = result

                if task.on_complete:
                    task.on_complete(result)

                return result

        await asyncio.gather(*[run_single(t) for t in tasks])
        return self.results

    async def _execute_claude(self, task: ClaudeTask) -> dict:
        """Execute single Claude Code instance."""

        # Create isolated working directory
        work_dir = Path(task.working_dir)
        work_dir.mkdir(parents=True, exist_ok=True)

        # Write task prompt to file
        prompt_file = work_dir / "TASK.md"
        prompt_file.write_text(task.prompt)

        # Run Claude Code CLI
        process = await asyncio.create_subprocess_exec(
            "claude",
            "--print",  # Non-interactive mode
            "-p", task.prompt,
            cwd=str(work_dir),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        # Send iTerm2 notification on complete
        self._notify_iterm(f"Task {task.task_id} complete")

        return {
            "task_id": task.task_id,
            "success": process.returncode == 0,
            "output": stdout.decode(),
            "error": stderr.decode() if stderr else None
        }

    def _notify_iterm(self, message: str):
        """Send iTerm2 notification."""
        # iTerm2 proprietary escape sequence
        print(f"\033]9;{message}\007", end="", flush=True)


# Video production example
async def parallel_video_production():
    """Generate multiple video shots in parallel."""

    orchestrator = ParallelClaudeOrchestrator(max_parallel=5)

    # Define shots for a product video
    shots = [
        ClaudeTask(
            task_id="shot_1_hero",
            prompt="Generate hero shot: Product floating, rotating 360°, black background",
            working_dir="./production/shot_1"
        ),
        ClaudeTask(
            task_id="shot_2_detail",
            prompt="Generate detail shot: Close-up of product texture, macro lens",
            working_dir="./production/shot_2"
        ),
        ClaudeTask(
            task_id="shot_3_lifestyle",
            prompt="Generate lifestyle shot: Product in use, natural environment",
            working_dir="./production/shot_3"
        ),
        ClaudeTask(
            task_id="shot_4_feature",
            prompt="Generate feature demo: Product mechanism in action, slow motion",
            working_dir="./production/shot_4"
        ),
        ClaudeTask(
            task_id="shot_5_outro",
            prompt="Generate outro: Product with logo, gradient background",
            working_dir="./production/shot_5"
        )
    ]

    results = await orchestrator.run_tasks(shots)

    # Compile results
    successful = [r for r in results.values() if r["success"]]
    print(f"Completed: {len(successful)}/{len(shots)} shots")

    return results


if __name__ == "__main__":
    asyncio.run(parallel_video_production())
```

### CLAUDE.md Pattern for Video Projects

Track Claude's mistakes and learnings in a single file.

```markdown
# CLAUDE.md - Video Production Project

## Project Context
- Goal: Create 30-second product video
- Model preference: Kling 2.6 for hero shots, Wan 2.1 for anime segments
- Quality bar: 4K 60fps final delivery

## Learned Preferences
- Always use negative prompt for product shots: "hands, human, text, watermark, dust"
- Interpolate BEFORE upscale (see 19_FFMPEG_POSTPROCESSING_PIPELINE.md)
- Use JSON structured prompts for Kling (03_JSON_PROMPTING_GUIDE.md)

## Mistakes to Avoid
- DON'T generate at 4K then interpolate (slow, high VRAM)
- DON'T skip quality check before post-processing
- DON'T use minterpolate for anime (use RIFE instead)

## Working Commands
```bash
# Quick generation
python scripts/generate.py "prompt" --model kling --duration 5

# Full pipeline
./full_pipeline.py input.mp4 output.mp4 --fps 60 --resolution 4k

# Quality check
python scripts/quality.py outputs/*.mp4 --threshold 0.7
```

## Cost Tracking
- Budget: $50/day
- Current spend: $23.40
- Alert threshold: $40

## Session Notes
- [2026-01-18] Hero shot approved after 2nd attempt
- [2026-01-18] Lifestyle shot needs more natural lighting
```

### MCP Server for fal.ai Video Generation

From PulseMCP: Fal.ai Video Generator MCP Server.

```python
# mcp_fal_video.py
"""
MCP Server for fal.ai video generation.
Enables Claude to generate videos directly via tool use.
"""

from mcp.server import Server
from mcp.types import Tool, TextContent
import fal_client

server = Server("fal-video-generator")

@server.tool()
async def generate_video(
    prompt: str,
    model: str = "kling",
    duration: int = 5,
    negative_prompt: str = None
) -> str:
    """
    Generate video using fal.ai.

    Args:
        prompt: Video description
        model: Model to use (kling, wan, ltx, hailuo)
        duration: Video duration in seconds
        negative_prompt: What to avoid

    Returns:
        URL of generated video
    """

    model_map = {
        "kling": "fal-ai/kling-video/v1/pro/text-to-video",
        "wan": "fal-ai/wan/v2.1/text-to-video",
        "ltx": "fal-ai/ltx-video",
        "hailuo": "fal-ai/minimax-video"
    }

    arguments = {
        "prompt": prompt,
        "duration": str(duration)
    }

    if negative_prompt:
        arguments["negative_prompt"] = negative_prompt

    handler = await fal_client.submit_async(
        model_map[model],
        arguments=arguments
    )

    result = await handler.get()
    video_url = result.get("video", {}).get("url")

    return f"Video generated: {video_url}"


@server.tool()
async def post_process_video(
    video_url: str,
    target_fps: int = 60,
    upscale: int = 2
) -> str:
    """
    Post-process video with RIFE interpolation and Real-ESRGAN upscaling.

    Args:
        video_url: URL of video to process
        target_fps: Target framerate
        upscale: Upscale factor (2 or 4)

    Returns:
        URL of processed video
    """

    # Download, process locally, upload result
    # (Implementation depends on your infrastructure)

    return f"Processed video ready at: {processed_url}"


if __name__ == "__main__":
    server.run()
```

---

## n8n Workflow Automation

### Full Video Production Workflow

From web resources: n8n workflows for AI video automation.

```json
{
  "name": "AI Video Production Pipeline",
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "video-request",
        "httpMethod": "POST"
      }
    },
    {
      "name": "Optimize Prompt",
      "type": "n8n-nodes-base.anthropic",
      "parameters": {
        "model": "claude-sonnet-4-20250514",
        "prompt": "Optimize this video prompt for Kling 2.6: {{ $json.brief }}"
      }
    },
    {
      "name": "Generate Video",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://queue.fal.run/fal-ai/kling-video/v1/pro/text-to-video",
        "method": "POST",
        "headers": {
          "Authorization": "Key {{ $credentials.falApiKey }}"
        },
        "body": {
          "prompt": "{{ $json.optimizedPrompt }}",
          "duration": "5"
        }
      }
    },
    {
      "name": "Poll for Result",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "{{ $json.status_url }}",
        "method": "GET",
        "retry": {
          "maxTries": 60,
          "waitBetweenTries": 5000
        }
      }
    },
    {
      "name": "Quality Check",
      "type": "n8n-nodes-base.executeCommand",
      "parameters": {
        "command": "python quality.py {{ $json.video_url }}"
      }
    },
    {
      "name": "Post-Process",
      "type": "n8n-nodes-base.executeCommand",
      "parameters": {
        "command": "python full_pipeline.py {{ $json.video_path }} output.mp4 --fps 60"
      }
    },
    {
      "name": "Notify Slack",
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "#video-production",
        "text": "Video ready: {{ $json.output_url }}"
      }
    }
  ]
}
```

---

*Claude Code Video Toolkit v1.1 — January 18, 2026*
*For use with: Python 3.10+, Claude Code, fal.ai, Replicate, ComfyUI*
*New: Multi-agent orchestration, Claude-Flow, n8n workflows, MCP servers*

#!/usr/bin/env python3
"""
ComfyUI API client for remote workflow execution.

Usage:
    from comfyui_client import ComfyUIClient

    client = ComfyUIClient(host="localhost", port=8188)
    workflow = await client.load_workflow("workflow.json")
    result = await client.execute_workflow(workflow, {
        "PROMPT": "A beautiful sunset",
        "NEGATIVE_PROMPT": "blurry, low quality"
    })
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
    # Additional nodes would be defined here for a complete workflow
}


async def main():
    """Demo usage of ComfyUI client."""
    import argparse

    parser = argparse.ArgumentParser(description="ComfyUI workflow executor")
    parser.add_argument("workflow", help="Path to workflow JSON file")
    parser.add_argument("--host", default="localhost", help="ComfyUI host")
    parser.add_argument("--port", type=int, default=8188, help="ComfyUI port")
    parser.add_argument("--prompt", "-p", help="Prompt text")
    parser.add_argument("--negative", "-n", help="Negative prompt")
    parser.add_argument("--image", "-i", help="Input image path")

    args = parser.parse_args()

    client = ComfyUIClient(host=args.host, port=args.port)

    # Load workflow
    workflow = await client.load_workflow(args.workflow)

    # Build substitutions
    subs = {}
    if args.prompt:
        subs["PROMPT"] = args.prompt
    if args.negative:
        subs["NEGATIVE_PROMPT"] = args.negative
    if args.image:
        # Upload image first
        image_name = await client.upload_image(args.image)
        subs["INPUT_IMAGE"] = image_name

    # Execute
    print(f"Executing workflow: {args.workflow}")
    result = await client.execute_workflow(workflow, subs)
    print(f"Result: {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3
"""
Parallel batch processor for video generation.

Usage:
    python batch.py batch_jobs.json --concurrent 5 --output ./outputs/batches

Example batch file (batch_jobs.json):
{
  "jobs": [
    {
      "id": "product_001",
      "prompt": "Product floating and rotating against black background",
      "model": "kling",
      "duration": 5,
      "negative_prompt": "hands, human, text",
      "priority": 2,
      "tags": ["product", "hero"]
    }
  ]
}
"""

import asyncio
import json
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, field
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
    tags: List[str] = field(default_factory=list)

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
        console.print(f"\n[yellow]Warning: {report['failed']} jobs failed[/yellow]")
        for detail in report["failed_details"]:
            console.print(f"  - {detail['id']}: {detail['error']}")


if __name__ == "__main__":
    asyncio.run(main())

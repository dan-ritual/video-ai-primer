#!/usr/bin/env python3
"""
Automated quality assessment for generated videos.

Usage:
    python quality.py video.mp4 --threshold 0.7
    python quality.py ./outputs/ --threshold 0.7  # Batch analyze directory

Checks:
    - Sharpness (Laplacian variance)
    - Motion quality (optical flow uniformity)
    - Temporal consistency (flickering detection)
    - Face quality (if faces present)
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

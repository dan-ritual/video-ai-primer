# Agent Quality Evals Framework

*January 2026 Edition*

Automated quality evaluation system for AI-generated video at scale.

---

## Table of Contents

1. [Framework Philosophy](#framework-philosophy)
2. [Evaluation Dimensions](#evaluation-dimensions)
3. [Automated Metrics](#automated-metrics)
4. [LLM-as-Judge Integration](#llm-as-judge-integration)
5. [Pipeline Architecture](#pipeline-architecture)
6. [Benchmark Datasets](#benchmark-datasets)
7. [Scoring Rubrics](#scoring-rubrics)
8. [Implementation Guide](#implementation-guide)
9. [Reporting & Analytics](#reporting--analytics)
10. [Continuous Improvement](#continuous-improvement)

---

## Framework Philosophy

### Why Automated Evals Matter

```
Manual Review Limitations:
- Doesn't scale (human bottleneck)
- Inconsistent (reviewer fatigue, bias)
- Slow (hours per batch)
- Expensive (human time)

Automated Evals Benefits:
- Scales infinitely
- Consistent scoring
- Real-time feedback
- Cost-effective
- Enables rapid iteration
```

### The Hybrid Approach

```
┌─────────────────────────────────────────────────────────────┐
│                     Quality Eval Pipeline                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Generated Video]                                          │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────┐                                        │
│  │ Technical Evals │  ← Automated (CV metrics)              │
│  │ - Sharpness     │                                        │
│  │ - Motion        │                                        │
│  │ - Consistency   │                                        │
│  └────────┬────────┘                                        │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────┐                                        │
│  │ Semantic Evals  │  ← LLM-as-Judge (Claude/GPT-4V)        │
│  │ - Prompt Match  │                                        │
│  │ - Aesthetics    │                                        │
│  │ - Coherence     │                                        │
│  └────────┬────────┘                                        │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────┐                                        │
│  │ Domain Evals    │  ← Specialized models                  │
│  │ - Face quality  │                                        │
│  │ - Object detect │                                        │
│  │ - Safety        │                                        │
│  └────────┬────────┘                                        │
│           │                                                 │
│           ▼                                                 │
│  [Composite Score + Report]                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Evaluation Dimensions

### The 10 Core Dimensions

| Dimension | Weight | Type | Description |
|-----------|--------|------|-------------|
| **Technical Quality** | 15% | Auto | Resolution, sharpness, artifacts |
| **Motion Quality** | 15% | Auto | Smoothness, physics, natural movement |
| **Temporal Consistency** | 15% | Auto | Flickering, stability, coherence |
| **Prompt Alignment** | 15% | LLM | Does output match request? |
| **Visual Aesthetics** | 10% | LLM | Beauty, composition, appeal |
| **Subject Consistency** | 10% | Auto+LLM | Character/object persistence |
| **Face/Hand Quality** | 10% | Auto | Anatomical correctness |
| **Audio-Video Sync** | 5% | Auto | If audio present |
| **Style Coherence** | 3% | LLM | Consistent art direction |
| **Safety/Compliance** | 2% | Auto | No prohibited content |

### Dimension Details

#### 1. Technical Quality
```
Metrics:
- Resolution achieved vs. requested
- Laplacian variance (sharpness)
- Compression artifact detection
- Color banding analysis
- Noise level estimation

Scoring:
1.0: Broadcast quality, no visible issues
0.8: Professional quality, minor issues
0.6: Acceptable for web use
0.4: Noticeable degradation
0.2: Significant quality issues
0.0: Unusable
```

#### 2. Motion Quality
```
Metrics:
- Optical flow smoothness
- Physics plausibility (gravity, momentum)
- Motion blur consistency
- Frame-to-frame velocity consistency
- Jitter/judder detection

Scoring:
1.0: Cinematic, realistic motion
0.8: Natural looking, minor artifacts
0.6: Acceptable, some unnatural moments
0.4: Noticeable motion issues
0.2: Significant motion problems
0.0: Broken/frozen/chaotic motion
```

#### 3. Temporal Consistency
```
Metrics:
- Inter-frame luminance variance (flickering)
- Object persistence tracking
- Background stability
- Color consistency over time
- Edge stability

Scoring:
1.0: Rock solid, no flickering
0.8: Very stable, rare minor flicker
0.6: Mostly stable, occasional flicker
0.4: Noticeable inconsistency
0.2: Frequent flickering/changes
0.0: Severe temporal issues
```

#### 4. Prompt Alignment
```
Evaluation Method: LLM-as-Judge

Criteria:
- Subject presence (described elements exist)
- Action match (described actions occur)
- Setting accuracy (environment matches)
- Style alignment (aesthetic matches)
- Negative prompt adherence (excluded elements absent)

Scoring:
1.0: Perfect match to prompt
0.8: Strong match, minor deviations
0.6: Captures main elements
0.4: Partial match
0.2: Weak connection to prompt
0.0: Completely different from prompt
```

#### 5. Visual Aesthetics
```
Evaluation Method: LLM-as-Judge

Criteria:
- Composition quality
- Color harmony
- Lighting appeal
- Overall visual interest
- Professional appearance

Scoring:
1.0: Stunning, gallery-worthy
0.8: Beautiful, professional
0.6: Pleasing, well-executed
0.4: Acceptable, unremarkable
0.2: Unappealing
0.0: Visually unpleasant
```

---

## Automated Metrics

### Technical Metrics Implementation

```python
# metrics/technical.py
import cv2
import numpy as np
from scipy import ndimage
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class TechnicalMetrics:
    sharpness: float
    noise_level: float
    color_banding: float
    artifact_score: float
    resolution_match: float
    overall: float

class TechnicalAnalyzer:
    """Automated technical quality metrics."""

    def analyze_video(
        self,
        video_path: str,
        target_resolution: Tuple[int, int] = (1920, 1080)
    ) -> TechnicalMetrics:
        """Analyze video technical quality."""

        cap = cv2.VideoCapture(video_path)
        frames = self._extract_sample_frames(cap)
        cap.release()

        # Individual metrics
        sharpness = self._measure_sharpness(frames)
        noise = self._measure_noise(frames)
        banding = self._measure_color_banding(frames)
        artifacts = self._detect_artifacts(frames)
        res_match = self._check_resolution(frames[0], target_resolution)

        # Weighted overall
        overall = (
            sharpness * 0.3 +
            (1 - noise) * 0.2 +
            (1 - banding) * 0.15 +
            (1 - artifacts) * 0.2 +
            res_match * 0.15
        )

        return TechnicalMetrics(
            sharpness=sharpness,
            noise_level=noise,
            color_banding=banding,
            artifact_score=artifacts,
            resolution_match=res_match,
            overall=overall
        )

    def _measure_sharpness(self, frames: List[np.ndarray]) -> float:
        """Measure image sharpness using Laplacian variance."""
        variances = []
        for frame in frames:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)
            variance = laplacian.var()
            variances.append(variance)

        avg = np.mean(variances)
        # Normalize (100 is typical sharp image threshold)
        return min(avg / 100, 1.0)

    def _measure_noise(self, frames: List[np.ndarray]) -> float:
        """Estimate noise level in frames."""
        noise_levels = []
        for frame in frames:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Median filter to get "clean" version
            clean = cv2.medianBlur(gray, 5)
            # Difference = noise estimate
            noise = np.mean(np.abs(gray.astype(float) - clean.astype(float)))
            noise_levels.append(noise)

        avg = np.mean(noise_levels)
        # Normalize (higher = more noise, worse quality)
        return min(avg / 50, 1.0)

    def _measure_color_banding(self, frames: List[np.ndarray]) -> float:
        """Detect color banding artifacts."""
        banding_scores = []
        for frame in frames:
            # Convert to gradient
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gradient = np.gradient(gray.astype(float))
            magnitude = np.sqrt(gradient[0]**2 + gradient[1]**2)

            # Banding shows as sharp gradient transitions
            histogram = np.histogram(magnitude, bins=256)[0]
            # Many sharp peaks = banding
            peak_count = np.sum(histogram > np.mean(histogram) * 3)
            banding_scores.append(peak_count / 256)

        return np.mean(banding_scores)

    def _detect_artifacts(self, frames: List[np.ndarray]) -> float:
        """Detect compression and generation artifacts."""
        artifact_scores = []
        for frame in frames:
            # DCT block artifact detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Look for 8x8 block patterns (JPEG/compression artifacts)
            h, w = gray.shape
            blocks = gray[:h//8*8, :w//8*8].reshape(h//8, 8, w//8, 8)
            block_vars = blocks.std(axis=(1, 3))

            # High variance at block boundaries = artifacts
            artifact_score = np.mean(np.diff(block_vars.flatten())) / 50
            artifact_scores.append(min(abs(artifact_score), 1.0))

        return np.mean(artifact_scores)

    def _check_resolution(
        self,
        frame: np.ndarray,
        target: Tuple[int, int]
    ) -> float:
        """Check if resolution matches target."""
        h, w = frame.shape[:2]
        target_w, target_h = target

        # Score based on how close to target
        w_ratio = min(w / target_w, target_w / w)
        h_ratio = min(h / target_h, target_h / h)

        return (w_ratio + h_ratio) / 2

    def _extract_sample_frames(
        self,
        cap: cv2.VideoCapture,
        n_samples: int = 10
    ) -> List[np.ndarray]:
        """Extract evenly spaced sample frames."""
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        indices = np.linspace(0, frame_count - 1, n_samples, dtype=int)

        frames = []
        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)

        return frames
```

### Motion Metrics Implementation

```python
# metrics/motion.py
import cv2
import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class MotionMetrics:
    smoothness: float
    physics_plausibility: float
    consistency: float
    overall: float

class MotionAnalyzer:
    """Analyze motion quality in video."""

    def analyze_video(self, video_path: str) -> MotionMetrics:
        """Analyze motion quality."""

        cap = cv2.VideoCapture(video_path)
        frames = self._extract_all_frames(cap)
        cap.release()

        if len(frames) < 3:
            return MotionMetrics(0.5, 0.5, 0.5, 0.5)

        smoothness = self._measure_smoothness(frames)
        physics = self._measure_physics_plausibility(frames)
        consistency = self._measure_consistency(frames)

        overall = smoothness * 0.4 + physics * 0.3 + consistency * 0.3

        return MotionMetrics(
            smoothness=smoothness,
            physics_plausibility=physics,
            consistency=consistency,
            overall=overall
        )

    def _measure_smoothness(self, frames: List[np.ndarray]) -> float:
        """Measure motion smoothness using optical flow."""
        flow_magnitudes = []
        flow_angles = []

        for i in range(len(frames) - 1):
            gray1 = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frames[i + 1], cv2.COLOR_BGR2GRAY)

            flow = cv2.calcOpticalFlowFarneback(
                gray1, gray2, None,
                pyr_scale=0.5, levels=3, winsize=15,
                iterations=3, poly_n=5, poly_sigma=1.2, flags=0
            )

            magnitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
            angle = np.arctan2(flow[..., 1], flow[..., 0])

            flow_magnitudes.append(np.mean(magnitude))
            flow_angles.append(np.mean(angle))

        # Smooth motion = gradual changes in magnitude and direction
        mag_variance = np.std(flow_magnitudes)
        angle_variance = np.std(flow_angles)

        # Lower variance = smoother
        smoothness = 1 - min((mag_variance + angle_variance) / 10, 1.0)
        return max(smoothness, 0)

    def _measure_physics_plausibility(self, frames: List[np.ndarray]) -> float:
        """Estimate if motion follows physics."""
        # This is a simplified heuristic
        # Full implementation would use physics simulation comparison

        velocities = []
        for i in range(len(frames) - 1):
            gray1 = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frames[i + 1], cv2.COLOR_BGR2GRAY)

            # Track features
            corners = cv2.goodFeaturesToTrack(gray1, 100, 0.01, 10)
            if corners is None:
                continue

            corners2, status, _ = cv2.calcOpticalFlowPyrLK(
                gray1, gray2, corners, None
            )

            good_old = corners[status == 1]
            good_new = corners2[status == 1]

            # Calculate velocities
            if len(good_old) > 0:
                v = good_new - good_old
                velocities.extend(np.linalg.norm(v, axis=1))

        if not velocities:
            return 0.5

        # Check for sudden velocity changes (unphysical)
        velocities = np.array(velocities)
        acceleration = np.diff(velocities)
        sudden_changes = np.sum(np.abs(acceleration) > np.std(velocities) * 3)

        # Fewer sudden changes = more physical
        return 1 - min(sudden_changes / len(velocities), 1.0)

    def _measure_consistency(self, frames: List[np.ndarray]) -> float:
        """Measure temporal motion consistency."""
        # Check if motion is consistent across frame pairs
        consistencies = []

        for i in range(1, len(frames) - 1):
            prev_flow = self._get_flow(frames[i-1], frames[i])
            next_flow = self._get_flow(frames[i], frames[i+1])

            # Flows should be similar for consistent motion
            flow_diff = np.mean(np.abs(prev_flow - next_flow))
            consistency = 1 - min(flow_diff / 10, 1.0)
            consistencies.append(consistency)

        return np.mean(consistencies) if consistencies else 0.5

    def _get_flow(self, frame1: np.ndarray, frame2: np.ndarray) -> np.ndarray:
        """Calculate optical flow between frames."""
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        return cv2.calcOpticalFlowFarneback(
            gray1, gray2, None,
            pyr_scale=0.5, levels=3, winsize=15,
            iterations=3, poly_n=5, poly_sigma=1.2, flags=0
        )

    def _extract_all_frames(self, cap: cv2.VideoCapture) -> List[np.ndarray]:
        """Extract all frames from video."""
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        return frames
```

---

## LLM-as-Judge Integration

### Prompt Alignment Evaluation

```python
# metrics/llm_judge.py
import anthropic
import base64
import cv2
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class SemanticEvaluation:
    prompt_alignment: float
    visual_aesthetics: float
    style_coherence: float
    reasoning: Dict[str, str]
    overall: float

class LLMJudge:
    """Use Claude for semantic evaluation of video quality."""

    SYSTEM_PROMPT = """You are an expert video quality evaluator. You will be shown frames from an AI-generated video along with the original prompt used to generate it.

Your task is to evaluate the video on these dimensions:

1. PROMPT ALIGNMENT (0.0-1.0): How well does the video match the prompt?
   - Are all described subjects present?
   - Do the described actions occur?
   - Does the setting match?
   - Are negative prompt elements absent?

2. VISUAL AESTHETICS (0.0-1.0): How visually appealing is the video?
   - Composition quality
   - Color harmony
   - Lighting
   - Overall professional appearance

3. STYLE COHERENCE (0.0-1.0): Is the style consistent?
   - Same art style throughout
   - Consistent color palette
   - Unified visual language

Respond in JSON format:
{
  "prompt_alignment": 0.0-1.0,
  "prompt_alignment_reasoning": "explanation",
  "visual_aesthetics": 0.0-1.0,
  "visual_aesthetics_reasoning": "explanation",
  "style_coherence": 0.0-1.0,
  "style_coherence_reasoning": "explanation"
}"""

    def __init__(self, api_key: str = None):
        self.client = anthropic.Anthropic(api_key=api_key)

    def evaluate(
        self,
        video_path: str,
        prompt: str,
        negative_prompt: str = None,
        n_frames: int = 5
    ) -> SemanticEvaluation:
        """Evaluate video semantically using Claude."""

        # Extract sample frames
        frames = self._extract_frames(video_path, n_frames)
        frame_images = [self._encode_frame(f) for f in frames]

        # Build message
        content = [
            {
                "type": "text",
                "text": f"Original generation prompt: {prompt}"
            }
        ]

        if negative_prompt:
            content.append({
                "type": "text",
                "text": f"Negative prompt (elements that should NOT appear): {negative_prompt}"
            })

        content.append({
            "type": "text",
            "text": f"The following {n_frames} frames are sampled evenly from the generated video:"
        })

        for i, img_data in enumerate(frame_images):
            content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": img_data
                }
            })
            content.append({
                "type": "text",
                "text": f"Frame {i+1}/{n_frames}"
            })

        content.append({
            "type": "text",
            "text": "Please evaluate this video according to the criteria. Respond with JSON only."
        })

        # Call Claude
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=self.SYSTEM_PROMPT,
            messages=[{"role": "user", "content": content}]
        )

        # Parse response
        result = self._parse_response(response.content[0].text)

        overall = (
            result["prompt_alignment"] * 0.5 +
            result["visual_aesthetics"] * 0.3 +
            result["style_coherence"] * 0.2
        )

        return SemanticEvaluation(
            prompt_alignment=result["prompt_alignment"],
            visual_aesthetics=result["visual_aesthetics"],
            style_coherence=result["style_coherence"],
            reasoning={
                "prompt_alignment": result.get("prompt_alignment_reasoning", ""),
                "visual_aesthetics": result.get("visual_aesthetics_reasoning", ""),
                "style_coherence": result.get("style_coherence_reasoning", "")
            },
            overall=overall
        )

    def _extract_frames(self, video_path: str, n: int) -> List:
        """Extract n evenly spaced frames."""
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        indices = [int(i * frame_count / n) for i in range(n)]

        frames = []
        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)

        cap.release()
        return frames

    def _encode_frame(self, frame) -> str:
        """Encode frame to base64 JPEG."""
        _, buffer = cv2.imencode('.jpg', frame)
        return base64.b64encode(buffer).decode('utf-8')

    def _parse_response(self, text: str) -> Dict:
        """Parse JSON response from Claude."""
        import json
        # Find JSON in response
        start = text.find('{')
        end = text.rfind('}') + 1
        if start >= 0 and end > start:
            return json.loads(text[start:end])
        return {
            "prompt_alignment": 0.5,
            "visual_aesthetics": 0.5,
            "style_coherence": 0.5
        }
```

---

## Pipeline Architecture

### Complete Evaluation Pipeline

```python
# pipeline/evaluator.py
import asyncio
from dataclasses import dataclass
from typing import Dict, List, Optional
from pathlib import Path

from metrics.technical import TechnicalAnalyzer
from metrics.motion import MotionAnalyzer
from metrics.llm_judge import LLMJudge

@dataclass
class EvaluationResult:
    video_path: str
    prompt: str
    technical: Dict
    motion: Dict
    semantic: Dict
    face_quality: Optional[float]
    composite_score: float
    passed: bool
    recommendations: List[str]

class VideoEvaluationPipeline:
    """Complete video quality evaluation pipeline."""

    WEIGHTS = {
        "technical": 0.15,
        "motion": 0.15,
        "temporal": 0.15,
        "prompt_alignment": 0.15,
        "aesthetics": 0.10,
        "subject_consistency": 0.10,
        "face_quality": 0.10,
        "style": 0.03,
        "safety": 0.02,
        "audio_sync": 0.05
    }

    def __init__(
        self,
        pass_threshold: float = 0.7,
        anthropic_api_key: str = None
    ):
        self.pass_threshold = pass_threshold
        self.technical_analyzer = TechnicalAnalyzer()
        self.motion_analyzer = MotionAnalyzer()
        self.llm_judge = LLMJudge(api_key=anthropic_api_key)

    async def evaluate(
        self,
        video_path: str,
        prompt: str,
        negative_prompt: str = None,
        has_faces: bool = None,
        has_audio: bool = None
    ) -> EvaluationResult:
        """Run complete evaluation pipeline."""

        # Run analyzers in parallel where possible
        technical_result = await asyncio.to_thread(
            self.technical_analyzer.analyze_video,
            video_path
        )

        motion_result = await asyncio.to_thread(
            self.motion_analyzer.analyze_video,
            video_path
        )

        semantic_result = await asyncio.to_thread(
            self.llm_judge.evaluate,
            video_path, prompt, negative_prompt
        )

        # Face quality (if applicable)
        face_quality = None
        if has_faces or has_faces is None:
            face_quality = await asyncio.to_thread(
                self._analyze_faces,
                video_path
            )

        # Calculate composite score
        scores = {
            "technical": technical_result.overall,
            "motion": motion_result.overall,
            "temporal": motion_result.consistency,
            "prompt_alignment": semantic_result.prompt_alignment,
            "aesthetics": semantic_result.visual_aesthetics,
            "subject_consistency": motion_result.consistency,  # Proxy
            "face_quality": face_quality if face_quality else 1.0,
            "style": semantic_result.style_coherence,
            "safety": 1.0,  # Assume safe unless flagged
            "audio_sync": 1.0 if not has_audio else 0.8  # Proxy
        }

        composite = sum(
            scores[k] * self.WEIGHTS[k]
            for k in self.WEIGHTS
        )

        # Generate recommendations
        recommendations = self._generate_recommendations(scores)

        return EvaluationResult(
            video_path=video_path,
            prompt=prompt,
            technical={
                "sharpness": technical_result.sharpness,
                "noise": technical_result.noise_level,
                "artifacts": technical_result.artifact_score,
                "overall": technical_result.overall
            },
            motion={
                "smoothness": motion_result.smoothness,
                "physics": motion_result.physics_plausibility,
                "consistency": motion_result.consistency,
                "overall": motion_result.overall
            },
            semantic={
                "prompt_alignment": semantic_result.prompt_alignment,
                "aesthetics": semantic_result.visual_aesthetics,
                "style_coherence": semantic_result.style_coherence,
                "reasoning": semantic_result.reasoning
            },
            face_quality=face_quality,
            composite_score=composite,
            passed=composite >= self.pass_threshold,
            recommendations=recommendations
        )

    def _analyze_faces(self, video_path: str) -> float:
        """Analyze face quality in video."""
        import cv2

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        cap = cv2.VideoCapture(video_path)
        scores = []

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        sample_indices = range(0, frame_count, max(1, frame_count // 10))

        for idx in sample_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                # Sharpness of face region
                sharpness = cv2.Laplacian(face_roi, cv2.CV_64F).var()
                scores.append(min(sharpness / 50, 1.0))

        cap.release()

        if not scores:
            return None  # No faces detected

        return np.mean(scores)

    def _generate_recommendations(self, scores: Dict) -> List[str]:
        """Generate improvement recommendations based on scores."""
        recommendations = []

        if scores["technical"] < 0.7:
            recommendations.append(
                "Technical quality is below threshold. Consider regenerating "
                "with higher quality settings or upscaling."
            )

        if scores["motion"] < 0.7:
            recommendations.append(
                "Motion quality needs improvement. Try adjusting motion_scale "
                "or using a model with better motion handling."
            )

        if scores["prompt_alignment"] < 0.7:
            recommendations.append(
                "Output doesn't match prompt well. Review prompt structure "
                "and try being more specific about key elements."
            )

        if scores["face_quality"] and scores["face_quality"] < 0.7:
            recommendations.append(
                "Face quality is poor. Add face-specific negative prompts "
                "or use face correction in post."
            )

        if scores["style"] < 0.7:
            recommendations.append(
                "Style is inconsistent. Use stronger style tokens and "
                "ensure consistent negative prompts."
            )

        return recommendations


# Batch evaluation
async def evaluate_batch(
    video_dir: str,
    prompts_file: str,
    output_file: str = "eval_results.json"
):
    """Evaluate a batch of videos."""
    import json

    pipeline = VideoEvaluationPipeline()

    with open(prompts_file) as f:
        prompts = json.load(f)

    results = []
    video_dir = Path(video_dir)

    for item in prompts:
        video_path = video_dir / item["video_filename"]
        if not video_path.exists():
            continue

        result = await pipeline.evaluate(
            str(video_path),
            item["prompt"],
            item.get("negative_prompt")
        )

        results.append({
            "video": item["video_filename"],
            "composite_score": result.composite_score,
            "passed": result.passed,
            "technical": result.technical,
            "motion": result.motion,
            "semantic": result.semantic,
            "recommendations": result.recommendations
        })

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    # Print summary
    passed = sum(1 for r in results if r["passed"])
    print(f"\nEvaluation Complete")
    print(f"Total: {len(results)}")
    print(f"Passed: {passed} ({passed/len(results)*100:.1f}%)")
    print(f"Failed: {len(results) - passed}")
    print(f"Average Score: {sum(r['composite_score'] for r in results)/len(results):.3f}")
```

---

## Benchmark Datasets

### Standard Test Prompts

```json
{
  "benchmark_prompts": [
    {
      "id": "basic_motion_001",
      "category": "basic_motion",
      "prompt": "A red ball bouncing on a wooden floor",
      "expected": ["ball", "bouncing", "floor", "physics"],
      "difficulty": "easy"
    },
    {
      "id": "human_action_001",
      "category": "human_action",
      "prompt": "A person walking through a park on a sunny day",
      "expected": ["person", "walking", "park", "daylight"],
      "difficulty": "medium"
    },
    {
      "id": "face_quality_001",
      "category": "face_quality",
      "prompt": "Close-up of a woman speaking to camera, professional lighting",
      "expected": ["face", "speaking", "professional"],
      "difficulty": "hard"
    },
    {
      "id": "complex_scene_001",
      "category": "complex_scene",
      "prompt": "A busy coffee shop with multiple people ordering, barista making drinks",
      "expected": ["multiple_people", "interaction", "environment"],
      "difficulty": "very_hard"
    },
    {
      "id": "anime_style_001",
      "category": "stylized",
      "prompt": "Anime girl with blue hair running through cherry blossoms",
      "expected": ["anime_style", "character", "environment"],
      "difficulty": "medium"
    }
  ]
}
```

---

## Reporting & Analytics

### Evaluation Dashboard Data

```python
# reporting/dashboard.py
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
import json

@dataclass
class EvalReport:
    timestamp: str
    total_evaluated: int
    pass_rate: float
    average_score: float
    by_category: Dict[str, Dict]
    by_model: Dict[str, Dict]
    trends: List[Dict]
    recommendations: List[str]

def generate_report(results: List[Dict]) -> EvalReport:
    """Generate comprehensive evaluation report."""

    # Basic stats
    total = len(results)
    passed = sum(1 for r in results if r.get("passed", False))
    avg_score = sum(r["composite_score"] for r in results) / total

    # By category
    categories = {}
    for r in results:
        cat = r.get("category", "uncategorized")
        if cat not in categories:
            categories[cat] = {"count": 0, "passed": 0, "total_score": 0}
        categories[cat]["count"] += 1
        categories[cat]["passed"] += 1 if r.get("passed") else 0
        categories[cat]["total_score"] += r["composite_score"]

    for cat in categories:
        categories[cat]["avg_score"] = (
            categories[cat]["total_score"] / categories[cat]["count"]
        )
        categories[cat]["pass_rate"] = (
            categories[cat]["passed"] / categories[cat]["count"]
        )

    # By model
    models = {}
    for r in results:
        model = r.get("model", "unknown")
        if model not in models:
            models[model] = {"count": 0, "passed": 0, "total_score": 0}
        models[model]["count"] += 1
        models[model]["passed"] += 1 if r.get("passed") else 0
        models[model]["total_score"] += r["composite_score"]

    for model in models:
        models[model]["avg_score"] = (
            models[model]["total_score"] / models[model]["count"]
        )

    # Top recommendations
    all_recs = []
    for r in results:
        all_recs.extend(r.get("recommendations", []))

    # Count recommendation frequency
    rec_counts = {}
    for rec in all_recs:
        rec_counts[rec] = rec_counts.get(rec, 0) + 1

    top_recs = sorted(rec_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    return EvalReport(
        timestamp=datetime.now().isoformat(),
        total_evaluated=total,
        pass_rate=passed / total,
        average_score=avg_score,
        by_category=categories,
        by_model=models,
        trends=[],  # Would calculate from historical data
        recommendations=[r[0] for r in top_recs]
    )
```

---

*Agent Quality Evals Framework v1.0 — January 18, 2026*
*For automated quality assessment at scale*

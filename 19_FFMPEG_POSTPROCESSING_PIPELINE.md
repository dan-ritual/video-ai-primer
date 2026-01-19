# FFmpeg Post-Processing Pipeline Guide

*January 2026 Edition*

Advanced CLI automation for AI video post-processing: RIFE interpolation, Real-ESRGAN upscaling, batch pipelines, and agentic editing.

---

## Table of Contents

1. [Pipeline Overview](#pipeline-overview)
2. [RIFE Frame Interpolation](#rife-frame-interpolation)
3. [Real-ESRGAN Upscaling](#real-esrgan-upscaling)
4. [Processing Order Optimization](#processing-order-optimization)
5. [Batch Automation Scripts](#batch-automation-scripts)
6. [Agentic Post-Production](#agentic-post-production)
7. [Full Pipeline Integration](#full-pipeline-integration)
8. [Advanced FFmpeg Techniques](#advanced-ffmpeg-techniques)
9. [X/Twitter Power User Workflows](#xtwitter-power-user-workflows)

---

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│              FFmpeg POST-PROCESSING PIPELINE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  AI VIDEO OUTPUT                                                        │
│       │                                                                 │
│       ▼                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    │
│  │   INTERPOLATE   │ -> │    UPSCALE      │ -> │   RE-ENCODE     │    │
│  │   (RIFE 4.6+)   │    │ (Real-ESRGAN)   │    │   (FFmpeg)      │    │
│  │   2x-4x FPS     │    │   2x-4x Res     │    │   H.264/HEVC    │    │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘    │
│                                                                         │
│  CRITICAL: Interpolate FIRST (smaller frames = faster)                 │
│            Upscale SECOND (fewer frames to process)                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why This Order Matters

| Order | Interpolate → Upscale | Upscale → Interpolate |
|-------|----------------------|----------------------|
| Speed | **Faster** (interpolate small frames) | Slower (interpolate large frames) |
| Memory | **Lower** VRAM usage | Higher VRAM usage |
| Quality | Equivalent | Equivalent |
| Cost | **Lower** GPU time | Higher GPU time |

---

## RIFE Frame Interpolation

### Overview

RIFE (Real-time Intermediate Flow Estimation) is the gold standard for AI frame interpolation, especially for AI-generated videos where low frame rates (8-24 fps) need boosting for fluidity.

### Model Selection

```
RIFE MODEL RECOMMENDATIONS (January 2026)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model 4.6    │ Highest quality, ~10-15% slower
Model 4.4    │ Great balance, works on 8GB VRAM for 4K
Model 4.24+  │ Minimum for diffusion model outputs (Practical-RIFE)
Model 4.0    │ Legacy, still works but outdated

RECOMMENDATION: Use Model 4.6 for final renders, Model 4.4 for previews
```

### Basic FFmpeg Interpolation

```bash
# FFmpeg's built-in minterpolate filter (no RIFE required)
# Good for quick 2x interpolation
ffmpeg -i input.mp4 -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:vsbmc=1" -c:v libx264 output_60fps.mp4

# Breakdown:
# fps=60          : Target framerate
# mi_mode=mci     : Motion compensated interpolation
# mc_mode=aobmc   : Adaptive overlapped block motion compensation
# vsbmc=1         : Variable block size motion compensation
```

### RIFE CLI Pipeline (Practical-RIFE)

```bash
#!/bin/bash
# rife_interpolate.sh - RIFE interpolation pipeline

INPUT=$1
OUTPUT=$2
SCALE=${3:-2}  # 2x interpolation by default

# Extract frames
mkdir -p frames_input frames_output
ffmpeg -i "$INPUT" frames_input/frame_%05d.png

# Run RIFE interpolation
python -m rife.inference_video \
    --input frames_input \
    --output frames_output \
    --exp $SCALE \
    --model rife46 \
    --fp16

# Get original FPS and calculate new FPS
ORIG_FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$INPUT")
NEW_FPS=$(echo "$ORIG_FPS * $((2**SCALE))" | bc)

# Re-encode with new framerate
ffmpeg -framerate $NEW_FPS \
    -i frames_output/frame_%05d.png \
    -c:v libx264 \
    -preset slow \
    -crf 18 \
    -pix_fmt yuv420p \
    "$OUTPUT"

# Cleanup
rm -rf frames_input frames_output

echo "Interpolated: $INPUT -> $OUTPUT at ${NEW_FPS}fps"
```

### RIFE + NCNN Vulkan (Cross-Platform)

```bash
# Download rife-ncnn-vulkan from GitHub releases
# Works on AMD/Intel/NVIDIA without CUDA

# Basic usage
./rife-ncnn-vulkan -i input_frames/ -o output_frames/ -m rife-v4.6

# With specific GPU
./rife-ncnn-vulkan -i input/ -o output/ -g 0 -m rife-v4.6

# Docker version (no local GPU dependencies)
docker run --rm -it --gpus all \
    -v $PWD:/host \
    rife:latest inference_video \
    --exp=1 \
    --video=input.mp4 \
    --output=interpolated.mp4
```

### AnimationKit-AI Integration

From X power users: AnimationKit-AI combines RIFE + Real-ESRGAN + FFmpeg in one pipeline.

```python
# AnimationKit workflow (GitHub: sadnow/AnimationKit-AI)
# Processes choppy Stable Diffusion outputs into high-FPS videos

# Install
!pip install animationkit-ai

# Usage
from animationkit import process_video

result = process_video(
    input_path="ai_output.mp4",
    output_path="enhanced.mp4",
    upscale=4,              # Real-ESRGAN 4x
    interpolate=2,          # RIFE 2x (24fps -> 48fps)
    face_enhance=True,      # GFPGAN for faces
    codec="hevc_nvenc"      # NVIDIA hardware encoding
)
```

---

## Real-ESRGAN Upscaling

### Overview

Real-ESRGAN is the standard for practical image/video upscaling, trained on synthetic degradation data for artifact-free results.

### Basic FFmpeg + Real-ESRGAN Pipeline

```bash
#!/bin/bash
# upscale_video.sh - Real-ESRGAN video upscaling

INPUT=$1
OUTPUT=$2
SCALE=${3:-4}  # 4x by default

# Extract frames at original resolution
mkdir -p frames upscaled_frames
ffmpeg -i "$INPUT" -vf "fps=30" frames/frame_%04d.png

# Run Real-ESRGAN on all frames
python inference_realesrgan.py \
    -n RealESRGAN_x4plus \
    -i frames \
    -o upscaled_frames \
    --outscale $SCALE \
    --face_enhance  # Optional: improves faces

# Re-encode at higher resolution
ffmpeg -framerate 30 \
    -i upscaled_frames/frame_%04d.png \
    -c:v libx264 \
    -preset slow \
    -crf 18 \
    -pix_fmt yuv420p \
    "$OUTPUT"

# Cleanup
rm -rf frames upscaled_frames
```

### Real-ESRGAN Model Options

```
MODEL SELECTION GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RealESRGAN_x4plus           │ General purpose, best quality
RealESRGAN_x4plus_anime_6B  │ Optimized for anime/cartoon
RealESRNet_x4plus           │ Faster, slightly lower quality
realesr-animevideov3        │ Specifically for anime video

COMBINATION WITH GFPGAN:
--face_enhance              │ Adds GFPGAN face restoration
                            │ Critical for talking head videos
```

### ComfyUI Integration

From X threads (@github.com): Power users run Real-ESRGAN in ComfyUI for node-based automation.

```
ComfyUI Extensions for Video Upscaling:
├── ComfyUI-VideoHelperSuite    → FFmpeg integration nodes
├── SeedVR2 Video Upscaler      → Real-ESRGAN for sequences
├── ComfyUI-RIFE                → Frame interpolation nodes
└── Meta Batch Manager          → Large video processing
```

---

## Processing Order Optimization

### The Golden Rule: Interpolate First, Upscale Second

```python
# CORRECT ORDER (Fast & Efficient)
def process_optimal(video_path):
    """
    1. Interpolate at original resolution (fast)
    2. Upscale the interpolated video (fewer duplicate calcs)
    """
    # Step 1: 24fps -> 60fps at 720p (fast)
    interpolated = rife_interpolate(video_path, target_fps=60)

    # Step 2: 720p -> 4K (upscale once, done)
    final = realesrgan_upscale(interpolated, scale=4)

    return final

# WRONG ORDER (Slow & Wasteful)
def process_suboptimal(video_path):
    """
    DON'T DO THIS:
    1. Upscale to 4K first
    2. Then interpolate 4K frames (SLOW, high VRAM)
    """
    # Step 1: 720p -> 4K (unnecessary work)
    upscaled = realesrgan_upscale(video_path, scale=4)

    # Step 2: Interpolate at 4K (SLOW, ~4x longer)
    final = rife_interpolate(upscaled, target_fps=60)

    return final
```

### Benchmark Comparison (5-second video)

| Pipeline Order | Time | VRAM Usage | Output Quality |
|---------------|------|------------|----------------|
| Interpolate → Upscale | **8 min** | **6 GB** | Excellent |
| Upscale → Interpolate | 32 min | 16 GB | Excellent |

---

## Batch Automation Scripts

### Simple Batch Interpolation

```bash
#!/bin/bash
# batch_interpolate.sh - Process all MP4s in directory

for file in *.mp4; do
    ffmpeg -i "$file" \
        -vf "minterpolate=fps=60" \
        "interpolated_$file"
done
```

### Parallel Batch Processing

```bash
#!/bin/bash
# parallel_process.sh - Parallel processing with GNU parallel

# Install: apt install parallel

find . -name "*.mp4" | parallel -j 4 '
    ffmpeg -i {} -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc" \
    -c:v libx264 -preset fast -crf 20 \
    {.}_60fps.mp4
'
```

### FFmpeg-Batch Tool Integration

From @techhalla on X: ffmpeg-batch supports downloading, processing, and encoding multiple videos.

```bash
# Install ffmpeg-batch (sedlar.me)
pip install ffmpeg-batch

# Batch process with config file
ffmpeg-batch config.yaml

# config.yaml example:
# input_dir: ./raw_videos
# output_dir: ./processed
# operations:
#   - interpolate: { fps: 60 }
#   - upscale: { scale: 2 }
#   - encode: { codec: h265, crf: 18 }
```

### Cloud-Based Batch Scaling

From @truefan.ai: GPU farms for batch rendering.

```python
# cloud_batch.py - RunPod/Modal batch processing

import modal

app = modal.App("video-processing")

@app.function(gpu="A100", timeout=3600)
def process_video(video_url: str):
    """Process single video on cloud GPU."""
    import subprocess

    # Download
    subprocess.run(["wget", video_url, "-O", "input.mp4"])

    # Interpolate
    subprocess.run([
        "python", "-m", "rife.inference_video",
        "--video", "input.mp4",
        "--output", "interpolated.mp4",
        "--exp", "1"
    ])

    # Upscale
    subprocess.run([
        "python", "inference_realesrgan.py",
        "-i", "interpolated.mp4",
        "-o", "final.mp4",
        "-n", "RealESRGAN_x4plus"
    ])

    return upload_to_storage("final.mp4")

# Process 100 videos in parallel
@app.function()
def batch_process(video_urls: list):
    results = []
    for url in video_urls:
        result = process_video.remote(url)
        results.append(result)
    return results
```

---

## Agentic Post-Production

### Claude AI + Remotion Pipeline

From @SamanyouGarg on X: Agentic editing with Claude AI.

```typescript
// remotion_claude_pipeline.ts
// Analyze video, transcribe audio, detect silences, auto-edit

import { bundle } from '@remotion/bundler';
import Anthropic from '@anthropic-ai/sdk';

interface VideoAnalysis {
    resolution: [number, number];
    fps: number;
    duration: number;
    silences: Array<{start: number, end: number}>;
    transcript: string;
}

async function agenticEdit(videoPath: string): Promise<string> {
    const anthropic = new Anthropic();

    // Step 1: Analyze video
    const analysis = await analyzeVideo(videoPath);

    // Step 2: Claude determines edit decisions
    const response = await anthropic.messages.create({
        model: "claude-sonnet-4-20250514",
        max_tokens: 4096,
        messages: [{
            role: "user",
            content: `Analyze this video and suggest edits:
            Resolution: ${analysis.resolution.join('x')}
            FPS: ${analysis.fps}
            Duration: ${analysis.duration}s
            Silences: ${JSON.stringify(analysis.silences)}
            Transcript: ${analysis.transcript}

            Suggest:
            1. Segments to cut (silences, filler words)
            2. Where to add crossfades
            3. Zoom points for emphasis
            4. Caption timing`
        }]
    });

    // Step 3: Execute edits with FFmpeg
    const editDecisions = parseClaudeResponse(response.content);
    return executeEdits(videoPath, editDecisions);
}

function executeEdits(video: string, decisions: EditDecisions): string {
    // Generate FFmpeg filter complex for all edits
    const filterComplex = buildFilterComplex(decisions);

    execSync(`ffmpeg -i ${video} -filter_complex "${filterComplex}" output.mp4`);

    return "output.mp4";
}
```

### Smart-FFmpeg with AI (GPT-5 Backend)

From @fofrAI on X: Prompt-based video editing.

```python
# smart_ffmpeg.py - Natural language video editing

import openai
from typing import List

class SmartFFmpeg:
    """
    Natural language interface to FFmpeg.
    Examples:
    - "make this trippy"
    - "2x2 grid of the video"
    - "reverse and slow down 2x"
    """

    def __init__(self):
        self.client = openai.OpenAI()

    def edit(self, video_path: str, instruction: str) -> str:
        """Execute natural language edit instruction."""

        # Get FFmpeg command from GPT-5
        response = self.client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": """You are an FFmpeg expert.
                Convert natural language video editing instructions to FFmpeg commands.
                Return ONLY the ffmpeg command, nothing else.
                Input video is always 'input.mp4', output is 'output.mp4'."""},
                {"role": "user", "content": f"Edit instruction: {instruction}"}
            ]
        )

        ffmpeg_cmd = response.choices[0].message.content.strip()

        # Execute
        import subprocess
        subprocess.run(ffmpeg_cmd.replace("input.mp4", video_path), shell=True)

        return "output.mp4"

# Usage
smart = SmartFFmpeg()
smart.edit("raw.mp4", "make a 2x2 grid with the video playing in each quadrant")
smart.edit("raw.mp4", "add a dreamy glow effect and slow down 50%")
smart.edit("raw.mp4", "trim first 2 seconds and last 3 seconds, add fade in/out")
```

### Auto-Editor CLI

From @Frankenmint on X: Silence removal and timeline export.

```bash
# Install auto-editor
pip install auto-editor

# Basic silence removal
auto-editor input.mp4 --margin 0.2s

# Export to Premiere Pro timeline (no re-encoding)
auto-editor input.mp4 --export premiere

# Export to DaVinci Resolve
auto-editor input.mp4 --export resolve

# Custom silence threshold
auto-editor input.mp4 --silent-threshold 0.03 --margin 0.1s

# Batch process directory
for f in *.mp4; do
    auto-editor "$f" --no-open --output "edited_$f"
done
```

---

## Full Pipeline Integration

### Complete Post-Processing Pipeline

```python
#!/usr/bin/env python3
"""
full_pipeline.py - Complete AI video post-processing pipeline

Workflow:
1. Detect and remove duplicate frames
2. Interpolate to target FPS (RIFE)
3. Upscale to target resolution (Real-ESRGAN)
4. Color correction and enhancement
5. Audio sync and processing
6. Final encoding
"""

import subprocess
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class PipelineConfig:
    input_path: str
    output_path: str
    target_fps: int = 60
    target_resolution: tuple = (3840, 2160)  # 4K
    upscale_model: str = "RealESRGAN_x4plus"
    rife_model: str = "rife46"
    codec: str = "libx264"
    crf: int = 18
    audio_normalize: bool = True
    remove_silence: bool = False

class PostProcessingPipeline:
    """Full post-processing pipeline for AI-generated videos."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.temp_dir = Path("./temp_pipeline")
        self.temp_dir.mkdir(exist_ok=True)

    def run(self) -> str:
        """Execute full pipeline."""

        current = self.config.input_path

        # Step 1: Deduplicate frames
        print("Step 1/6: Deduplicating frames...")
        current = self._deduplicate(current)

        # Step 2: Interpolate
        print("Step 2/6: Interpolating frames...")
        current = self._interpolate(current)

        # Step 3: Upscale
        print("Step 3/6: Upscaling...")
        current = self._upscale(current)

        # Step 4: Color correction
        print("Step 4/6: Color correction...")
        current = self._color_correct(current)

        # Step 5: Audio processing
        print("Step 5/6: Processing audio...")
        current = self._process_audio(current)

        # Step 6: Final encode
        print("Step 6/6: Final encoding...")
        final = self._final_encode(current)

        # Cleanup
        self._cleanup()

        return final

    def _deduplicate(self, input_path: str) -> str:
        """Remove duplicate frames using mpdecimate."""
        output = self.temp_dir / "deduped.mp4"

        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-vf", "mpdecimate,setpts=N/FRAME_RATE/TB",
            "-an",  # Process video only, add audio later
            str(output)
        ], check=True)

        return str(output)

    def _interpolate(self, input_path: str) -> str:
        """Interpolate using RIFE."""
        output = self.temp_dir / "interpolated.mp4"

        # Use rife-ncnn-vulkan for cross-platform compatibility
        frames_in = self.temp_dir / "frames_in"
        frames_out = self.temp_dir / "frames_out"
        frames_in.mkdir(exist_ok=True)
        frames_out.mkdir(exist_ok=True)

        # Extract frames
        subprocess.run([
            "ffmpeg", "-i", input_path,
            f"{frames_in}/frame_%05d.png"
        ], check=True)

        # Run RIFE
        subprocess.run([
            "./rife-ncnn-vulkan",
            "-i", str(frames_in),
            "-o", str(frames_out),
            "-m", self.config.rife_model
        ], check=True)

        # Reassemble at target FPS
        subprocess.run([
            "ffmpeg", "-framerate", str(self.config.target_fps),
            "-i", f"{frames_out}/frame_%05d.png",
            "-c:v", "libx264", "-crf", "15",
            str(output)
        ], check=True)

        return str(output)

    def _upscale(self, input_path: str) -> str:
        """Upscale using Real-ESRGAN."""
        output = self.temp_dir / "upscaled.mp4"

        frames_in = self.temp_dir / "upscale_in"
        frames_out = self.temp_dir / "upscale_out"
        frames_in.mkdir(exist_ok=True)
        frames_out.mkdir(exist_ok=True)

        # Extract frames
        subprocess.run([
            "ffmpeg", "-i", input_path,
            f"{frames_in}/frame_%05d.png"
        ], check=True)

        # Run Real-ESRGAN
        subprocess.run([
            "python", "inference_realesrgan.py",
            "-n", self.config.upscale_model,
            "-i", str(frames_in),
            "-o", str(frames_out)
        ], check=True)

        # Reassemble
        subprocess.run([
            "ffmpeg", "-framerate", str(self.config.target_fps),
            "-i", f"{frames_out}/frame_%05d.png",
            "-c:v", "libx264", "-crf", "15",
            str(output)
        ], check=True)

        return str(output)

    def _color_correct(self, input_path: str) -> str:
        """Apply color correction and enhancement."""
        output = self.temp_dir / "color_corrected.mp4"

        # FFmpeg color correction filter chain
        filters = [
            "eq=contrast=1.05:brightness=0.02:saturation=1.1",  # Slight boost
            "unsharp=5:5:0.5:5:5:0"  # Subtle sharpening
        ]

        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-vf", ",".join(filters),
            "-c:v", "libx264", "-crf", "15",
            str(output)
        ], check=True)

        return str(output)

    def _process_audio(self, input_path: str) -> str:
        """Process and normalize audio."""
        output = self.temp_dir / "with_audio.mp4"

        # Get original audio from input
        original_audio = self.temp_dir / "original_audio.aac"

        subprocess.run([
            "ffmpeg", "-i", self.config.input_path,
            "-vn", "-acodec", "copy",
            str(original_audio)
        ], check=True)

        if self.config.audio_normalize:
            # Normalize audio levels
            normalized_audio = self.temp_dir / "normalized_audio.aac"
            subprocess.run([
                "ffmpeg", "-i", str(original_audio),
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                str(normalized_audio)
            ], check=True)
            audio_source = normalized_audio
        else:
            audio_source = original_audio

        # Merge audio with processed video
        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-i", str(audio_source),
            "-c:v", "copy",
            "-c:a", "aac",
            "-map", "0:v:0",
            "-map", "1:a:0",
            str(output)
        ], check=True)

        return str(output)

    def _final_encode(self, input_path: str) -> str:
        """Final encoding pass with optimal settings."""
        output = self.config.output_path

        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-c:v", self.config.codec,
            "-preset", "slow",
            "-crf", str(self.config.crf),
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",  # Web optimization
            output
        ], check=True)

        return output

    def _cleanup(self):
        """Remove temporary files."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)


# CLI Interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Full video post-processing pipeline")
    parser.add_argument("input", help="Input video path")
    parser.add_argument("output", help="Output video path")
    parser.add_argument("--fps", type=int, default=60, help="Target FPS")
    parser.add_argument("--resolution", default="4k", choices=["1080p", "4k"])
    parser.add_argument("--crf", type=int, default=18, help="Quality (lower=better)")

    args = parser.parse_args()

    resolution = (1920, 1080) if args.resolution == "1080p" else (3840, 2160)

    config = PipelineConfig(
        input_path=args.input,
        output_path=args.output,
        target_fps=args.fps,
        target_resolution=resolution,
        crf=args.crf
    )

    pipeline = PostProcessingPipeline(config)
    result = pipeline.run()

    print(f"\nPipeline complete: {result}")
```

---

## Advanced FFmpeg Techniques

### RISC-V Assembly Optimization

From X discussions: RISC-V patches in FFmpeg for faster H.264 processing.

```bash
# Build FFmpeg with RISC-V optimizations (if on RISC-V hardware)
./configure --enable-riscv --enable-asm
make -j$(nproc)

# Results in ~30% faster H.264 encoding on RISC-V platforms
```

### Hardware Acceleration Encoding

```bash
# NVIDIA NVENC (fastest)
ffmpeg -i input.mp4 \
    -c:v hevc_nvenc \
    -preset p7 \
    -cq 20 \
    output_nvenc.mp4

# AMD AMF
ffmpeg -i input.mp4 \
    -c:v hevc_amf \
    -quality quality \
    output_amf.mp4

# Intel QuickSync
ffmpeg -i input.mp4 \
    -c:v hevc_qsv \
    -preset veryslow \
    output_qsv.mp4

# Apple VideoToolbox (M1/M2/M3)
ffmpeg -i input.mp4 \
    -c:v hevc_videotoolbox \
    -q:v 65 \
    output_vtb.mp4
```

### Professional Color Grading

```bash
# Apply LUT (Look-Up Table) for cinematic color
ffmpeg -i input.mp4 \
    -vf "lut3d=cinematic.cube" \
    -c:v libx264 -crf 18 \
    output_graded.mp4

# HDR to SDR conversion (for web delivery)
ffmpeg -i hdr_input.mp4 \
    -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" \
    -c:v libx264 -crf 18 \
    output_sdr.mp4
```

---

## X/Twitter Power User Workflows

### Key Accounts to Follow

| Handle | Specialty | Key Workflow |
|--------|-----------|--------------|
| @AIWarper | VQGAN+CLIP+RIFE | 324 frames → 2x interpolation |
| @techhalla | ffmpeg-batch | Bulk Higgsfield/Runway processing |
| @SamanyouGarg | Claude+Remotion | Agentic editing pipelines |
| @fofrAI | Smart-FFmpeg | GPT-5 prompt-based editing |
| @Frankenmint | auto-editor | Cross-editor silence removal |
| @LincolnMargison | Full chains | prompt→mesh→video→mocap→retarget |
| @Livepeer | Real-time AI | Minutes to seconds iteration |
| @AINativeF | VideoAR+RIFE | Multi-scale frame prediction |
| @Emo_wordsworth | Node limitations | Dynamic frame/audio continuity |

### Emerging Trends (January 2026)

1. **Full Automated Chains**: prompt → mesh/rig gen → video gen → mocap → retarget
2. **Real-time AI Processing**: Iteration time from minutes to seconds
3. **Agentic Editing**: Claude AI analyzing and auto-editing videos
4. **Smart-FFmpeg**: Natural language video editing via LLMs
5. **Cross-Editor Compatibility**: Tools like auto-editor working with Premiere, Resolve, FCP

---

## Quick Reference

### Essential Commands

```bash
# Quick 2x interpolation
ffmpeg -i input.mp4 -vf "minterpolate=fps=60" output_60fps.mp4

# Quick 4x upscale
python inference_realesrgan.py -n RealESRGAN_x4plus -i input.mp4 -o output_4x.mp4

# Remove silence
auto-editor input.mp4 --margin 0.2s

# Batch process directory
for f in *.mp4; do ffmpeg -i "$f" -vf "minterpolate=fps=60" "processed_$f"; done

# Full pipeline (interpolate + upscale)
./full_pipeline.py input.mp4 output.mp4 --fps 60 --resolution 4k
```

### Recommended Software Stack

```
INTERPOLATION:
├── Practical-RIFE (Python, CUDA)
├── rife-ncnn-vulkan (CLI, cross-platform)
└── Flowframes (GUI, Windows)

UPSCALING:
├── Real-ESRGAN (Python, CUDA)
├── Video2X (Python wrapper)
└── Topaz Video AI (GUI, commercial)

AUTOMATION:
├── FFmpeg (core processing)
├── auto-editor (silence removal)
├── AnimationKit-AI (full pipeline)
└── Claude Code (orchestration)

ENCODING:
├── FFmpeg + libx264/libx265
├── NVENC (NVIDIA hardware)
└── HandBrake (GUI alternative)
```

---

*FFmpeg Post-Processing Pipeline Guide v1.0 — January 18, 2026*
*Sources: Grok X search (11 posts, 9 web pages), GitHub, Reddit r/StableDiffusion*

# ComfyUI & Node-Based Video Workflows Guide

*January 2026 Edition*

Comprehensive guide to node-based video AI workflows, with focus on ComfyUI ecosystem.

---

## Table of Contents

1. [ComfyUI Video Ecosystem](#comfyui-video-ecosystem)
2. [Essential Node Packages](#essential-node-packages)
3. [Core Video Workflows](#core-video-workflows)
4. [Model Integration Guides](#model-integration-guides)
5. [VRAM Optimization](#vram-optimization)
6. [Alternative Node Platforms](#alternative-node-platforms)
7. [Automation & Orchestration](#automation--orchestration)

---

## ComfyUI Video Ecosystem

### Overview

ComfyUI has become the de facto standard for node-based video AI workflows as of January 2026. The ecosystem now supports:

- **Native video generation** (LTX-2, Wan, HunyuanVideo)
- **Video-to-video transformation** (ControlNet Video)
- **Frame interpolation** (FILM, RIFE)
- **Upscaling** (RealESRGAN Video, Topaz integration)
- **Audio synchronization** (LTX-2 native audio)

### Installation

```bash
# Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Install dependencies
pip install -r requirements.txt

# Install ComfyUI Manager (essential)
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git

# Start ComfyUI
cd ..
python main.py
```

### Recommended Hardware (Jan 2026)

| Configuration | VRAM | Use Case |
|---------------|------|----------|
| Minimum | 8GB | LTX-2, Wan with FP8 |
| Recommended | 16GB | Most workflows |
| Professional | 24GB+ | Multi-model, high-res |

---

## Essential Node Packages

### Kijai's Video Nodes

**The most important contributor to ComfyUI video.** Kijai has ported nearly every major video model.

```bash
# Via ComfyUI Manager, search for:
# - ComfyUI-WanVideoWrapper
# - ComfyUI-HunyuanVideoWrapper
# - ComfyUI-CogVideoXWrapper
```

**Kijai's Packages:**

| Package | Models | Features |
|---------|--------|----------|
| WanVideoWrapper | Wan 2.1, 2.2, 2.6 | Full MoE support, I2V, T2V |
| HunyuanVideoWrapper | HunyuanVideo | T2V, I2V, high quality |
| CogVideoXWrapper | CogVideoX | Fast generation |
| MochiWrapper | Mochi 1 | OSS alternative |

### LTX-2 Native Nodes

LTX-2 has Day 0 ComfyUI support (released Jan 6, 2026):

```bash
# Native nodes - no wrapper needed
# Load via standard ComfyUI model loader
```

**LTX-2 Node Types:**

| Node | Function |
|------|----------|
| LTXVideoLoader | Load model checkpoint |
| LTXVideoSampler | Generation sampling |
| LTXControlNet | Canny/Depth/Pose control |
| LTXAudioSync | Audio-video sync |

### ControlNet Video Nodes

Essential for video-to-video workflows:

```bash
# Install via ComfyUI Manager
# Search: ComfyUI-ControlNet-Aux
# Search: ComfyUI-VideoHelperSuite
```

**Control Types:**

| Type | Best For |
|------|----------|
| Canny | Edge preservation, line art |
| Depth | 3D structure, parallax |
| Pose | Human movement transfer |
| Normal | Surface detail preservation |
| Softedge | Gentle guidance |

### Video Helper Suite

Critical utility nodes for video workflows:

| Node | Function |
|------|----------|
| LoadVideoPath | Load video from disk |
| LoadVideoUpload | Browser upload |
| VideoCombine | Merge video sequences |
| ExtractFrames | Video → image sequence |
| BatchManager | Handle frame batches |

---

## Core Video Workflows

### 1. Text-to-Video (T2V)

Basic text-to-video generation:

```
[CLIPTextEncode] → [KSampler] → [VAEDecode] → [VideoCombine]
       ↑                ↑
  [Prompt]      [ModelLoader]
```

**Wan 2.6 T2V Example:**
```
Load Checkpoint (wan-2.6)
    ↓
CLIP Text Encode (positive prompt)
    ↓
CLIP Text Encode (negative prompt)
    ↓
Wan Video Sampler
    - steps: 30
    - cfg: 7.0
    - num_frames: 81
    ↓
VAE Decode
    ↓
Video Combine (output.mp4)
```

### 2. Image-to-Video (I2V)

Start frame guided generation:

```
[LoadImage] → [ImageEncode] → [I2VSampler] → [Decode] → [VideoCombine]
                    ↑
            [TextPrompt]
```

**Settings for I2V:**
- `image_strength`: 0.7-0.9 (higher = more faithful)
- `motion_bucket_id`: 127 (default, adjust for motion)
- `fps`: 8-24 (generation fps, not output)

### 3. First-Last Frame (FLF2V)

Generate video between two keyframes:

```
[FirstFrame] ──┐
               ├→ [FLFSampler] → [Decode] → [VideoCombine]
[LastFrame]  ──┘
       ↑
  [MotionPrompt]
```

**Key Parameters:**
- `interpolation_strength`: How much AI fills the gap
- `frame_count`: Number of intermediate frames
- `motion_guidance`: Text description of movement

### 4. Video-to-Video (V2V)

Style transfer or transformation:

```
[LoadVideo] → [ExtractFrames] → [ControlNetApply] → [Sampler] → [Combine]
                    ↓                    ↑
              [DepthEstimate]    [StylePrompt]
```

**V2V Control Strengths:**
- `0.3-0.5`: Loose guidance, creative freedom
- `0.5-0.7`: Balanced, recommended default
- `0.7-0.9`: Tight adherence to source

### 5. Multi-Shot Consistency

Maintaining character across clips:

```
[CharacterSheet] → [FeatureExtract] → [Shot1Sampler] ─┐
                                      [Shot2Sampler] ─┼→ [Concatenate]
                                      [Shot3Sampler] ─┘
```

**Consistency Techniques:**
- Use IP-Adapter for face/character consistency
- Reference image conditioning on each shot
- Consistent negative prompts across shots
- Same seed family (seed, seed+1, seed+2)

---

## Model Integration Guides

### Wan 2.6 (via Kijai)

**Model Download:**
```
# Via HuggingFace
huggingface-cli download Kijai/WanVideo_comfy --local-dir models/wan/
```

**Recommended Settings:**
```
Model: wan-2.6-1.3B (for 16GB VRAM)
       wan-2.6-14B (for 24GB+ VRAM)
Sampler: uni_pc_bh2
Steps: 30
CFG: 7.0
Num Frames: 81 (for ~5s at 16fps)
FP8: true (for VRAM savings)
```

**Wan Style Tokens:**
- Include anime/style keywords in prompt
- Use MoE expert hints: "anime style", "realistic style"
- Negative: "blurry, low quality, distorted"

### LTX-2 (Native)

**Model Download:**
```
# Official weights
huggingface-cli download Lightricks/LTX-Video-2 --local-dir models/ltx2/
```

**Recommended Settings:**
```
Steps: 50
CFG: 7.5
Width: 768 or 1024
Height: 512 or 576
Frames: 121 (for 5s at 24fps)
Audio: enabled (for dialogue/SFX)
```

**Control Integration:**
- Use LTXControlNet node for Canny/Depth/Pose
- Strength 0.6-0.8 for balanced control
- Preprocessors: MiDaS for depth, OpenPose for pose

### HunyuanVideo (via Kijai)

**Model Download:**
```
# Large model - 13B parameters
huggingface-cli download Kijai/HunyuanVideo_comfy --local-dir models/hunyuan/
```

**Recommended Settings:**
```
Steps: 40
CFG: 6.0
Num Frames: 65
FP8: highly recommended
VAE Tiling: enabled for high-res
```

**Notes:**
- Slower than Wan/LTX-2
- Higher quality for realistic content
- Requires more VRAM even with FP8

---

## VRAM Optimization

### FP8 Quantization

Reduces model memory by ~50%:

```
# In node settings
Model Precision: fp8_e4m3fn
VAE Precision: fp16 (or fp8)
```

**FP8 Compatibility:**
- Wan 2.x: ✅ Full support
- LTX-2: ✅ Full support
- HunyuanVideo: ✅ Recommended
- CogVideoX: ⚠️ Quality loss

### Workflow Chaining

Avoid reloading models between generations:

```
[ModelLoader] → [Sampler1] → [Sampler2] → [Sampler3]
     ↓              ↓            ↓            ↓
  (cached)     (vid1.mp4)  (vid2.mp4)  (vid3.mp4)
```

### Tiled Processing

For high-resolution outputs:

```
# Enable tiling in VAE
VAE Tiling: true
Tile Size: 512
Overlap: 64
```

### Offloading Strategies

```
# CPU offload settings
model_management:
  vram_mode: lowvram
  cpu_offload: true
  attention_offload: true
```

### Memory-Efficient Attention

```
# Use xformers or flash attention
--use-pytorch-cross-attention  # fallback
--use-xformers                  # recommended
```

---

## Alternative Node Platforms

### Weavy

**Status:** Not a video AI tool. Figma-style automation platform.

Could potentially integrate via:
- API nodes connecting to video AI services
- Webhook triggers for batch processing
- Visual automation of non-video tasks

**Verdict:** Not recommended for video AI workflows.

### Flora Fauna AI

**Focus:** Motion and animation, especially organic/nature content.

**Integration:**
- API available for external calls
- Could chain via HTTP request nodes
- Specialized for specific aesthetic

**Use Case:** Nature documentaries, organic motion

### n8n (Workflow Automation)

**Not a visual node editor for AI, but useful for orchestration:**

```json
{
  "workflow": [
    {"node": "Webhook", "action": "receive_prompt"},
    {"node": "HTTP Request", "action": "call_fal_api"},
    {"node": "Wait", "action": "poll_completion"},
    {"node": "Download", "action": "save_video"},
    {"node": "Email", "action": "notify_user"}
  ]
}
```

**Best For:** Batch processing pipelines, multi-service orchestration

### BuildShip

**No-code backend for API orchestration:**

- Connect multiple video AI APIs
- Build microservices without code
- Trigger-based automation

**Use Case:** Production pipelines, API aggregation

---

## Automation & Orchestration

### ComfyUI API Mode

Run ComfyUI as a server for automation:

```bash
python main.py --listen 0.0.0.0 --port 8188
```

**API Endpoint:**
```python
import requests
import json

workflow = json.load(open("workflow.json"))

response = requests.post(
    "http://localhost:8188/prompt",
    json={"prompt": workflow}
)

prompt_id = response.json()["prompt_id"]
```

### Claude Code Integration

Use Claude Code to orchestrate ComfyUI:

```bash
# Example Claude Code slash command
/video-gen "A cat playing piano" --model wan26 --frames 81
```

**Implementation:**
1. Claude Code calls ComfyUI API
2. Polls for completion
3. Downloads result
4. Chains with ffmpeg for post-processing

### Batch Processing Script

```python
import os
import json
import requests

prompts = [
    "A sunrise over mountains",
    "A city street at night",
    "Ocean waves on a beach"
]

for i, prompt in enumerate(prompts):
    workflow = load_workflow("base_t2v.json")
    workflow["6"]["inputs"]["text"] = prompt

    response = requests.post(
        "http://localhost:8188/prompt",
        json={"prompt": workflow}
    )

    # Wait and download result
    # ... polling logic ...

    print(f"Generated video {i+1}/{len(prompts)}")
```

### ffmpeg Post-Processing Chain

```bash
# Upscale with ffmpeg
ffmpeg -i output.mp4 -vf "scale=3840:2160:flags=lanczos" output_4k.mp4

# Add audio track
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac final.mp4

# Concatenate clips
ffmpeg -f concat -i clips.txt -c copy combined.mp4

# Frame interpolation prep
ffmpeg -i input.mp4 -r 60 interpolated.mp4
```

---

## Recommended Workflow Stacks

### Anime/Stylized Production

1. **Frame Gen:** MidJourney Niji 7 / FLUX
2. **Video:** Wan 2.6 via Kijai nodes
3. **Control:** Canny + Pose ControlNet
4. **Upscale:** RealESRGAN-anime
5. **Post:** DaVinci Resolve

### Realistic/Cinematic

1. **Frame Gen:** FLUX or Ideogram
2. **Video:** LTX-2 or HunyuanVideo
3. **Control:** Depth + Normal
4. **Audio:** LTX-2 native or ElevenLabs
5. **Post:** Premiere + After Effects

### Rapid Prototyping

1. **Iteration:** Pika / Krea Nano Banana
2. **Refine:** Kling 2.6 native
3. **Control:** Minimal (text-only)
4. **Post:** Quick cut in Premiere

### OSS-Only Pipeline

1. **Frame Gen:** FLUX or SDXL
2. **Video:** LTX-2 (fully open)
3. **Control:** ControlNet (open)
4. **Upscale:** RealESRGAN (open)
5. **Post:** DaVinci Resolve (free)

---

*Guide compiled January 18, 2026*
*Kijai remains the MVP of ComfyUI video*

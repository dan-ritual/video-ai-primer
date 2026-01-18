# Start/Stop Frame Deep Dive

*January 2026 Edition*

Mastering the First-Last Frame workflow for controlled video generation.

---

## Table of Contents

1. [The First-Last Frame Revolution](#the-first-last-frame-revolution)
2. [Nano Banana Pro Workflows](#nano-banana-pro-workflows)
3. [Niji 7 Anime Workflows](#niji-7-anime-workflows)
4. [FLF2V Technical Deep Dive](#flf2v-technical-deep-dive)
5. [Platform-Specific Implementations](#platform-specific-implementations)
6. [Advanced Multi-Frame Techniques](#advanced-multi-frame-techniques)
7. [Production Recipes](#production-recipes)
8. [Troubleshooting & Optimization](#troubleshooting--optimization)

---

## The First-Last Frame Revolution

### Why Start/Stop Frames Matter

The First-Last Frame (FLF) paradigm represents the most controllable approach to AI video generation. Instead of hoping the model interprets your prompt correctly, you define exactly where the video starts and ends.

```
TRADITIONAL TEXT-TO-VIDEO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Prompt] → [Model Interpretation] → [Unpredictable Output]

FIRST-LAST FRAME (FLF)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Start Frame] + [End Frame] → [Deterministic Transition] → [Controlled Output]
```

### The Control Advantage

| Method | Control Level | Consistency | Speed | Cost |
|--------|--------------|-------------|-------|------|
| Text-to-Video | Low | Variable | Fast | $ |
| Image-to-Video (I2V) | Medium | Good | Fast | $ |
| First-Last Frame (FLF) | High | Excellent | Medium | $$ |
| Multi-Keyframe | Highest | Excellent | Slow | $$$ |

### Core Platforms Supporting FLF

```
NATIVE FLF SUPPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Wan 2.1/2.2 FLF2V (via ComfyUI)
├── Native first-last frame model
├── 720p HD output
├── Open source, local runnable
└── Best for: Anime, stylized content

Kling 2.6 (End Frame Feature)
├── Multi-version with end frame control
├── 1080p output
├── Commercial API available
└── Best for: Realistic content, variations

Runway Gen-4.5 (Motion Reference)
├── Motion brush + reference system
├── Up to 4K output
├── Professional quality
└── Best for: Commercial production

Krea.ai (Visual Interface)
├── Node-based workflow
├── Multiple model access
├── Beginner-friendly
└── Best for: Quick iteration
```

---

## Nano Banana Pro Workflows

### Understanding Nano Banana Pro

Nano Banana Pro (Gemini 3 Pro Image) represents Google's state-of-the-art in image generation, with unique features that make it ideal for video frame preparation.

```
UNIQUE CAPABILITIES FOR VIDEO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SEQUENTIAL FRAME GENERATION
   Generate frames one-by-one in storyboard mode
   Characters maintain identity across frames

2. NATURAL LANGUAGE EDITING
   "Make the character turn slightly right"
   "Add motion blur to suggest movement"

3. CHARACTER LOCK
   Automatic identity preservation
   Works across different poses and expressions

4. FRAME-ACCURATE HINTS
   Timing annotations for motion
   Professional squash-and-stretch suggestions
```

### Workflow 1: Basic Start/End Frame Generation

```python
# Nano Banana Pro API Workflow (Pseudocode)

# Step 1: Generate Start Frame
start_prompt = """
A young woman with short black hair in a red dress,
standing at a train station platform, morning light,
film photography style, composition for animation
"""

start_frame = nanobananap_pro.generate(
    prompt=start_prompt,
    resolution="1920x1080",
    style="cinematic",
    character_mode="lock"  # Enable character lock
)

# Step 2: Generate End Frame (Same Character)
end_prompt = """
Same woman, now seated on the train,
looking out the window, warm interior lighting,
same film photography style, slight smile
"""

end_frame = nano_banana_pro.generate(
    prompt=end_prompt,
    resolution="1920x1080",
    style="cinematic",
    character_reference=start_frame,  # Lock to start frame
    character_mode="lock"
)

# Step 3: Pass to Video Model
video = wan_flf2v.generate(
    start_frame=start_frame,
    end_frame=end_frame,
    duration=5,
    motion_style="smooth"
)
```

### Workflow 2: Storyboard Mode

```
STORYBOARD GENERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Define Storyboard
"Generate a 10-frame storyboard showing:
 Frame 1: Character enters room
 Frame 2: Looks around curiously
 Frame 3: Notices object on table
 Frame 4: Walks toward table
 Frame 5: Reaches for object
 Frame 6: Picks up object
 Frame 7: Examines closely
 Frame 8: Reacts with surprise
 Frame 9: Puts object down
 Frame 10: Exits room"

Step 2: Generate Frames
- Frames generated sequentially
- Character locked across all frames
- Lighting consistent
- Camera angles logical

Step 3: Create Video Segments
- Frames 1-2 → Video Segment A
- Frames 2-3 → Video Segment B
- ... etc.
- Concatenate with transitions
```

### Workflow 3: Motion Planning

```
MOTION-AWARE FRAME GENERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nano Banana Pro with motion hints:

Prompt Enhancement:
"Character in starting pose for walk cycle,
 weight on left foot, right arm forward,
 slight forward lean suggesting impending movement"

End Frame:
"Same character completing stride,
 weight now on right foot, left arm forward,
 natural follow-through position"

These specific pose instructions help the video
model interpolate realistic motion between frames.
```

### Best Practices for Nano Banana Pro

```
DO:
✓ Use character_mode="lock" for consistency
✓ Describe poses with animation terminology
✓ Maintain lighting direction across frames
✓ Keep background elements consistent
✓ Use high resolution (1080p+)

DON'T:
✗ Change clothing/accessories between frames
✗ Dramatically shift camera angles
✗ Alter character proportions
✗ Mix different art styles
✗ Forget to specify important details
```

---

## Niji 7 Anime Workflows

### Why Niji 7 for Anime FLF

Niji 7's January 2026 release brought critical improvements for anime video production:

```
NIJI 7 ADVANTAGES FOR FLF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. COHERENCY LEAP
   - Fine details (eyes, reflections) dramatically improved
   - Consistent character rendering
   - "Anime screenshot" keyword produces authentic frames

2. --sref UPGRADE
   - Style reference more reliable
   - Reduced style drift between frames
   - Better preservation of artistic intent

3. PROMPT LITERALITY
   - Complex poses accurately reproduced
   - Specific details honored
   - Multi-element compositions work
```

### Workflow 1: Character Turnaround for Video

```
STEP 1: Generate Character Sheet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/imagine character turnaround sheet,
[detailed character description],
front view, three-quarter view, side view, back view,
anime style, white background, full body,
consistent design --niji 7 --ar 16:9

Example:
/imagine character turnaround sheet,
young woman with long silver hair in ponytail,
violet eyes, black and red school uniform,
athletic build, confident expression,
front view, three-quarter view, side view, back view,
anime style, white background, full body,
consistent design --niji 7 --ar 16:9
```

```
STEP 2: Generate Start Frame
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/imagine [character description],
standing at school entrance gate,
morning sunlight, sakura petals falling,
looking forward with determination,
anime screenshot, cinematic composition,
detailed background --niji 7 --ar 16:9 --sref [url_of_turnaround]
```

```
STEP 3: Generate End Frame
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/imagine same character [description],
now walking through the gate,
same morning sunlight, sakura petals,
slight smile, hair flowing from movement,
anime screenshot, same cinematic style,
matching background --niji 7 --ar 16:9 --sref [same_url]
```

### Workflow 2: Action Sequence Frames

```
ANIME ACTION WORKFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For dynamic anime sequences, generate key poses:

Frame A (Wind-up):
/imagine [character] in fighting stance,
weight shifting back, fist drawn back,
intense expression, motion lines,
dramatic anime lighting, speed lines in background
--niji 7 --ar 16:9

Frame B (Impact):
/imagine same character,
punch extended, opponent recoiling,
impact effect stars, dramatic shadows,
matching style --niji 7 --ar 16:9 --sref [frame_a_url]

Frame C (Follow-through):
/imagine same character,
follow-through pose, triumphant expression,
settling dust/debris, same lighting
--niji 7 --ar 16:9 --sref [frame_a_url]

Then: A→B, B→C as separate FLF video generations
```

### Workflow 3: PsyopAnime-Style Production

Based on analysis of PsyopAnime's workflow patterns:

```
PSYOPANIME PRODUCTION APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 1: Character & Style Lock
├── Generate definitive character references
├── Establish consistent style parameters
├── Create lighting/color palette reference
└── Document all --sref values

PHASE 2: Storyboard Frame Generation
├── Script to shot breakdown
├── Generate key frames with Niji 7
├── Maintain style continuity
└── Flag frames needing regeneration

PHASE 3: Video Generation
├── Use Kling for realistic motion
├── Use Wan 2.6 --expert anime for stylized
├── FLF between key frames
└── Batch process similar shots

PHASE 4: Post-Production
├── Compile in NLE
├── Add sound design
├── Color grade for consistency
└── Export final
```

### Niji 7 Best Practices

```
PROMPT STRUCTURE FOR FLF:
[subject] + [action/pose] + [environment] + [lighting] +
[style: "anime screenshot"] + [composition] --niji 7 --ar 16:9 --sref [url]

CRITICAL KEYWORDS:
• "anime screenshot" - Production aesthetic
• "detailed eyes" - Niji 7's strength
• "consistent style" - Reinforces coherence
• Specific pose descriptions - Literal interpretation

SEED MANAGEMENT:
• Save seeds for successful generations
• Use seed families: seed, seed+1, seed+2
• Document seed + prompt combinations
```

---

## FLF2V Technical Deep Dive

### Wan 2.1/2.2 FLF2V Architecture

```
MODEL ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Input:
├── Start Frame (Image)
├── End Frame (Image)
└── Optional: Text prompt for motion guidance

Processing:
├── Encode both frames to latent space
├── Interpolate latent trajectory
├── Decode intermediate frames
└── Apply temporal consistency

Output:
├── 720p HD video (default)
├── Variable frame count
└── Smooth transition between frames
```

### ComfyUI FLF2V Workflow

```json
{
  "workflow_name": "WAN_FLF2V_Basic",
  "nodes": [
    {
      "id": 1,
      "type": "LoadImage",
      "title": "Start Frame",
      "inputs": {"image": "start_frame.png"}
    },
    {
      "id": 2,
      "type": "LoadImage",
      "title": "End Frame",
      "inputs": {"image": "end_frame.png"}
    },
    {
      "id": 3,
      "type": "WanFLF2VLoader",
      "title": "Load FLF Model",
      "inputs": {
        "model": "wan2.2_flf2v_720p.safetensors"
      }
    },
    {
      "id": 4,
      "type": "WanFLF2VSampler",
      "title": "Generate Video",
      "inputs": {
        "model": ["3", 0],
        "start_frame": ["1", 0],
        "end_frame": ["2", 0],
        "num_frames": 81,
        "steps": 30,
        "cfg": 7.0,
        "seed": 12345
      }
    },
    {
      "id": 5,
      "type": "VHS_VideoCombine",
      "title": "Export Video",
      "inputs": {
        "images": ["4", 0],
        "frame_rate": 24,
        "filename": "output"
      }
    }
  ]
}
```

### Parameter Optimization

```
SAMPLING PARAMETERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

num_frames:
├── 49 frames = ~2 seconds at 24fps
├── 81 frames = ~3.4 seconds (default)
├── 129 frames = ~5.4 seconds
└── More frames = smoother but slower

steps:
├── 20 steps = Fast, acceptable quality
├── 30 steps = Balanced (recommended)
├── 50 steps = Maximum quality
└── Diminishing returns above 50

cfg (Classifier-Free Guidance):
├── 5.0 = More creative, may drift
├── 7.0 = Balanced (recommended)
├── 9.0 = Strict to frames, may artifact
└── Adjust based on frame similarity

seed:
├── Fixed seed = Reproducible results
├── Random = Exploration
└── Document successful seeds
```

### Quality Optimization

```
FOR HIGHEST QUALITY FLF:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FRAME PREPARATION
   • Match resolution exactly between frames
   • Use same aspect ratio
   • Ensure similar lighting conditions
   • Keep character scale consistent

2. CONTENT COMPATIBILITY
   • Avoid impossible transitions (teleportation)
   • Keep camera angle change minimal
   • Maintain environment continuity
   • Character pose should be interpolable

3. GENERATION SETTINGS
   • Higher steps for complex motion
   • Lower CFG if frames are very different
   • More frames for subtle transitions
   • Fewer frames for quick actions
```

---

## Platform-Specific Implementations

### Krea.ai FLF Workflow

```
KREA.AI INTERFACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Navigate to Video section
2. Select "Image to Video" or "Multi-reference"
3. Upload start frame
4. Upload end frame (if supported)
5. Select model (Wan 2.5, Kling 2.5, etc.)
6. Adjust duration and settings
7. Generate

Krea Advantage:
• Visual node interface
• Multiple model access
• No local GPU needed
• Quick iteration
```

### Kling 2.6 End Frame Feature

```
KLING END FRAME WORKFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature: "Multi-Version + End Frame"
Purpose: Generate variations landing on specific final state

Usage:
1. Upload start frame
2. Enable "End Frame" option
3. Upload target end frame
4. Set duration
5. Generate

Best For:
• Product transformations
• Character pose changes
• Scene transitions
• Controlled narratives
```

### Runway Gen-4.5 Motion Reference

```
RUNWAY MOTION REFERENCE APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Runway's approach differs from pure FLF:

1. Start Frame + Motion Reference
   └── Define how motion should flow

2. Motion Brush
   └── Paint specific areas to animate

3. Style Reference
   └── Maintain visual consistency

4. Keyframe System
   └── Multiple control points

Best For:
• Complex professional work
• When motion direction matters
• High-budget production
• Maximum control needed
```

---

## Advanced Multi-Frame Techniques

### Keyframe Chaining

```
MULTI-KEYFRAME SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Instead of just start/end, use multiple keyframes:

[KF1] → [KF2] → [KF3] → [KF4] → [KF5]

Generate: KF1→KF2, KF2→KF3, KF3→KF4, KF4→KF5

Benefits:
• More control over motion arc
• Handle complex sequences
• Better consistency
• Easier debugging

Example (Character Walking):
KF1: Standing still
KF2: Left foot forward (mid-stride)
KF3: Right foot forward
KF4: Left foot forward
KF5: Stopping pose

Each segment = short FLF, concatenated
```

### Parallel Processing Pipeline

```python
# Parallel FLF Processing for Long Sequences

import asyncio
from wan_flf2v import WanFLF2V

async def generate_segment(model, start, end, segment_id):
    """Generate single FLF segment."""
    result = await model.generate(
        start_frame=start,
        end_frame=end,
        num_frames=81
    )
    return segment_id, result

async def generate_sequence(keyframes):
    """Generate all segments in parallel."""
    model = WanFLF2V()
    tasks = []

    for i in range(len(keyframes) - 1):
        task = generate_segment(
            model,
            keyframes[i],
            keyframes[i + 1],
            segment_id=i
        )
        tasks.append(task)

    # Run all segments in parallel
    results = await asyncio.gather(*tasks)

    # Sort by segment_id and concatenate
    results.sort(key=lambda x: x[0])
    return concatenate_videos([r[1] for r in results])
```

### Frame Interpolation Enhancement

```
POST-GENERATION ENHANCEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After FLF generation, enhance with:

RIFE (Frame Interpolation):
• Double or quadruple frame rate
• Smoother motion
• 24fps → 48fps → 60fps

Command:
rife-ncnn-vulkan -i input.mp4 -o output.mp4 -m rife-v4.6

Topaz Video AI:
• AI frame interpolation
• Motion blur addition
• Artifact reduction

Best Practice:
1. Generate at target resolution
2. Interpolate to higher fps
3. Add subtle motion blur
4. Export final
```

---

## Production Recipes

### Recipe 1: Anime Character Introduction (30 seconds)

```
ANIME CHARACTER INTRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tools: Niji 7 + Wan 2.6 FLF2V
Time: 2-3 hours
Cost: ~$10-20

KEYFRAMES:
KF1: Wide shot - Character silhouette against dramatic sky
KF2: Medium shot - Character turns, face partially visible
KF3: Close-up - Full face reveal, eyes open
KF4: Wide shot - Character in action pose
KF5: Hero shot - Final dramatic pose

GENERATION:
For each KF pair, generate with Niji 7 + --sref
Process through Wan 2.6 --expert anime
Concatenate with crossfades

POST:
Add dramatic anime music
Sound design (whooshes, impacts)
Color grade for consistency
```

### Recipe 2: Product Transformation (15 seconds)

```
PRODUCT TRANSFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tools: FLUX.2 Pro + Kling 2.6 End Frame
Time: 1-2 hours
Cost: ~$5-15

KEYFRAMES:
KF1: Product in closed state (box, folded, etc.)
KF2: Mid-transformation
KF3: Product fully revealed

GENERATION:
Generate frames with FLUX.2 Pro (same seed family)
Use Kling End Frame feature
Enable face lock if human elements present

POST:
Add satisfying SFX
Subtle music bed
Export multiple aspect ratios
```

### Recipe 3: Music Video Scene (10 seconds)

```
MUSIC VIDEO SCENE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tools: Nano Banana Pro + Seedance/Veo 3.1
Time: 1 hour
Cost: ~$5-10

APPROACH:
1. Analyze music beat structure
2. Place keyframes on beats
3. Generate frames with motion hints
4. Process with audio-aware model

KEYFRAMES (synced to downbeats):
Beat 1: Pose A (tension)
Beat 5: Pose B (release)
Beat 9: Pose C (impact)

GENERATION:
Nano Banana Pro with motion hints
Seedance for beat-reactive animation
OR Veo 3.1 with audio prompt
```

---

## Troubleshooting & Optimization

### Common Issues & Solutions

```
ISSUE: Characters morph between frames
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cause: Frames too different, model inventing details
Fix:
• Use same model + settings for both frames
• Apply --sref from first frame to second
• Reduce pose difference between frames
• Use higher CFG (8-9)

ISSUE: Motion is unnatural/jerky
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cause: Insufficient frames or impossible transition
Fix:
• Increase num_frames
• Add intermediate keyframe
• Ensure poses are physically interpolable
• Try lower CFG for more freedom

ISSUE: Style/lighting changes mid-video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cause: Frames have inconsistent style/lighting
Fix:
• Match lighting direction exactly
• Use same prompt elements
• Apply style reference
• Color correct in post

ISSUE: Background elements shift
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cause: Model regenerating background
Fix:
• More detailed background description
• Use ControlNet depth/normal
• Keep background simpler
• Mask background in post
```

### Performance Optimization

```
SPEED OPTIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For faster generation:
• Use FLUX Schnell for iteration frames
• Lower steps (20 instead of 30)
• Smaller frame count for tests
• Batch similar requests

VRAM OPTIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For limited VRAM:
• Use FP8 quantization
• Process at 720p, upscale after
• Reduce num_frames
• Close other applications

QUALITY OPTIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For maximum quality:
• Generate frames at 2K+, downscale
• 50 steps, CFG 7.0
• Frame interpolation in post
• Professional color grading
```

---

*Start/Stop Frame Deep Dive v1.0 — January 18, 2026*

Sources:
- [Wan FLF2V Workflow](https://www.runcomfy.com/comfyui-workflows/wan-2-1-flf2v-first-last-frame-video-generation)
- [Wan 2.2 FLF2V Tutorial](https://www.nextdiffusion.ai/tutorials/wan-22-first-last-frame-video-generation-in-comfyui)
- [Niji 7 Guide](https://domoai.app/blog/niji-7-guide-animate-ai-anime)
- [Nano Banana Frame Generation](https://nanobanana.io/image-to-video)

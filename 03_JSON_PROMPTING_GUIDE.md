# JSON/Structured Prompting Guide for Video AI Models

*January 2026 Edition*

This guide provides detailed JSON schemas, structured prompting techniques, and best practices for each major video AI model.

---

## Table of Contents

1. [Veo 3.1 (Google)](#veo-31-google)
2. [Kling 2.5/2.6 (Kuaishou)](#kling-2526-kuaishou)
3. [Sora 2/Pro (OpenAI)](#sora-2pro-openai)
4. [Runway Gen-4/4.5](#runway-gen-445)
5. [Wan 2.1-2.6 (Alibaba)](#wan-21-26-alibaba)
6. [Seedance 1.5 Pro (ByteDance)](#seedance-15-pro-bytedance)
7. [LTX-2 (Lightricks)](#ltx-2-lightricks)
8. [Hailuo 2.3 (MiniMax)](#hailuo-23-minimax)
9. [Cross-Model Comparison](#cross-model-comparison)

---

## Veo 3.1 (Google)

### Five-Part Formula

Veo 3.1 responds best to prompts structured in five distinct parts:

```
[SUBJECT] + [ACTION] + [SCENE/ENVIRONMENT] + [STYLE] + [TECHNICAL]
```

### JSON Schema

```json
{
  "model": "veo-3.1",
  "prompt": {
    "subject": "A young woman with silver hair",
    "action": "walks slowly through falling cherry blossoms",
    "scene": "in a traditional Japanese garden at golden hour",
    "style": "cinematic, film grain, shallow depth of field",
    "technical": "4K, 24fps, anamorphic lens flare"
  },
  "parameters": {
    "duration": 8,
    "aspect_ratio": "16:9",
    "audio": {
      "enabled": true,
      "dialogue": "She whispers: 'I finally found it.'",
      "ambient": "gentle wind, distant temple bells"
    },
    "camera_motion": ["slow dolly forward", "subtle rack focus"]
  }
}
```

### Key Features

- **Native Audio**: Veo 3.1 generates synchronized dialogue, SFX, and ambient audio
- **Dialogue Sync**: Include spoken dialogue in quotes for lip-sync
- **Camera Arrays**: Supports multiple camera instructions as array
- **Style Persistence**: Strong style adherence across generations

### Best Practices

1. **Front-load the subject** - Veo prioritizes the first descriptor
2. **Use cinematic vocabulary** - "dolly", "crane", "rack focus" work better than generic descriptions
3. **Specify audio explicitly** - Don't leave audio to chance
4. **Keep technical specs at end** - Resolution and framerate should close the prompt

### Example Prompts

**Narrative Scene:**
```
A weathered detective in a trench coat examines a crime scene photograph
under dim lamplight in a cluttered 1940s office, noir style with harsh
shadows and venetian blind patterns, 35mm film grain, slow push-in.
Audio: rain against windows, jazz playing from a distant radio.
```

**Action Sequence:**
```
A parkour athlete vaults over concrete barriers chasing through a neon-lit
Tokyo alley at night, cyberpunk aesthetic with holographic advertisements,
handheld camera with motion blur, 60fps for smooth motion.
```

---

## Kling 2.5/2.6 (Kuaishou)

### Beats/Timing System

Kling's standout feature is precise temporal control using beats notation:

```
[0:00-0:02] Initial state
[0:02-0:05] Transition/action
[0:05-0:08] Resolution
```

### JSON Schema

```json
{
  "model": "kling-2.6",
  "prompt": {
    "beats": [
      {"time": "0:00-0:02", "description": "Close-up of eye opening"},
      {"time": "0:02-0:04", "description": "Pull back to reveal face"},
      {"time": "0:04-0:06", "description": "Continue pullback, subject stands"},
      {"time": "0:06-0:08", "description": "Wide shot, subject walks toward camera"}
    ]
  },
  "parameters": {
    "duration": 8,
    "aspect_ratio": "16:9",
    "motion_scale": 7,
    "negative_prompt": "blurry, distorted, extra limbs",
    "camera": {
      "preset": "crane",
      "direction": "up and back"
    }
  }
}
```

### Camera Presets

| Preset | Description |
|--------|-------------|
| `orbit` | 360° rotation around subject |
| `zoom` | Push in or pull out |
| `pan` | Horizontal sweep |
| `tilt` | Vertical movement |
| `crane` | Combined vertical + horizontal |
| `dolly` | Forward/backward on track |
| `handheld` | Organic shake |
| `static` | Locked-off tripod |

### Motion Scale (1-10)

- **1-3**: Subtle movement, portraits, talking heads
- **4-6**: Natural movement, walking, gestures
- **7-8**: Dynamic action, sports, dance
- **9-10**: Extreme motion, explosions, chase scenes

### Best Practices

1. **Use beats for complex sequences** - Timing markers dramatically improve coherence
2. **Set motion_scale appropriately** - Too high causes artifacts
3. **Always include negative prompts** - Kling is sensitive to quality guidance
4. **Leverage camera presets** - Native presets outperform described movements

---

## Sora 2/Pro (OpenAI)

### Shot-List Structure

Sora excels at multi-scene generation with shot-list formatting:

```json
{
  "model": "sora-2-pro",
  "scenes": [
    {
      "shot": 1,
      "duration": 3,
      "description": "Establishing shot: Manhattan skyline at dawn",
      "camera": "slow pan right",
      "audio": "city ambience, distant traffic"
    },
    {
      "shot": 2,
      "duration": 4,
      "description": "Medium shot: protagonist exits subway",
      "camera": "tracking shot following subject",
      "audio": "subway doors, footsteps"
    },
    {
      "shot": 3,
      "duration": 3,
      "description": "Close-up: determined expression",
      "camera": "static with shallow DOF",
      "audio": "heartbeat, muted city sounds"
    }
  ],
  "parameters": {
    "total_duration": 10,
    "aspect_ratio": "21:9",
    "style": "cinematic, Fincher-esque desaturated palette",
    "character_reference": "ref_image_001.png"
  }
}
```

### Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| `16:9` | Standard widescreen |
| `9:16` | Vertical/mobile |
| `1:1` | Square/social |
| `21:9` | Cinematic ultrawide |
| `4:3` | Classic/vintage |

### Best Practices

1. **Number your shots** - Sora tracks shot continuity better with explicit numbering
2. **Include transitions** - Specify cuts, dissolves, or continuous takes
3. **Reference previous shots** - "Same character as Shot 2" improves consistency
4. **Use Pro for >10s** - Standard Sora struggles with longer durations

---

## Runway Gen-4/4.5

### Timeline Array Format

Runway uses frame-accurate timeline arrays for precise control:

```json
{
  "model": "runway-gen-4.5",
  "timeline": [
    {
      "frame_range": [0, 24],
      "keyframe": {
        "subject": "woman standing still",
        "environment": "empty white studio",
        "lighting": "soft key light from left"
      }
    },
    {
      "frame_range": [24, 72],
      "keyframe": {
        "subject": "woman begins walking forward",
        "environment": "studio transforms into forest",
        "lighting": "dappled sunlight through trees"
      }
    },
    {
      "frame_range": [72, 120],
      "keyframe": {
        "subject": "woman running, hair flowing",
        "environment": "dense mystical forest",
        "lighting": "golden hour volumetric rays"
      }
    }
  ],
  "parameters": {
    "fps": 24,
    "resolution": "1080p",
    "keyframe_mode": "precise",
    "interpolation": "smooth",
    "camera_path": {
      "type": "custom",
      "points": [
        {"frame": 0, "position": [0, 0, 5], "rotation": [0, 0, 0]},
        {"frame": 60, "position": [2, 1, 3], "rotation": [10, 15, 0]},
        {"frame": 120, "position": [0, 0.5, 2], "rotation": [5, 0, 0]}
      ]
    }
  }
}
```

### Keyframe Modes

| Mode | Description |
|------|-------------|
| `precise` | Strict adherence to keyframes |
| `smooth` | Natural interpolation between states |
| `dynamic` | AI-enhanced transitions |

### Camera Path Specifications

- **position**: [x, y, z] coordinates
- **rotation**: [pitch, yaw, roll] in degrees
- **fov**: Field of view (default 50)

### Best Practices

1. **Use frame numbers, not time** - Runway thinks in frames at 24fps
2. **Define keyframes at key moments** - Don't over-specify
3. **Let interpolation do work** - Trust the model between keyframes
4. **Export camera data** - Useful for VFX compositing

---

## Wan 2.1-2.6 (Alibaba)

### MoE Architecture Awareness

Wan uses Mixture of Experts (MoE) architecture. Prompts should acknowledge this:

```json
{
  "model": "wan-2.6",
  "prompt": {
    "primary_expert": "anime",
    "content": {
      "subject": "magical girl with twin-tails",
      "action": "casting a sparkle spell",
      "environment": "floating among stars and moons",
      "style_tokens": ["mahou shoujo", "cel shaded", "dynamic pose"]
    }
  },
  "multi_shot": [
    {
      "shot": 1,
      "content": "close-up transformation sequence",
      "persist_subject": true
    },
    {
      "shot": 2,
      "content": "wide shot spell activation",
      "persist_subject": true,
      "persist_style": true
    }
  ],
  "parameters": {
    "aspect_ratio": "16:9",
    "style_strength": 0.8,
    "motion_intensity": "medium",
    "expert_weights": {
      "anime": 0.9,
      "realistic": 0.1
    }
  }
}
```

### Expert Types

| Expert | Best For |
|--------|----------|
| `anime` | Japanese animation style |
| `realistic` | Photorealistic content |
| `artistic` | Painterly, stylized |
| `motion` | Complex movement |

### Style Tokens

Wan responds well to established anime/art terminology:
- `sakuga` - High-quality animation
- `cel shaded` - Traditional anime look
- `itasha` - Detailed mechanical/vehicle
- `bishoujo`/`bishounen` - Character archetypes

### Best Practices

1. **Specify expert preference** - Don't let the model guess
2. **Use Japanese terms for anime** - Better recognition
3. **Enable persist_subject** - Critical for multi-shot
4. **Balance expert weights** - Mixing adds nuance

---

## Seedance 1.5 Pro (ByteDance)

### Four-Layer Structure

Seedance uses a layered approach optimized for dance/music content:

```json
{
  "model": "seedance-1.5-pro",
  "layers": {
    "subject": {
      "description": "professional dancer in flowing white dress",
      "body_type": "athletic feminine",
      "face_visible": true
    },
    "motion": {
      "style": "contemporary ballet",
      "intensity": "high",
      "timing_markers": [
        {"beat": 1, "pose": "arabesque"},
        {"beat": 2, "pose": "pirouette"},
        {"beat": 3, "pose": "grand jeté"},
        {"beat": 4, "pose": "landing, arms extended"}
      ]
    },
    "environment": {
      "setting": "minimalist white studio",
      "lighting": "dramatic spotlights with fog",
      "floor": "reflective black surface"
    },
    "style": {
      "aesthetic": "music video, high fashion",
      "color_grade": "high contrast, desaturated",
      "camera_style": "smooth steadicam orbit"
    }
  },
  "audio_sync": {
    "enabled": true,
    "bpm": 120,
    "beat_alignment": "on-beat",
    "reference_track": "audio_ref.mp3"
  }
}
```

### Dance Styles Supported

| Style | Keywords |
|-------|----------|
| Ballet | `arabesque`, `pirouette`, `plié`, `jeté` |
| Hip-hop | `popping`, `locking`, `breaking`, `krump` |
| Contemporary | `floor work`, `release`, `contraction` |
| K-pop | `point choreography`, `formations`, `sync` |

### Audio-Reactive Parameters

- **bpm**: Beats per minute for timing
- **beat_alignment**: `on-beat`, `off-beat`, `syncopated`
- **accent_frames**: Specific frames for hits
- **flow_type**: `staccato`, `legato`, `mixed`

### Best Practices

1. **Provide audio reference** - Even without processing, it guides generation
2. **Use dance-specific vocabulary** - Model recognizes formal terms
3. **Define timing markers** - Essential for choreography
4. **Layer information cleanly** - Each layer should be independent

---

## LTX-2 (Lightricks)

### Open Source Paragraph Format

LTX-2 uses natural language with embedded control signals:

```json
{
  "model": "ltx-2",
  "prompt": {
    "paragraph": "A serene mountain lake at sunrise. [CAMERA: slow push forward] The mist rises gently from the still water, reflecting the pink and orange sky. [MOTION: subtle ripples] A lone heron takes flight from the shore, wings catching the golden light. [AUDIO: water lapping, bird call, gentle wind] The camera continues forward, revealing a small wooden dock with an empty rowboat. [DURATION: 8 seconds]",
    "control_type": "canny",
    "control_strength": 0.7
  },
  "parameters": {
    "width": 1280,
    "height": 720,
    "fps": 24,
    "num_frames": 192,
    "guidance_scale": 7.5,
    "num_inference_steps": 50
  },
  "controlnet": {
    "type": "depth",
    "reference": "depth_map.png",
    "strength": 0.8
  }
}
```

### Control Types

| Type | Use Case |
|------|----------|
| `canny` | Edge-guided generation |
| `depth` | 3D structure preservation |
| `pose` | Human pose control |
| `none` | Pure text-to-video |

### Embedded Tags

- `[CAMERA: ...]` - Camera movement instructions
- `[MOTION: ...]` - Subject motion descriptors
- `[AUDIO: ...]` - Sound design notes (generation quality varies)
- `[DURATION: ...]` - Segment timing
- `[TRANSITION: ...]` - Cut/dissolve instructions

### ComfyUI Integration

```python
# ComfyUI workflow snippet
ltx_loader = LTXVideoLoader()
ltx_loader.model_path = "models/ltx-2.safetensors"

controlnet = LTXControlNet()
controlnet.type = "depth"
controlnet.strength = 0.8

sampler = LTXSampler()
sampler.steps = 50
sampler.cfg = 7.5
```

### Best Practices

1. **Use bracket tags inline** - Don't separate from content
2. **Leverage ControlNet** - LTX-2 excels with guidance
3. **Run locally for iteration** - OSS advantage
4. **Chain with other nodes** - Combine with upscalers, interpolators

---

## Hailuo 2.3 (MiniMax)

### Camera Control Keywords

Hailuo has extensive camera vocabulary recognition:

```json
{
  "model": "hailuo-2.3",
  "prompt": {
    "en": "A cyberpunk street vendor sells neon-lit gadgets from a hovering cart",
    "camera_keywords": [
      "crane shot descending",
      "rack focus from background to vendor",
      "slight dutch angle"
    ],
    "movement": "steady with subtle handheld shake",
    "style": "blade runner aesthetic, rain-slicked streets, neon reflections"
  },
  "parameters": {
    "mode": "standard",
    "duration": 5,
    "aspect_ratio": "16:9"
  },
  "fast_mode": {
    "enabled": false
  }
}
```

### Camera Keyword Library

**Movement:**
- `pan left/right` - Horizontal sweep
- `tilt up/down` - Vertical pivot
- `dolly in/out` - Forward/back on track
- `crane up/down` - Vertical boom
- `orbit clockwise/counter` - Circular movement
- `steadicam follow` - Smooth tracking

**Framing:**
- `extreme close-up (ECU)` - Eyes/details only
- `close-up (CU)` - Face fills frame
- `medium shot (MS)` - Waist up
- `full shot (FS)` - Entire body
- `wide shot (WS)` - Subject + environment
- `extreme wide (EWS)` - Landscape

**Techniques:**
- `rack focus` - Shift focus plane
- `pull focus` - Subject goes sharp
- `dutch angle` - Tilted horizon
- `over-the-shoulder (OTS)` - Conversational
- `point-of-view (POV)` - First person

### Fast Mode

Hailuo Fast (2.3 Fast) trades quality for speed:
- 3-4x faster generation
- Lower resolution
- Good for rapid iteration/storyboarding

### Best Practices

1. **Use precise camera terminology** - Model was trained on cinematography
2. **Combine movement types** - "dolly in while panning left"
3. **Use Fast mode for tests** - Switch to standard for finals
4. **Include both EN and style** - English prompt + style keywords

---

## Cross-Model Comparison

### Feature Matrix

| Feature | Veo 3.1 | Kling 2.6 | Sora 2 | Runway 4.5 | Wan 2.6 | Seedance | LTX-2 | Hailuo 2.3 |
|---------|---------|-----------|--------|------------|---------|----------|-------|------------|
| Native Audio | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ⚠️ | ❌ |
| JSON Schema | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Beats/Timing | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| Camera Presets | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| ControlNet | ❌ | ⚠️ | ❌ | ⚠️ | ✅ | ❌ | ✅ | ❌ |
| Open Source | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ✅ | ❌ |
| Multi-Shot | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Max Duration | 8s | 10s | 20s | 10s | 10s | 8s | Custom | 6s |

✅ = Excellent | ⚠️ = Supported | ❌ = Not available

### When to Use Each

| Use Case | Recommended Model |
|----------|-------------------|
| Cinematic with dialogue | Veo 3.1 |
| Precise timing/beats | Kling 2.6 |
| Multi-shot sequences | Sora 2 Pro |
| Frame-accurate control | Runway Gen-4.5 |
| Anime/stylized | Wan 2.6 |
| Music videos/dance | Seedance 1.5 Pro |
| OSS/local workflows | LTX-2 |
| Camera-heavy shots | Hailuo 2.3 |
| Rapid iteration | Hailuo Fast / Kling Turbo |

---

*Guide compiled January 18, 2026*
*Sources: Official documentation, community research, practical testing*

# Model Selection Decision Tree

*January 2026 Edition*

Systematic framework for selecting the optimal video AI model for any project.

---

## Table of Contents

1. [Quick Decision Flowchart](#quick-decision-flowchart)
2. [Primary Selection Criteria](#primary-selection-criteria)
3. [Use Case Decision Trees](#use-case-decision-trees)
4. [Feature Comparison Matrix](#feature-comparison-matrix)
5. [Quality Tiers by Budget](#quality-tiers-by-budget)
6. [Technical Requirements](#technical-requirements)
7. [Workflow Integration Guide](#workflow-integration-guide)
8. [Model Profiles](#model-profiles)

---

## Quick Decision Flowchart

```
START: What's your primary need?
│
├─► COMMERCIAL PROJECT
│   └─► Is budget critical?
│       ├─► YES → Wan 2.6 (OSS) or Kling Standard
│       └─► NO → What's the content type?
│           ├─► Talking Head → Veo 3.1* or HeyGen
│           ├─► Cinematic → Runway Gen-4.5 or Veo 3.1*
│           ├─► Music Video → Seedance 1.5 Pro
│           ├─► Product → Runway Gen-4.5
│           └─► Social/Fast → Kling 2.6 or Pika
│
├─► PERSONAL/PROTOTYPE
│   └─► Do you have a GPU?
│       ├─► YES (24GB+) → Wan 2.6 14B or HunyuanVideo
│       ├─► YES (12-16GB) → LTX-2 or Wan 1.3B
│       └─► NO → Use cloud (Pika free, Luma free, Krea)
│
├─► ANIME/STYLIZED
│   └─► Wan 2.6 with --expert anime
│
├─► MAXIMUM QUALITY (COST NO OBJECT)
│   └─► Veo 3.1* → Runway Gen-4.5 → Upscale
│
└─► OPEN SOURCE REQUIRED
    └─► Wan 2.6 (Apache 2.0) > LTX-2 > HunyuanVideo*

* Veo 3.1: Verify GA status for commercial use
* HunyuanVideo: Excludes EU/UK/South Korea
```

---

## Primary Selection Criteria

### Decision Factor Weights

| Factor | Weight | Description |
|--------|--------|-------------|
| Legal/Commercial Rights | Critical | Can you legally use the output? |
| Quality Requirements | High | Does output meet your standards? |
| Budget Constraints | High | Can you afford it at scale? |
| Turnaround Speed | Medium | How fast do you need results? |
| Control Features | Medium | Do you need precise control? |
| Audio Requirements | Medium | Native audio or post-sync? |
| Integration Needs | Low-Medium | API, ComfyUI, standalone? |

### The First Question: Commercial vs. Personal

```
COMMERCIAL USE?
│
├─► YES
│   ├─► CHECK: Platform commercial rights (see Legal Primer)
│   ├─► AVOID: Veo 3.1 (Pre-GA), free tiers, unclear ToS
│   └─► PREFER: Wan (Apache 2.0), Runway Enterprise, Luma Plus+
│
└─► NO (Personal/Prototype)
    ├─► All platforms available
    ├─► Focus on quality and features
    └─► Free tiers acceptable
```

---

## Use Case Decision Trees

### Tree 1: Talking Head / Avatar Content

```
TALKING HEAD CONTENT
│
├─► Native Lip Sync Required?
│   ├─► YES
│   │   ├─► Quality: Premium → HeyGen or Synthesia
│   │   ├─► Quality: Good → Hedra Character-3
│   │   └─► Quality: Acceptable → Pika Lip Sync
│   │
│   └─► NO (Post-sync acceptable)
│       ├─► Generate video → Add lip sync in post
│       └─► Model: Any quality video model + MuseTalk
│
├─► Multi-Language Dubbing?
│   ├─► YES → HeyGen (175+ languages)
│   └─► NO → Any lip sync tool
│
├─► Real Person Likeness?
│   ├─► YES
│   │   ├─► CONSENT REQUIRED
│   │   └─► Use: HeyGen, Synthesia (compliance frameworks)
│   └─► NO (Custom Avatar)
│       └─► Use: Hedra (custom avatar creation)
│
└─► Budget?
    ├─► Enterprise → Synthesia ($1000+/mo)
    ├─► Professional → HeyGen ($48+/mo)
    ├─► Budget → Hedra ($0.05/min) or MuseTalk (free)
    └─► Prototype → D-ID free tier, Pika
```

### Tree 2: Cinematic / Narrative Content

```
CINEMATIC CONTENT
│
├─► Audio Integration?
│   ├─► Native dialogue + SFX + music
│   │   └─► Veo 3.1* (best native audio)
│   │
│   ├─► Music sync (dance/MV)
│   │   └─► Seedance 1.5 Pro
│   │
│   └─► Post-production audio
│       └─► Any quality model
│
├─► Character Consistency Critical?
│   ├─► YES
│   │   ├─► Use reference system: Vidu (7-image)
│   │   ├─► Use face lock: Kling 2.6 Pro
│   │   └─► Use IP-Adapter: ComfyUI + Wan/LTX-2
│   │
│   └─► NO (Standalone shots)
│       └─► Any model based on quality needs
│
├─► Camera Control Precision?
│   ├─► Frame-accurate required
│   │   └─► Runway Gen-4.5 (timeline arrays)
│   │
│   ├─► Good camera vocabulary
│   │   └─► Hailuo 02 or Kling 2.6
│   │
│   └─► Basic control sufficient
│       └─► Any model
│
└─► Quality Tier?
    ├─► Broadcast/Film → Veo 3.1* or Runway Gen-4.5
    ├─► Professional → Kling 2.6 Pro or Sora 2 Pro
    ├─► Good → Pika, Luma, Hailuo
    └─► Acceptable → Wan 2.6, LTX-2
```

### Tree 3: Product / Commercial Content

```
PRODUCT / COMMERCIAL
│
├─► Product Type?
│   ├─► Physical Product (hero shots)
│   │   ├─► Premium: Runway Gen-4.5
│   │   └─► Good: Kling 2.6 Pro
│   │
│   ├─► Software/App (UI demos)
│   │   ├─► Screen recording + AI enhancement
│   │   └─► Consider: Synthesia for presenter
│   │
│   └─► Lifestyle (product in use)
│       ├─► Premium: Veo 3.1* (natural scenarios)
│       └─► Good: Kling 2.6 or Pika
│
├─► Brand Guidelines Strict?
│   ├─► YES
│   │   ├─► Use ControlNet for precise framing
│   │   └─► Multiple iterations expected
│   │
│   └─► NO
│       └─► Standard workflow
│
├─► Localization Required?
│   ├─► YES (multiple languages)
│   │   └─► HeyGen for presenter content
│   │
│   └─► NO
│       └─► Standard workflow
│
└─► Volume?
    ├─► High (100+ videos/month)
    │   ├─► API integration: fal.ai, Replicate
    │   └─► Consider self-hosting Wan/LTX-2
    │
    └─► Low-Medium
        └─► Native platforms sufficient
```

### Tree 4: Social Media / Short-Form

```
SOCIAL CONTENT
│
├─► Platform Target?
│   ├─► TikTok/Reels (vertical 9:16)
│   │   ├─► Fast turnaround: Pika or Kling
│   │   └─► Quality: Any with aspect ratio support
│   │
│   ├─► YouTube (horizontal 16:9)
│   │   ├─► Longer form: Veo 3.1*, Runway
│   │   └─► Shorts: Same as TikTok
│   │
│   └─► Twitter/X (flexible)
│       └─► Any model, compress for platform
│
├─► Trend-Reactive (fast turnaround)?
│   ├─► YES
│   │   ├─► Fastest: Pika (~30s generation)
│   │   └─► Good: Kling standard tier
│   │
│   └─► NO (planned content)
│       └─► Optimize for quality over speed
│
├─► Character Swap / Meme Content?
│   ├─► YES
│   │   ├─► Kling (video-to-video strength)
│   │   └─► ComfyUI + IP-Adapter pipeline
│   │
│   └─► NO
│       └─► Standard model selection
│
└─► Budget per Video?
    ├─► <$0.50 → Wan (free), LTX-2 (free), Free tiers
    ├─► $0.50-2 → Kling, Pika, Hailuo
    └─► $2+ → Any model
```

### Tree 5: Anime / Stylized Content

```
ANIME / STYLIZED
│
├─► Style Type?
│   ├─► Anime (Japanese animation style)
│   │   └─► Wan 2.6 with --expert anime (BEST)
│   │       └─► Alternatives: Pika (anime mode), Kling
│   │
│   ├─► Cartoon (Western animation)
│   │   ├─► Wan 2.6 with style prompting
│   │   └─► Runway with style reference
│   │
│   ├─► Painterly / Artistic
│   │   ├─► Wan 2.6 (strong stylization)
│   │   └─► Genmo Mochi 1 (artistic outputs)
│   │
│   └─► Mixed / Hybrid
│       └─► Wan 2.6 with --expert anime,realistic
│
├─► Consistency Requirements?
│   ├─► Multi-episode series
│   │   └─► LoRA training recommended
│   │       └─► Platform: ComfyUI + Wan/LTX-2
│   │
│   └─► Standalone / Short
│       └─► IP-Adapter sufficient
│
├─► Action Intensity?
│   ├─► High (fight scenes, fast movement)
│   │   ├─► Wan 2.6 (handles motion well)
│   │   └─► Kling 2.6 (good action)
│   │
│   └─► Low-Medium
│       └─► Any anime-capable model
│
└─► Budget/Platform?
    ├─► Open source required → Wan 2.6 (Apache 2.0)
    ├─► Cloud preferred → Pika, Kling
    └─► Local preferred → Wan 2.6 via ComfyUI
```

### Tree 6: Open Source / Self-Hosted

```
OPEN SOURCE REQUIREMENT
│
├─► License Requirements?
│   ├─► Fully permissive (Apache 2.0)
│   │   └─► Wan 2.6 (ONLY OPTION)
│   │
│   ├─► Commercial OK with restrictions
│   │   └─► LTX-2, CogVideoX
│   │
│   └─► Non-commercial / Research
│       └─► HunyuanVideo, various research models
│
├─► Territory Restrictions?
│   ├─► EU/UK/South Korea
│   │   └─► AVOID: HunyuanVideo
│   │   └─► USE: Wan 2.6, LTX-2
│   │
│   └─► No restrictions
│       └─► All OSS models available
│
├─► Hardware Available?
│   ├─► 48GB+ VRAM
│   │   └─► All models, full quality
│   │   └─► Wan 14B, HunyuanVideo 8.3B
│   │
│   ├─► 24GB VRAM
│   │   └─► Most models with FP8 quantization
│   │   └─► Wan 14B (FP8), LTX-2, HunyuanVideo-1.5
│   │
│   ├─► 12-16GB VRAM
│   │   └─► Smaller models only
│   │   └─► Wan 1.3B, LTX-2 (optimized)
│   │
│   └─► 8GB VRAM or CPU
│       └─► Very limited options
│       └─► Wan 1.3B (reduced quality)
│
└─► ComfyUI Integration?
    ├─► Required
    │   └─► Wan (Kijai nodes), LTX-2 (Day 0), HunyuanVideo
    │
    └─► Not required
        └─► Any OSS with Python API
```

---

## Feature Comparison Matrix

### Core Capabilities

| Model | Max Duration | Max Resolution | Native Audio | Commercial |
|-------|-------------|----------------|--------------|------------|
| Veo 3.1 | 8s | 1080p | ✓ Excellent | ❌ Pre-GA |
| Sora 2 Pro | 20s | 1080p | Partial | ✓ |
| Runway Gen-4.5 | 10s | 4K | ❌ | ✓ |
| Kling 2.6 Pro | 10s | 1080p | ❌ | ✓ |
| Pika | 5s | 1080p | ❌ | ✓ Pro+ |
| Luma | 5s | 1080p | ❌ | ✓ Plus+ |
| Seedance 1.5 | 10s | 1080p | ✓ Music | ✓ |
| LTX-2 | 5s | 720p | ✓ | ✓ Std+ |
| Wan 2.6 | 5s | 720p | ❌ | ✓ Apache |
| Hailuo 02 | 6s | 1080p | ❌ | ✓ |
| HunyuanVideo | 5s | 720p | ❌ | Limited* |

### Control Features

| Model | I2V | V2V | ControlNet | Camera Control | Character Ref |
|-------|-----|-----|------------|----------------|---------------|
| Veo 3.1 | ✓ | ✓ | Limited | Good | ✓ Subject Ref |
| Sora 2 Pro | ✓ | ✓ | ❌ | Excellent | ❌ |
| Runway Gen-4.5 | ✓ | ✓ | ✓ | Excellent | ✓ Motion Ref |
| Kling 2.6 | ✓ | ✓ | ❌ | Good | ✓ Face Lock |
| Pika | ✓ | ✓ | ❌ | Basic | ❌ |
| Luma | ✓ | ❌ | ❌ | Basic | ✓ Persistence |
| Seedance 1.5 | ✓ | ❌ | ❌ | Basic | ❌ |
| LTX-2 | ✓ | ✓ | ✓ Full | Good | ❌ |
| Wan 2.6 | ✓ | ✓ | ✓ Full | Basic | Via IP-Adapter |
| Hailuo 02 | ✓ | ✓ | ❌ | Excellent | ❌ |

### Quality Ratings (Subjective, Jan 2026)

| Model | Realism | Motion | Consistency | Hands/Faces |
|-------|---------|--------|-------------|-------------|
| Veo 3.1 | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| Sora 2 Pro | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Runway Gen-4.5 | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Kling 2.6 | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Pika | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ |
| Luma | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| Seedance 1.5 | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| LTX-2 | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |
| Wan 2.6 | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| Hailuo 02 | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |

---

## Quality Tiers by Budget

### Tier 1: Maximum Quality ($1-3 per 5s video)

```
Primary Choice: Veo 3.1* or Runway Gen-4.5

Workflow:
1. Generate with premium model
2. Upscale with Topaz or similar
3. Color grade in DaVinci
4. Professional audio in post

Best For:
- Broadcast/Film
- High-end commercials
- Premium brand content
- Trailer/teaser production

*Veo 3.1: Verify GA status before commercial use
```

### Tier 2: Professional ($0.30-1 per 5s video)

```
Primary Choices: Kling 2.6 Pro, Sora 2 Pro, Hailuo 02

Workflow:
1. Generate with mid-tier model
2. Light upscaling if needed
3. Standard post-production

Best For:
- Corporate video
- Marketing content
- YouTube production
- Social campaigns
```

### Tier 3: Budget ($0.05-0.30 per 5s video)

```
Primary Choices: Kling Standard, Pika, fal.ai APIs

Workflow:
1. Generate with budget model
2. Minimal post-production
3. Volume over perfection

Best For:
- Social media content
- Rapid prototyping
- High-volume production
- Testing concepts
```

### Tier 4: Free/Minimal Cost (<$0.05 per 5s video)

```
Primary Choices: Wan 2.6 (local), LTX-2 (local), Free tiers

Workflow:
1. Self-host or use free tiers
2. Batch process
3. Accept quality limitations

Best For:
- Personal projects
- Learning/experimentation
- Proof of concept
- Open source requirements
```

---

## Technical Requirements

### VRAM Requirements

| Model | Minimum | Recommended | Optimal |
|-------|---------|-------------|---------|
| Wan 2.6 14B | 16GB (FP8) | 24GB | 48GB |
| Wan 2.6 1.3B | 8GB | 12GB | 16GB |
| LTX-2 | 8GB | 16GB | 24GB |
| HunyuanVideo | 16GB (FP8) | 24GB | 48GB |
| CogVideoX | 12GB | 16GB | 24GB |

### API Rate Limits (Typical)

| Platform | Free Tier | Paid Tier | Enterprise |
|----------|-----------|-----------|------------|
| Kling | 66/day | Unlimited | Custom |
| Pika | 100/day | Unlimited | Custom |
| Luma | 30/day | Unlimited | Custom |
| Runway | 125 credits | Varies | Custom |
| fal.ai | Pay-per-use | Pay-per-use | Volume discounts |

### Generation Speed

| Model | Typical Time (5s video) | Fast Mode |
|-------|------------------------|-----------|
| Pika | 30-60s | ~20s |
| Kling | 2-3 min | ~1 min |
| Runway | 3-5 min | ~2 min |
| Veo 3.1 | 2-4 min | N/A |
| Wan (local) | 3-5 min | N/A |
| LTX-2 (local) | 1-2 min | N/A |

---

## Workflow Integration Guide

### ComfyUI Integration

```
Native Support (Day 0):
✓ LTX-2 — Full support, audio-video
✓ Wan 2.6 — Via Kijai nodes (WanVideoWrapper)
✓ HunyuanVideo — Via Kijai nodes

Good Support:
✓ CogVideoX — Community nodes
✓ AnimateDiff — Established ecosystem

API Integration:
✓ Kling — Via fal.ai nodes
✓ Runway — Via API nodes
✓ Replicate models — Via Replicate nodes
```

### API-First Workflows

```
Best API Platforms:

fal.ai:
- Kling 2.6, Wan 2.6, LTX-2, Hailuo
- Simple SDK, good documentation
- Pay-per-use pricing

Replicate:
- Wan 2.6, LTX-2, various OSS
- Model versioning
- Per-second billing

Native APIs:
- Runway API
- Luma API
- HeyGen API
- OpenAI API (Sora)
```

### Batch Processing Setup

```python
# Example: Multi-model batch with fallback
class VideoGenerationPipeline:
    def __init__(self):
        self.models = {
            "premium": VeoClient(),      # Quality priority
            "standard": KlingClient(),   # Balance
            "fallback": WanClient(),     # Cost priority
        }

    def generate(self, prompt, budget="standard", retries=3):
        model = self.models[budget]

        for attempt in range(retries):
            try:
                return model.generate(prompt)
            except RateLimitError:
                # Fallback to cheaper model
                model = self.models["fallback"]
            except QualityError:
                # Retry with same model
                continue

        raise GenerationError("All attempts failed")
```

---

## Model Profiles

### Veo 3.1 (Google)

```
BEST FOR: Cinematic content with native audio
AVOID FOR: Commercial use (until GA)

Strengths:
+ Best-in-class audio generation (~10ms latency)
+ Excellent realism
+ Good prompt following
+ Person-in-context grounding

Weaknesses:
- Pre-GA (no commercial use)
- Limited availability
- Higher cost
- Less camera control than Runway

Typical Workflow:
Prompt → Veo 3.1 → Minor post-production → Delivery
```

### Runway Gen-4.5

```
BEST FOR: Professional production, precise control
COMMERCIAL: ✓ Full rights on all tiers

Strengths:
+ Best motion quality
+ Excellent camera control (timeline arrays)
+ Motion/style reference system
+ Enterprise-ready (SOC 2)

Weaknesses:
- No native audio
- Higher cost
- Occasional consistency issues

Typical Workflow:
Reference → Runway Gen-4.5 → Post audio → Color → Delivery
```

### Kling 2.6

```
BEST FOR: Balanced quality/cost, face lock features
COMMERCIAL: ✓ Paid tiers

Strengths:
+ Good quality/price ratio
+ Face lock feature (Pro)
+ Fast generation
+ Good action/motion

Weaknesses:
- Data residency (China servers)
- Inconsistent hands/faces
- Limited control features

Typical Workflow:
Prompt → Kling → Review/regenerate → Post-production → Delivery
```

### Wan 2.6

```
BEST FOR: Anime, open source requirements, cost-sensitive
COMMERCIAL: ✓ Apache 2.0 (unrestricted)

Strengths:
+ Best anime/stylized results
+ Fully open source
+ MoE architecture (expert routing)
+ ComfyUI ecosystem
+ Zero licensing concerns

Weaknesses:
- Requires self-hosting for best results
- 720p max resolution
- No native audio
- Hardware requirements (14B model)

Typical Workflow:
ComfyUI → Wan 2.6 + IP-Adapter → Upscale → Post-production
```

### LTX-2

```
BEST FOR: Open source with audio, ComfyUI workflows
COMMERCIAL: ✓ Standard tier+

Strengths:
+ Open source with audio-video
+ Day 0 ComfyUI support
+ Full ControlNet support
+ 19B parameters

Weaknesses:
- 720p resolution
- Newer/less tested
- Requires hardware

Typical Workflow:
ComfyUI → LTX-2 (with ControlNet) → Post-production
```

### Seedance 1.5 Pro

```
BEST FOR: Music videos, dance content, beat-sync
COMMERCIAL: ✓ Check current terms

Strengths:
+ Best music synchronization
+ Audio-reactive generation
+ Dance choreography understanding
+ Energy curve mapping

Weaknesses:
- Limited non-dance use cases
- Less precise camera control
- ByteDance platform

Typical Workflow:
Audio track → Seedance → Cut to beat → Delivery
```

---

## Quick Reference Card

### By Primary Need

| Need | First Choice | Backup | Budget Option |
|------|-------------|--------|---------------|
| Cinematic | Veo 3.1* | Runway | Kling Pro |
| Talking Head | HeyGen | Hedra | MuseTalk |
| Product | Runway | Kling Pro | Pika |
| Social/Fast | Pika | Kling Std | Free tiers |
| Anime | Wan 2.6 | Pika | Wan 1.3B |
| Music Video | Seedance | Kling | Manual sync |
| Open Source | Wan 2.6 | LTX-2 | HunyuanVideo* |

*Restrictions apply — see full profiles

### By Budget (per 5s video)

| Budget | Best Quality | Best Value |
|--------|-------------|------------|
| $2+ | Veo 3.1, Runway | Sora 2 Pro |
| $0.50-2 | Kling Pro | Hailuo |
| $0.10-0.50 | Kling Std | fal.ai Wan |
| <$0.10 | Local Wan | Free tiers |

---

*Model Selection Decision Tree v1.0 — January 18, 2026*
*Recommendations based on publicly available information and typical use cases*

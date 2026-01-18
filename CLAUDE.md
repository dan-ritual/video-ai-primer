# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Video AI Primer** — a comprehensive knowledge base for AI video generation (January 2026 Edition). It contains 18 markdown documents (~400KB total) covering video AI models, prompting techniques, production workflows, and automation scripts.

**Primary audience**: Expert-level video editors working with AI video generation tools.

## Document Structure

```
00_INDEX.md                         # Navigation & reading paths
01_VIDEO_AI_COMPREHENSIVE_GUIDE.md  # Foundation: all major models
02_MODEL_SELECTION_DECISION_TREE.md # Decision framework by use case
03_JSON_PROMPTING_GUIDE.md          # Structured prompt engineering
04_PROMPT_TEMPLATE_LIBRARY.md       # Copy-paste prompt templates
05_PLATFORM_HARNESS_GUIDE.md        # API & platform deep dives (fal.ai, Replicate)
06_COMFYUI_NODE_WORKFLOWS_GUIDE.md  # Node-based automation
07_IMAGE_MODELS_STATE_OF_UNION.md   # Start frame generation (Niji 7, FLUX, Nano Banana)
08_START_STOP_FRAME_DEEP_DIVE.md    # First-Last Frame (FLF) workflows
09_CHARACTER_CONSISTENCY_GUIDE.md   # Multi-shot coherence techniques
10_AUDIO_VIDEO_SYNC_GUIDE.md        # Sound integration & lip sync
11_WORKFLOW_RECIPES_COOKBOOK.md     # 18 production recipes
12_COST_OPTIMIZATION_GUIDE.md       # Budget & efficiency
13_CLAUDE_CODE_VIDEO_TOOLKIT.md     # Python automation scripts
14_AGENT_QUALITY_EVALS_FRAMEWORK.md # Automated quality assessment
16_VIDEO_AI_INFLUENCERS_GUIDE.md    # Who to follow
17_FUTURE_PROOFING_ROADMAP.md       # 2026-2027 predictions
18_RESEARCH_LOG.md                  # Source documentation
99_AGENTS.md                        # Agent retrieval optimization guide
```

## Query Routing

When answering questions from this knowledge base:

| Query Intent | Primary Document |
|-------------|------------------|
| "Which model for X?" | `02_MODEL_SELECTION_DECISION_TREE.md` |
| "How do I prompt for X?" | `03_JSON_PROMPTING_GUIDE.md` |
| "Give me a template" | `04_PROMPT_TEMPLATE_LIBRARY.md` |
| "How does platform X work?" | `05_PLATFORM_HARNESS_GUIDE.md` |
| "ComfyUI workflow" | `06_COMFYUI_NODE_WORKFLOWS_GUIDE.md` |
| "Best image model for start frames" | `07_IMAGE_MODELS_STATE_OF_UNION.md` |
| "First-last frame / FLF / I2V" | `08_START_STOP_FRAME_DEEP_DIVE.md` |
| "Character consistency" | `09_CHARACTER_CONSISTENCY_GUIDE.md` |
| "Audio / lip sync" | `10_AUDIO_VIDEO_SYNC_GUIDE.md` |
| "Step-by-step recipe" | `11_WORKFLOW_RECIPES_COOKBOOK.md` |
| "Cost / pricing" | `12_COST_OPTIMIZATION_GUIDE.md` |
| "Python script / automation" | `13_CLAUDE_CODE_VIDEO_TOOLKIT.md` |
| "Quality evaluation" | `14_AGENT_QUALITY_EVALS_FRAMEWORK.md` |

## Key Models Covered

**Commercial Video Models**: Veo 3.1 (Google), Kling 2.6 (ByteDance), Sora 2 Pro (OpenAI), Runway Gen-4.5, Seedance 1.5 Pro, Hailuo 2.3

**Open Source Video Models**: Wan 2.1-2.6 (Alibaba), LTX-2 (Lightricks), HunyuanVideo

**Image Models for Start Frames**: Midjourney Niji 7, FLUX.2, Nano Banana Pro, Ideogram 3.0

## Code Assets

`13_CLAUDE_CODE_VIDEO_TOOLKIT.md` contains production-ready Python scripts for:
- Multi-model video generation (`generate.py`)
- Batch processing pipelines (`batch.py`)
- Quality assessment automation (`quality.py`)
- ComfyUI API client
- fal.ai and Replicate integrations

**Dependencies**: Python 3.10+, fal-client, replicate, httpx, opencv-python, rich

## Workflow Types

- **T2V**: Text-to-video (all models)
- **I2V**: Image-to-video (single start frame)
- **FLF2V**: First-Last Frame to video (Wan 2.1+, Kling O1)
- **Character Swap**: Replace character preserving motion

## Freshness Note

This corpus reflects **January 2026** knowledge. Video AI evolves rapidly — supplement with web search for:
- New model releases
- Pricing changes
- Platform updates

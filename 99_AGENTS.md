# AGENTS.md — Agent-Optimized Retrieval Guide

**Specification for LLM Agents Consuming This Knowledge Base**

---

## Purpose

This document optimizes the Video AI Primer for consumption by:
- **Claude Code** (Anthropic)
- **OpenCode** / Open Interpreter
- **Amp** (Sourcegraph)
- **Codex** (OpenAI)
- **Cursor** / Windsurf / Other AI-assisted IDEs
- **Custom agents** built on Claude, GPT-4, or other foundation models

The goal is maximum retrieval accuracy and response quality when agents query this knowledge base.

---

## Quick Reference Card

```
CORPUS METADATA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Domain:          AI Video Generation
Temporal Scope:  January 2026 (current)
Total Files:     20 markdown documents
Total Size:      ~420 KB
Primary Topics:  Video AI models, prompting, workflows,
                 platforms, image-to-video, production
Target User:     Expert-level video editor

FRESHNESS WARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This corpus reflects January 2026 knowledge.
Video AI evolves rapidly. For queries about:
- New model releases after Jan 2026
- Pricing changes
- Platform updates
Recommend supplementing with web search.
```

---

## Document Map

### File → Topic Routing

Use this routing table to select the optimal document for a given query:

```yaml
Query Intent Routing:
  "Which model should I use for X?":
    primary: 02_MODEL_SELECTION_DECISION_TREE.md
    secondary: 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md

  "How do I prompt for X?":
    primary: 03_JSON_PROMPTING_GUIDE.md
    secondary: 04_PROMPT_TEMPLATE_LIBRARY.md

  "Give me a template/example for X":
    primary: 04_PROMPT_TEMPLATE_LIBRARY.md
    secondary: 11_WORKFLOW_RECIPES_COOKBOOK.md

  "How does platform X work?":
    primary: 05_PLATFORM_HARNESS_GUIDE.md
    secondary: 12_COST_OPTIMIZATION_GUIDE.md

  "ComfyUI workflow for X":
    primary: 06_COMFYUI_NODE_WORKFLOWS_GUIDE.md
    secondary: 13_CLAUDE_CODE_VIDEO_TOOLKIT.md

  "Best image model for start frames":
    primary: 07_IMAGE_MODELS_STATE_OF_UNION.md
    secondary: 08_START_STOP_FRAME_DEEP_DIVE.md

  "First-last frame / FLF / I2V workflow":
    primary: 08_START_STOP_FRAME_DEEP_DIVE.md
    secondary: 07_IMAGE_MODELS_STATE_OF_UNION.md

  "Anime workflow / Niji 7":
    primary: 08_START_STOP_FRAME_DEEP_DIVE.md
    secondary: 07_IMAGE_MODELS_STATE_OF_UNION.md

  "Character consistency / multi-shot":
    primary: 09_CHARACTER_CONSISTENCY_GUIDE.md
    secondary: 08_START_STOP_FRAME_DEEP_DIVE.md

  "Audio / sound / lip sync / music":
    primary: 10_AUDIO_VIDEO_SYNC_GUIDE.md

  "Step-by-step production recipe":
    primary: 11_WORKFLOW_RECIPES_COOKBOOK.md
    secondary: 08_START_STOP_FRAME_DEEP_DIVE.md

  "Cost / pricing / budget":
    primary: 12_COST_OPTIMIZATION_GUIDE.md
    secondary: 05_PLATFORM_HARNESS_GUIDE.md

  "Python script / automation / API":
    primary: 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
    secondary: 05_PLATFORM_HARNESS_GUIDE.md

  "Quality metrics / evaluation":
    primary: 14_AGENT_QUALITY_EVALS_FRAMEWORK.md

  "Who to follow / community":
    primary: 16_VIDEO_AI_INFLUENCERS_GUIDE.md

  "Future / predictions / roadmap":
    primary: 17_FUTURE_PROOFING_ROADMAP.md

  "Overview / getting started":
    primary: 00_INDEX.md
    secondary: 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md
```

---

## Semantic Chunks

### High-Value Retrieval Targets

When searching this corpus, these are the highest-information-density sections:

#### 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md
```
Chunks:
- "Model Landscape Overview" → Current state of all major models
- "Veo 3.1" section → Google's flagship capabilities
- "Kling 2.6" section → ByteDance's motion strengths
- "Open Source Options" → Wan, LTX-2, HunyuanVideo
- "Capability Matrix" → Model comparison tables
```

#### 02_MODEL_SELECTION_DECISION_TREE.md
```
Chunks:
- Decision trees (multiple) → If/then model selection
- "By Content Type" → Realistic vs anime vs abstract
- "By Use Case" → Social media vs commercial vs film
- "By Budget" → Free/cheap/premium tiers
```

#### 03_JSON_PROMPTING_GUIDE.md
```
Chunks:
- JSON schema templates → Structured prompt format
- "Model-Specific Syntax" → Per-model adjustments
- "Negative Prompts" → What to avoid
- "Camera Movement Vocabulary" → Shot types
```

#### 07_IMAGE_MODELS_STATE_OF_UNION.md
```
Chunks:
- "Nano Banana Pro" → Gemini 3 Pro Image details
- "Midjourney Niji 7" → Anime-optimized model
- "FLUX.2" → Open source champion
- Comparison tables → Head-to-head analysis
```

#### 08_START_STOP_FRAME_DEEP_DIVE.md
```
Chunks:
- "FLF2V Pipeline" → First-last frame workflow
- "Niji 7 for Anime" → Anime start frame generation
- "Wan 2.1/2.2" → FLF video generation
- "Production Recipes" → Step-by-step workflows
- "Character Consistency in FLF" → Multi-shot coherence
```

#### 11_WORKFLOW_RECIPES_COOKBOOK.md
```
Chunks:
- Each numbered recipe → Complete production workflows
- "Social Media" recipes → Short-form content
- "Product Video" recipes → E-commerce content
- "Music Video" recipes → Audio-synced content
```

#### 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
```
Chunks:
- Python code blocks → Copy-paste ready scripts
- "fal.ai Integration" → API wrapper code
- "Batch Processing" → Multi-video pipelines
- "Quality Checking" → Automated validation
```

---

## Retrieval Instructions

### For Claude Code / Anthropic Agents

```markdown
RETRIEVAL PROTOCOL

1. Query Classification
   - Identify query intent from routing table above
   - Determine primary and secondary documents

2. Document Loading
   - Read primary document FIRST
   - If insufficient, read secondary document
   - For complex queries, may need 2-3 documents

3. Response Construction
   - Cite specific sections when referencing
   - Include code blocks verbatim when applicable
   - Note document freshness (January 2026)

4. Confidence Calibration
   - High confidence: Direct matches to documented content
   - Medium confidence: Inferences from documented patterns
   - Low confidence: Extrapolations or predictions
   - Flag when query exceeds corpus scope
```

### For Codex / OpenAI Agents

```markdown
CODEX-OPTIMIZED INSTRUCTIONS

This corpus contains production-ready code in:
- Python (primary)
- Bash (secondary)
- JSON schemas (prompting)

When asked for code:
1. Check 13_CLAUDE_CODE_VIDEO_TOOLKIT.md first
2. Check 04_PROMPT_TEMPLATE_LIBRARY.md for JSON
3. Check 05_PLATFORM_HARNESS_GUIDE.md for API patterns

Code is designed for:
- Python 3.10+
- async/await patterns
- fal.ai, Replicate, Runway SDKs
```

### For Cursor / IDE Agents

```markdown
IDE AGENT INSTRUCTIONS

Context awareness:
- User is likely a video editor with Python familiarity
- Workflows target production use, not research
- Prefer practical over theoretical responses

When assisting with:
- Video generation scripts → 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
- ComfyUI workflows → 06_COMFYUI_NODE_WORKFLOWS_GUIDE.md
- Prompt engineering → 03_JSON_PROMPTING_GUIDE.md
- API integration → 05_PLATFORM_HARNESS_GUIDE.md
```

---

## Entity Definitions

### Model Entities

```yaml
Models:
  Veo_3.1:
    vendor: Google
    type: Text-to-Video, Image-to-Video
    audio: Native generation
    max_duration: 8 seconds
    quality_tier: Premium
    access: API (Google AI Studio)

  Kling_2.6:
    vendor: ByteDance/Kuaishou
    type: Text-to-Video, Image-to-Video
    audio: Native (Seedance)
    max_duration: 10 seconds
    quality_tier: Premium
    access: API, Web UI

  Sora_2_Pro:
    vendor: OpenAI
    type: Text-to-Video
    audio: Via integration
    max_duration: 20 seconds
    quality_tier: Premium
    access: ChatGPT Pro, API

  Runway_Gen-4.5:
    vendor: Runway
    type: Text-to-Video, Image-to-Video
    audio: Coming soon
    max_duration: 10 seconds
    quality_tier: Premium
    access: Web UI, API

  Wan_2.6:
    vendor: Alibaba
    type: Text-to-Video, Image-to-Video, FLF
    audio: No
    max_duration: Variable
    quality_tier: Open Source Premium
    access: Self-hosted, fal.ai

  LTX_2:
    vendor: Lightricks
    type: Text-to-Video
    audio: Yes
    max_duration: Variable
    quality_tier: Open Source
    access: Self-hosted, fal.ai

  Niji_7:
    vendor: Midjourney
    type: Image Generation (anime)
    purpose: Start frames for I2V
    access: Discord, Web UI

  Nano_Banana_Pro:
    vendor: Google (fal.ai hosted)
    type: Image Generation
    purpose: Start frames for I2V
    access: fal.ai API
```

### Platform Entities

```yaml
Platforms:
  fal.ai:
    type: Model hosting, API gateway
    models: Wan, LTX, FLUX, Nano Banana
    pricing: Pay-per-generation

  Replicate:
    type: Model hosting, API gateway
    models: Various open source
    pricing: Pay-per-second

  RunPod:
    type: GPU rental
    use_case: Self-hosting models
    pricing: Hourly GPU rental

  ComfyUI:
    type: Node-based workflow tool
    use_case: Complex generation pipelines
    access: Self-hosted (free)
```

### Workflow Entities

```yaml
Workflows:
  FLF2V:
    name: First-Last Frame to Video
    description: Generate video from start and end frame images
    models: Wan 2.1, Wan 2.2
    complexity: Intermediate

  I2V:
    name: Image to Video
    description: Animate a single image
    models: All major models
    complexity: Basic

  T2V:
    name: Text to Video
    description: Generate video from text prompt only
    models: All major models
    complexity: Basic

  Character_Swap:
    name: Character/Motion Transfer
    description: Replace character while preserving motion
    models: Kling (primary), Wan 2.2
    complexity: Intermediate
```

---

## Query Patterns

### Common Query Templates

Agents should recognize these query patterns and route accordingly:

```
PATTERN: Model Comparison
Examples:
- "Veo vs Kling for X"
- "Should I use Runway or Sora"
- "Best model for anime"
Route to: 02_MODEL_SELECTION_DECISION_TREE.md

PATTERN: How-To / Tutorial
Examples:
- "How do I generate X"
- "Steps to create X"
- "Workflow for X"
Route to: 11_WORKFLOW_RECIPES_COOKBOOK.md

PATTERN: Prompt Request
Examples:
- "Write a prompt for X"
- "JSON prompt for X"
- "Negative prompts for X"
Route to: 03_JSON_PROMPTING_GUIDE.md, 04_PROMPT_TEMPLATE_LIBRARY.md

PATTERN: Code Request
Examples:
- "Python script for X"
- "API code for X"
- "Automate X"
Route to: 13_CLAUDE_CODE_VIDEO_TOOLKIT.md

PATTERN: Cost/Pricing
Examples:
- "How much does X cost"
- "Cheapest way to X"
- "Budget for X project"
Route to: 12_COST_OPTIMIZATION_GUIDE.md

PATTERN: Start Frame / I2V
Examples:
- "Best image model for start frames"
- "Niji 7 workflow"
- "First-last frame"
Route to: 07_IMAGE_MODELS_STATE_OF_UNION.md, 08_START_STOP_FRAME_DEEP_DIVE.md
```

---

## Response Templates

### Structured Response Format

When responding to queries from this corpus, agents should use:

```markdown
## Answer

[Direct answer to the query]

## Source

From: [Document Name]
Section: [Specific section]
Freshness: January 2026

## Details

[Supporting information, code, or workflow steps]

## Caveats

[Any limitations, freshness concerns, or scope boundaries]

## Related

[Cross-references to other relevant documents]
```

### Code Response Format

```markdown
## Code

```python
# From: 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
# Purpose: [Description]

[Code block]
```

## Usage

[How to use this code]

## Dependencies

[Required packages or setup]
```

---

## Cross-Reference Graph

### Document Relationships

```
00_INDEX.md
├── Links to ALL documents
└── Reading path recommendations

01_VIDEO_AI_COMPREHENSIVE_GUIDE.md
├── → 02_MODEL_SELECTION_DECISION_TREE.md (model details)
├── → 05_PLATFORM_HARNESS_GUIDE.md (platform access)
└── → 12_COST_OPTIMIZATION_GUIDE.md (pricing)

02_MODEL_SELECTION_DECISION_TREE.md
├── ← 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md (context)
└── → 11_WORKFLOW_RECIPES_COOKBOOK.md (workflows)

03_JSON_PROMPTING_GUIDE.md
├── → 04_PROMPT_TEMPLATE_LIBRARY.md (templates)
└── ← 11_WORKFLOW_RECIPES_COOKBOOK.md (usage)

07_IMAGE_MODELS_STATE_OF_UNION.md
├── → 08_START_STOP_FRAME_DEEP_DIVE.md (workflows)
└── → 09_CHARACTER_CONSISTENCY_GUIDE.md (consistency)

08_START_STOP_FRAME_DEEP_DIVE.md
├── ← 07_IMAGE_MODELS_STATE_OF_UNION.md (image models)
├── → 09_CHARACTER_CONSISTENCY_GUIDE.md (consistency)
└── → 11_WORKFLOW_RECIPES_COOKBOOK.md (recipes)

09_CHARACTER_CONSISTENCY_GUIDE.md
├── ← 08_START_STOP_FRAME_DEEP_DIVE.md (FLF)
└── → 11_WORKFLOW_RECIPES_COOKBOOK.md (workflows)

11_WORKFLOW_RECIPES_COOKBOOK.md
├── ← ALL technique documents
└── → 13_CLAUDE_CODE_VIDEO_TOOLKIT.md (automation)

13_CLAUDE_CODE_VIDEO_TOOLKIT.md
├── ← 05_PLATFORM_HARNESS_GUIDE.md (APIs)
├── ← 11_WORKFLOW_RECIPES_COOKBOOK.md (workflows)
└── → 14_AGENT_QUALITY_EVALS_FRAMEWORK.md (quality)
```

---

## Embedding Hints

### For Vector Database Ingestion

If embedding this corpus into a vector store, use these chunking strategies:

```yaml
Chunking Strategy:
  method: Semantic paragraphs
  max_chunk_size: 1000 tokens
  overlap: 100 tokens

Metadata to Include:
  - document_id (filename)
  - section_header
  - subsection_header
  - document_category
  - freshness_date: "2026-01"
  - domain: "video_ai"

High-Priority Chunks:
  - Code blocks (preserve intact)
  - Tables (preserve structure)
  - Decision trees (preserve intact)
  - JSON schemas (preserve intact)

Index Fields:
  - title
  - section
  - keywords
  - models_mentioned
  - platforms_mentioned
  - workflow_types
```

### Suggested Keywords per Document

```yaml
00_INDEX.md:
  - navigation, overview, contents, getting started

01_VIDEO_AI_COMPREHENSIVE_GUIDE.md:
  - veo, kling, sora, runway, models, overview, landscape

02_MODEL_SELECTION_DECISION_TREE.md:
  - choose, select, decision, comparison, which model

03_JSON_PROMPTING_GUIDE.md:
  - prompt, json, schema, structured, engineering

04_PROMPT_TEMPLATE_LIBRARY.md:
  - template, example, copy, paste, prompt

05_PLATFORM_HARNESS_GUIDE.md:
  - fal, replicate, api, platform, hosting

06_COMFYUI_NODE_WORKFLOWS_GUIDE.md:
  - comfyui, nodes, workflow, automation, pipeline

07_IMAGE_MODELS_STATE_OF_UNION.md:
  - image, midjourney, niji, flux, nano banana, start frame

08_START_STOP_FRAME_DEEP_DIVE.md:
  - first frame, last frame, flf, i2v, anime, wan

09_CHARACTER_CONSISTENCY_GUIDE.md:
  - character, consistency, ip adapter, lora, multi-shot

10_AUDIO_VIDEO_SYNC_GUIDE.md:
  - audio, sound, music, lip sync, voice

11_WORKFLOW_RECIPES_COOKBOOK.md:
  - recipe, cookbook, tutorial, step-by-step, production

12_COST_OPTIMIZATION_GUIDE.md:
  - cost, price, budget, cheap, expensive, optimize

13_CLAUDE_CODE_VIDEO_TOOLKIT.md:
  - python, script, automation, api, claude, code

14_AGENT_QUALITY_EVALS_FRAMEWORK.md:
  - quality, evaluation, metrics, assessment, llm judge

16_VIDEO_AI_INFLUENCERS_GUIDE.md:
  - influencer, twitter, youtube, community, follow

17_FUTURE_PROOFING_ROADMAP.md:
  - future, prediction, roadmap, 2026, 2027, trends

18_RESEARCH_LOG.md:
  - research, source, citation, reference, log
```

---

## Agent System Prompts

### Claude Code System Prompt Addition

```markdown
You have access to the Video AI Primer (January 2026).
This is a comprehensive knowledge base covering AI video generation.

When answering video AI questions:
1. Check 99_AGENTS.md for routing guidance
2. Load the appropriate document based on query intent
3. Cite specific sections in your responses
4. Note that this knowledge is from January 2026

Key files for common queries:
- Model selection: 02_MODEL_SELECTION_DECISION_TREE.md
- Prompting: 03_JSON_PROMPTING_GUIDE.md
- Image-to-Video: 07 and 08 (Image Models, Start/Stop Frames)
- Production: 11_WORKFLOW_RECIPES_COOKBOOK.md
- Code/Automation: 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
```

### Generic LLM System Prompt

```markdown
VIDEO AI KNOWLEDGE BASE CONTEXT

You have access to a January 2026 knowledge base on AI video generation.
The corpus covers:
- Video generation models (Veo, Kling, Sora, Runway, Wan, etc.)
- Image models for start frames (Midjourney, FLUX, Nano Banana)
- Prompting techniques (JSON structured prompts)
- Production workflows (FLF, I2V, character consistency)
- Automation (Python scripts, API integration)
- Cost optimization and legal considerations

When responding:
- Reference specific documents when applicable
- Provide code from the toolkit when relevant
- Note that information may be outdated for fast-moving areas
- Recommend web search for pricing or new releases
```

---

## Fallback Handling

### When Query Exceeds Corpus Scope

```markdown
SCOPE BOUNDARIES

This corpus COVERS:
✓ Video AI model capabilities and selection
✓ Image-to-video workflows (especially FLF)
✓ Prompting and templates
✓ Production techniques
✓ Python automation
✓ Cost and legal basics

This corpus DOES NOT COVER:
✗ Non-video AI (text, audio-only, 3D)
✗ Traditional video editing (Premiere, DaVinci basics)
✗ Hardware purchasing decisions
✗ Business/marketing strategy
✗ Real-time streaming video
✗ Video compression/codecs

FALLBACK RESPONSES:
If query exceeds scope:
"This query is outside the scope of the Video AI Primer.
The primer covers [list relevant topics].
For [query topic], I recommend [alternative resource or web search]."
```

---

## Version Control

```yaml
Version: 1.0
Date: January 18, 2026
Author: Video AI Primer Team

Changes:
  1.0:
    - Initial release
    - Full corpus documentation
    - Routing tables
    - Entity definitions
    - Embedding hints

Planned Updates:
  1.1:
    - Add real usage analytics
    - Refine routing based on query patterns
    - Update for new model releases
```

---

## Appendix: Full File List

```
/jan2026-video-gen/
├── 00_INDEX.md                         # Navigation & overview
├── 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md  # Foundation guide
├── 02_MODEL_SELECTION_DECISION_TREE.md # Model selection
├── 03_JSON_PROMPTING_GUIDE.md          # Prompt engineering
├── 04_PROMPT_TEMPLATE_LIBRARY.md       # Templates
├── 05_PLATFORM_HARNESS_GUIDE.md        # Platform APIs
├── 06_COMFYUI_NODE_WORKFLOWS_GUIDE.md  # ComfyUI
├── 07_IMAGE_MODELS_STATE_OF_UNION.md   # Image models
├── 08_START_STOP_FRAME_DEEP_DIVE.md    # FLF workflows
├── 09_CHARACTER_CONSISTENCY_GUIDE.md   # Consistency
├── 10_AUDIO_VIDEO_SYNC_GUIDE.md        # Audio
├── 11_WORKFLOW_RECIPES_COOKBOOK.md     # Recipes
├── 12_COST_OPTIMIZATION_GUIDE.md       # Cost
├── 13_CLAUDE_CODE_VIDEO_TOOLKIT.md     # Automation
├── 14_AGENT_QUALITY_EVALS_FRAMEWORK.md # Quality
├── 16_VIDEO_AI_INFLUENCERS_GUIDE.md    # Community
├── 17_FUTURE_PROOFING_ROADMAP.md       # Future
├── 18_RESEARCH_LOG.md                  # Sources
├── 99_AGENTS.md                        # This file
├── index.html                          # Web viewer
└── /archive/
    └── XX_PROPOSED_PRIMER_TASKS.md     # Historical
```

---

*AGENTS.md v1.0 — January 18, 2026*
*Optimized for Claude Code, OpenCode, Amp, Codex, and custom agents*

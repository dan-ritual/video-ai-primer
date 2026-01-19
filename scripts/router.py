#!/usr/bin/env python3
"""
Intelligent model router based on prompt analysis and requirements.

Usage:
    from router import ModelRouter, RoutingConfig, ContentType, QualityTier

    router = ModelRouter()
    config = RoutingConfig(
        content_type=ContentType.PRODUCT,
        quality_tier=QualityTier.STANDARD,
        max_cost=0.50
    )
    model = router.route(config)  # Returns "kling" or "hailuo"

    # Auto-detect content type from prompt
    content_type = router.analyze_prompt("Anime character running through city")
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class ContentType(Enum):
    CINEMATIC = "cinematic"
    PRODUCT = "product"
    TALKING_HEAD = "talking_head"
    ANIME = "anime"
    SOCIAL = "social"
    MUSIC_VIDEO = "music_video"

class QualityTier(Enum):
    DRAFT = "draft"
    STANDARD = "standard"
    PREMIUM = "premium"

@dataclass
class RoutingConfig:
    content_type: ContentType
    quality_tier: QualityTier
    max_cost: Optional[float] = None
    requires_audio: bool = False
    requires_consistency: bool = False

class ModelRouter:
    """Route requests to optimal model based on requirements."""

    ROUTING_TABLE = {
        (ContentType.CINEMATIC, QualityTier.PREMIUM): ["veo", "runway"],
        (ContentType.CINEMATIC, QualityTier.STANDARD): ["kling", "sora"],
        (ContentType.CINEMATIC, QualityTier.DRAFT): ["wan", "ltx"],

        (ContentType.PRODUCT, QualityTier.PREMIUM): ["runway", "veo"],
        (ContentType.PRODUCT, QualityTier.STANDARD): ["kling", "hailuo"],
        (ContentType.PRODUCT, QualityTier.DRAFT): ["pika", "wan"],

        (ContentType.ANIME, QualityTier.PREMIUM): ["wan"],
        (ContentType.ANIME, QualityTier.STANDARD): ["wan", "kling"],
        (ContentType.ANIME, QualityTier.DRAFT): ["wan"],

        (ContentType.SOCIAL, QualityTier.PREMIUM): ["kling", "pika"],
        (ContentType.SOCIAL, QualityTier.STANDARD): ["kling", "pika"],
        (ContentType.SOCIAL, QualityTier.DRAFT): ["pika", "wan"],

        (ContentType.MUSIC_VIDEO, QualityTier.PREMIUM): ["seedance", "kling"],
        (ContentType.MUSIC_VIDEO, QualityTier.STANDARD): ["seedance"],
        (ContentType.MUSIC_VIDEO, QualityTier.DRAFT): ["kling", "wan"],
    }

    MODEL_COSTS = {
        "veo": 1.00,      # per 5s
        "runway": 1.25,
        "sora": 1.10,
        "kling": 0.28,
        "seedance": 0.50,
        "hailuo": 0.28,
        "pika": 0.20,
        "wan": 0.05,      # local/API
        "ltx": 0.10,
    }

    def route(self, config: RoutingConfig) -> str:
        """Get optimal model for given configuration."""

        candidates = self.ROUTING_TABLE.get(
            (config.content_type, config.quality_tier),
            ["kling"]  # Default fallback
        )

        # Filter by cost constraint
        if config.max_cost:
            candidates = [
                m for m in candidates
                if self.MODEL_COSTS.get(m, 0) <= config.max_cost
            ]

        # Special requirements
        if config.requires_audio:
            audio_capable = ["veo", "ltx", "seedance"]
            candidates = [m for m in candidates if m in audio_capable]

        if not candidates:
            raise ValueError("No models match requirements")

        return candidates[0]

    def analyze_prompt(self, prompt: str) -> ContentType:
        """Analyze prompt to determine content type."""

        prompt_lower = prompt.lower()

        if any(kw in prompt_lower for kw in ["anime", "manga", "cartoon", "animated"]):
            return ContentType.ANIME

        if any(kw in prompt_lower for kw in ["product", "floating", "rotating", "hero shot"]):
            return ContentType.PRODUCT

        if any(kw in prompt_lower for kw in ["speaking", "talking", "presenter", "avatar"]):
            return ContentType.TALKING_HEAD

        if any(kw in prompt_lower for kw in ["dance", "music", "beat", "choreography"]):
            return ContentType.MUSIC_VIDEO

        if any(kw in prompt_lower for kw in ["cinematic", "film", "movie", "dramatic"]):
            return ContentType.CINEMATIC

        return ContentType.SOCIAL  # Default


if __name__ == "__main__":
    # Demo usage
    router = ModelRouter()

    # Example 1: Product video with cost constraint
    config = RoutingConfig(
        content_type=ContentType.PRODUCT,
        quality_tier=QualityTier.STANDARD,
        max_cost=0.50
    )
    model = router.route(config)
    print(f"Product video (standard, <$0.50): {model}")

    # Example 2: Auto-detect from prompt
    prompt = "Anime character running through neon city at night"
    content_type = router.analyze_prompt(prompt)
    print(f"Detected content type for '{prompt[:40]}...': {content_type.value}")

    # Example 3: Premium cinematic
    config = RoutingConfig(
        content_type=ContentType.CINEMATIC,
        quality_tier=QualityTier.PREMIUM
    )
    model = router.route(config)
    print(f"Cinematic (premium): {model}")

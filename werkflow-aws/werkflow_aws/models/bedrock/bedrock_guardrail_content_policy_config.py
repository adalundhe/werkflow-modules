from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_content_filter_config import BedrockGuardrailContentFilterConfig
from .bedrock_guardrail_content_filters_tier_config import BedrockGuardrailContentFiltersTierConfig


class BedrockGuardrailContentPolicyConfig(BaseModel):
    filtersConfig: list[BedrockGuardrailContentFilterConfig]
    tierConfig: BedrockGuardrailContentFiltersTierConfig | None = None

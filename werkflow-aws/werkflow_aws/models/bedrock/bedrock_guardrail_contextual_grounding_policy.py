from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_contextual_grounding_filter import BedrockGuardrailContextualGroundingFilter
from .bedrock_guardrail_contextual_grounding_tier import BedrockGuardrailContextualGroundingTier


class BedrockGuardrailContextualGroundingPolicy(BaseModel):
    filters: list[BedrockGuardrailContextualGroundingFilter] | None = None
    tier: BedrockGuardrailContextualGroundingTier | None = None

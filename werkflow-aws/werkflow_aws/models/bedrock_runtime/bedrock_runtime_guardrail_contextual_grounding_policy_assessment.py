from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_contextual_grounding_filter import BedrockRuntimeGuardrailContextualGroundingFilter


class BedrockRuntimeGuardrailContextualGroundingPolicyAssessment(BaseModel):
    filters: list[BedrockRuntimeGuardrailContextualGroundingFilter] | None = None

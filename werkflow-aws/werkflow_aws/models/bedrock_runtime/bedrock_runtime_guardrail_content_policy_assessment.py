from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_content_filter import BedrockRuntimeGuardrailContentFilter


class BedrockRuntimeGuardrailContentPolicyAssessment(BaseModel):
    filters: list[BedrockRuntimeGuardrailContentFilter] | None = None

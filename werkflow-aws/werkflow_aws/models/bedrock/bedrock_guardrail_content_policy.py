from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_content_filter import BedrockGuardrailContentFilter
from .bedrock_guardrail_content_filters_tier import BedrockGuardrailContentFiltersTier


class BedrockGuardrailContentPolicy(BaseModel):
    filters: list[BedrockGuardrailContentFilter] | None = None
    tier: BedrockGuardrailContentFiltersTier | None = None

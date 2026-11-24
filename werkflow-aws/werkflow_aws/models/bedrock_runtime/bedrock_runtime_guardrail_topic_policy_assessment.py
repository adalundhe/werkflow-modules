from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_topic import BedrockRuntimeGuardrailTopic


class BedrockRuntimeGuardrailTopicPolicyAssessment(BaseModel):
    topics: list[BedrockRuntimeGuardrailTopic] | None = None

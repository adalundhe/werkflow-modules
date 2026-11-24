from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_topic import BedrockGuardrailTopic
from .bedrock_guardrail_topics_tier import BedrockGuardrailTopicsTier


class BedrockGuardrailTopicPolicy(BaseModel):
    topics: list[BedrockGuardrailTopic] | None = None
    tier: BedrockGuardrailTopicsTier | None = None

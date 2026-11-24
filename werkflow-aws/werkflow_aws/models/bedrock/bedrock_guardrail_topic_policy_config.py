from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_topic_config import BedrockGuardrailTopicConfig
from .bedrock_guardrail_topics_tier_config import BedrockGuardrailTopicsTierConfig


class BedrockGuardrailTopicPolicyConfig(BaseModel):
    topicsConfig: list[BedrockGuardrailTopicConfig]
    tierConfig: BedrockGuardrailTopicsTierConfig | None = None

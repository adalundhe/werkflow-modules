from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_bedrock_guardrails import WAFv2BedrockGuardrails


class WAFv2AWSManagedRulesAISecurityRuleSet(BaseModel):
    BedrockGuardrails: WAFv2BedrockGuardrails | None = None

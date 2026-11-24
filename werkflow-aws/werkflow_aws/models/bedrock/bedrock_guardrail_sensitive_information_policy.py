from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_pii_entity import BedrockGuardrailPiiEntity
from .bedrock_guardrail_regex import BedrockGuardrailRegex


class BedrockGuardrailSensitiveInformationPolicy(BaseModel):
    piiEntities: list[BedrockGuardrailPiiEntity] | None = None
    regexes: list[BedrockGuardrailRegex] | None = None

from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_pii_entity_config import BedrockGuardrailPiiEntityConfig
from .bedrock_guardrail_regex_config import BedrockGuardrailRegexConfig


class BedrockGuardrailSensitiveInformationPolicyConfig(BaseModel):
    piiEntitiesConfig: list[BedrockGuardrailPiiEntityConfig] | None = None
    regexesConfig: list[BedrockGuardrailRegexConfig] | None = None

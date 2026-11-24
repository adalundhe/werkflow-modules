from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_pii_entity_filter import BedrockRuntimeGuardrailPiiEntityFilter
from .bedrock_runtime_guardrail_regex_filter import BedrockRuntimeGuardrailRegexFilter


class BedrockRuntimeGuardrailSensitiveInformationPolicyAssessment(BaseModel):
    piiEntities: list[BedrockRuntimeGuardrailPiiEntityFilter] | None = None
    regexes: list[BedrockRuntimeGuardrailRegexFilter] | None = None

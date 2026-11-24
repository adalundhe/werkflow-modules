from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .bedrock_runtime_guardrail_checks_sensitive_information_result_entry import BedrockRuntimeGuardrailChecksSensitiveInformationResultEntry


class BedrockRuntimeGuardrailChecksSensitiveInformationResult(BaseModel):
    results: list[BedrockRuntimeGuardrailChecksSensitiveInformationResultEntry] | None = None
    truncated: StrictBool | None = None

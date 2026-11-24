from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_runtime_guardrail_checks_results import BedrockRuntimeGuardrailChecksResults
from .bedrock_runtime_guardrail_checks_usage_results import BedrockRuntimeGuardrailChecksUsageResults


class BedrockRuntimeInvokeGuardrailChecksResponse(BaseModel):
    results: BedrockRuntimeGuardrailChecksResults | None = None
    usage: BedrockRuntimeGuardrailChecksUsageResults | None = None
    ResponseMetadata: dict[str, Any] | None = None

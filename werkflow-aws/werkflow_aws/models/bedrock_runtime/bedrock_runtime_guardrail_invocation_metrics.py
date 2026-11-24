from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_runtime_guardrail_coverage import BedrockRuntimeGuardrailCoverage
from .bedrock_runtime_guardrail_usage import BedrockRuntimeGuardrailUsage


class BedrockRuntimeGuardrailInvocationMetrics(BaseModel):
    guardrailProcessingLatency: StrictInt | None = None
    usage: BedrockRuntimeGuardrailUsage | None = None
    guardrailCoverage: BedrockRuntimeGuardrailCoverage | None = None

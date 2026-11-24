from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_guardrail_assessment import BedrockRuntimeGuardrailAssessment
from .bedrock_runtime_guardrail_coverage import BedrockRuntimeGuardrailCoverage
from .bedrock_runtime_guardrail_output_content import BedrockRuntimeGuardrailOutputContent
from .bedrock_runtime_guardrail_usage import BedrockRuntimeGuardrailUsage


class BedrockRuntimeApplyGuardrailResponse(BaseModel):
    usage: BedrockRuntimeGuardrailUsage | None = None
    action: StrictStr | None = None
    actionReason: StrictStr | None = None
    outputs: list[BedrockRuntimeGuardrailOutputContent] | None = None
    assessments: list[BedrockRuntimeGuardrailAssessment] | None = None
    guardrailCoverage: BedrockRuntimeGuardrailCoverage | None = None
    ResponseMetadata: dict[str, Any] | None = None

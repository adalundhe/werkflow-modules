from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_guardrail_assessment import BedrockRuntimeGuardrailAssessment


class BedrockRuntimeGuardrailTraceAssessment(BaseModel):
    modelOutput: list[StrictStr] | None = None
    inputAssessment: dict[StrictStr, BedrockRuntimeGuardrailAssessment] | None = None
    outputAssessments: dict[StrictStr, list[BedrockRuntimeGuardrailAssessment]] | None = None
    actionReason: StrictStr | None = None

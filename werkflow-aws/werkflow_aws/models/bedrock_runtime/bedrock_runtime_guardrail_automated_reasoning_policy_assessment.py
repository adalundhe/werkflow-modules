from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_automated_reasoning_finding import BedrockRuntimeGuardrailAutomatedReasoningFinding


class BedrockRuntimeGuardrailAutomatedReasoningPolicyAssessment(BaseModel):
    findings: list[BedrockRuntimeGuardrailAutomatedReasoningFinding] | None = None

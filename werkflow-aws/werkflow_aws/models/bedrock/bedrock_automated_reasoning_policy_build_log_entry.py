from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_annotation import BedrockAutomatedReasoningPolicyAnnotation
from .bedrock_automated_reasoning_policy_build_step import BedrockAutomatedReasoningPolicyBuildStep


class BedrockAutomatedReasoningPolicyBuildLogEntry(BaseModel):
    annotation: BedrockAutomatedReasoningPolicyAnnotation | None = None
    status: StrictStr | None = None
    buildSteps: list[BedrockAutomatedReasoningPolicyBuildStep] | None = None

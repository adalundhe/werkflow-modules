from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_annotation import BedrockAutomatedReasoningPolicyAnnotation


class BedrockUpdateAutomatedReasoningPolicyAnnotationsRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    annotations: list[BedrockAutomatedReasoningPolicyAnnotation]
    lastUpdatedAnnotationSetHash: StrictStr

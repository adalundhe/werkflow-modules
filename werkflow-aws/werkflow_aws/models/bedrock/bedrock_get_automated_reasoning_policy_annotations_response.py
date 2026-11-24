from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_annotation import BedrockAutomatedReasoningPolicyAnnotation


class BedrockGetAutomatedReasoningPolicyAnnotationsResponse(BaseModel):
    policyArn: StrictStr | None = None
    name: StrictStr | None = None
    buildWorkflowId: StrictStr | None = None
    annotations: list[BedrockAutomatedReasoningPolicyAnnotation] | None = None
    annotationSetHash: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

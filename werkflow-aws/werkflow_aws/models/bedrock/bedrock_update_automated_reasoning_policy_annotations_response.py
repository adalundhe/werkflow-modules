from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockUpdateAutomatedReasoningPolicyAnnotationsResponse(BaseModel):
    policyArn: StrictStr | None = None
    buildWorkflowId: StrictStr | None = None
    annotationSetHash: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

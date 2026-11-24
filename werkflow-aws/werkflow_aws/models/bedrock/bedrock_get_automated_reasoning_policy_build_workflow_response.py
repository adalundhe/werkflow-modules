from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyBuildWorkflowResponse(BaseModel):
    policyArn: StrictStr | None = None
    buildWorkflowId: StrictStr | None = None
    status: StrictStr | None = None
    buildWorkflowType: StrictStr | None = None
    documentName: StrictStr | None = None
    documentContentType: StrictStr | None = None
    documentDescription: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyBuildWorkflowSummary(BaseModel):
    policyArn: StrictStr | None = None
    buildWorkflowId: StrictStr | None = None
    status: StrictStr | None = None
    buildWorkflowType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None

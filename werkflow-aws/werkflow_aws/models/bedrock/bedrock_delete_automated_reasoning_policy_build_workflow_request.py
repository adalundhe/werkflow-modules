from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockDeleteAutomatedReasoningPolicyBuildWorkflowRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    lastUpdatedAt: datetime.datetime | StrictStr

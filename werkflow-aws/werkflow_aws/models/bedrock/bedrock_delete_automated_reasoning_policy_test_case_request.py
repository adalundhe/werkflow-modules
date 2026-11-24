from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockDeleteAutomatedReasoningPolicyTestCaseRequest(BaseModel):
    policyArn: StrictStr
    testCaseId: StrictStr
    lastUpdatedAt: datetime.datetime | StrictStr

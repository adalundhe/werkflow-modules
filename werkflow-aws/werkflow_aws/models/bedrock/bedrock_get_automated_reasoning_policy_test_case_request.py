from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyTestCaseRequest(BaseModel):
    policyArn: StrictStr
    testCaseId: StrictStr

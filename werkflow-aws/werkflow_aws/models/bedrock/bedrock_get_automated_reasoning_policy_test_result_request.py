from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyTestResultRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    testCaseId: StrictStr

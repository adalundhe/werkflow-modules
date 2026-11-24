from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockStartAutomatedReasoningPolicyTestWorkflowRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    testCaseIds: list[StrictStr] | None = None
    clientRequestToken: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockCancelAutomatedReasoningPolicyBuildWorkflowRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr

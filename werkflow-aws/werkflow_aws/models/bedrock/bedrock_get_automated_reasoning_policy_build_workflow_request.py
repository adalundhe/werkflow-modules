from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyBuildWorkflowRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr

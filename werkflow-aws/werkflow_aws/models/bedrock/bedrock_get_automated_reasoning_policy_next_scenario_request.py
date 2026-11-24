from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyNextScenarioRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyAnnotationsRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyRequest(BaseModel):
    policyArn: StrictStr

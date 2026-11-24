from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockDeleteAutomatedReasoningPolicyRequest(BaseModel):
    policyArn: StrictStr
    force: StrictBool | None = None

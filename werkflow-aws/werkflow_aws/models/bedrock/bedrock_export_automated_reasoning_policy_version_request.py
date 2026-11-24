from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockExportAutomatedReasoningPolicyVersionRequest(BaseModel):
    policyArn: StrictStr

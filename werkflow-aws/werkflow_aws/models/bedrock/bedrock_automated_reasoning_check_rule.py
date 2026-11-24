from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningCheckRule(BaseModel):
    id: StrictStr | None = None
    policyVersionArn: StrictStr | None = None

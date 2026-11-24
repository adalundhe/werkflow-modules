from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDeleteTypeValue(BaseModel):
    value: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDeleteTypeMutation(BaseModel):
    name: StrictStr | None = None

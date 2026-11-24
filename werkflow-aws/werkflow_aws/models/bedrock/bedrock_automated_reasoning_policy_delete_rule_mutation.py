from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDeleteRuleMutation(BaseModel):
    id: StrictStr | None = None

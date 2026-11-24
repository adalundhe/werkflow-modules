from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyUpdateVariableAnnotation(BaseModel):
    name: StrictStr | None = None
    newName: StrictStr | None = None
    description: StrictStr | None = None

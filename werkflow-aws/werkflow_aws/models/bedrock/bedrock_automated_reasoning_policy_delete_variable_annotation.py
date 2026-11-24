from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDeleteVariableAnnotation(BaseModel):
    name: StrictStr | None = None

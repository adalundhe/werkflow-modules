from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDefinitionTypeValuePair(BaseModel):
    typeName: StrictStr | None = None
    valueName: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetGuardrailRequest(BaseModel):
    guardrailIdentifier: StrictStr
    guardrailVersion: StrictStr | None = None

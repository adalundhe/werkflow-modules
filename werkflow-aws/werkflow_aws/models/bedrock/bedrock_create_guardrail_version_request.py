from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockCreateGuardrailVersionRequest(BaseModel):
    guardrailIdentifier: StrictStr
    description: StrictStr | None = None
    clientRequestToken: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailPiiEntity(BaseModel):
    type: StrictStr | None = None
    action: StrictStr | None = None
    inputAction: StrictStr | None = None
    outputAction: StrictStr | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

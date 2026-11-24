from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailWord(BaseModel):
    text: StrictStr | None = None
    inputAction: StrictStr | None = None
    outputAction: StrictStr | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

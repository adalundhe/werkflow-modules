from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailManagedWords(BaseModel):
    type: StrictStr | None = None
    inputAction: StrictStr | None = None
    outputAction: StrictStr | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

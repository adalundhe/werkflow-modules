from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailContentFilter(BaseModel):
    type: StrictStr | None = None
    inputStrength: StrictStr | None = None
    outputStrength: StrictStr | None = None
    inputModalities: list[StrictStr] | None = None
    outputModalities: list[StrictStr] | None = None
    inputAction: StrictStr | None = None
    outputAction: StrictStr | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

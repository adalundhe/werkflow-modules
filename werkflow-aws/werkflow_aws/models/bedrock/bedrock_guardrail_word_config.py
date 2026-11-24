from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailWordConfig(BaseModel):
    text: StrictStr
    inputAction: Literal['BLOCK', 'NONE'] | None = None
    outputAction: Literal['BLOCK', 'NONE'] | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

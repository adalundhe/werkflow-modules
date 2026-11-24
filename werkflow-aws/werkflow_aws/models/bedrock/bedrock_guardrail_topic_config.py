from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailTopicConfig(BaseModel):
    name: StrictStr
    definition: StrictStr
    type: Literal['DENY']
    examples: list[StrictStr] | None = None
    inputAction: Literal['BLOCK', 'NONE'] | None = None
    outputAction: Literal['BLOCK', 'NONE'] | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

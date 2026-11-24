from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailRegexConfig(BaseModel):
    name: StrictStr
    pattern: StrictStr
    action: Literal['BLOCK', 'ANONYMIZE', 'NONE']
    description: StrictStr | None = None
    inputAction: Literal['BLOCK', 'ANONYMIZE', 'NONE'] | None = None
    outputAction: Literal['BLOCK', 'ANONYMIZE', 'NONE'] | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None

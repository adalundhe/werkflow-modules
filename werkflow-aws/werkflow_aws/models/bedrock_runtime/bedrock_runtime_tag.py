from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeTag(BaseModel):
    key: StrictStr
    value: StrictStr

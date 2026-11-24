from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeSpecificToolChoice(BaseModel):
    name: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeSystemTool(BaseModel):
    name: StrictStr

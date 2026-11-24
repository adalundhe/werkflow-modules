from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeErrorBlock(BaseModel):
    message: StrictStr | None = None

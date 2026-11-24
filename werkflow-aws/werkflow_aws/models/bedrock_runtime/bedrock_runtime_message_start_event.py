from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeMessageStartEvent(BaseModel):
    role: StrictStr | None = None

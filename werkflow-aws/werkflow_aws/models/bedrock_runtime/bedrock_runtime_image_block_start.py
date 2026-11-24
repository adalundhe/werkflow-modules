from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeImageBlockStart(BaseModel):
    format: StrictStr | None = None

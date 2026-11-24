from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeToolUseBlockDelta(BaseModel):
    input: StrictStr | None = None

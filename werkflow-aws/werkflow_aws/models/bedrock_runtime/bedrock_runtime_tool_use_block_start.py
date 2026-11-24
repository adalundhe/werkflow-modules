from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeToolUseBlockStart(BaseModel):
    toolUseId: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None

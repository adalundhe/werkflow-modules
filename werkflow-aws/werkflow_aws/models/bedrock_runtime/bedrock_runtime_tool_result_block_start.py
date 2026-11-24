from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeToolResultBlockStart(BaseModel):
    toolUseId: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None

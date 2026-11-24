from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeSearchResultContentBlock(BaseModel):
    text: StrictStr | None = None

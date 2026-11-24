from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeServiceTier(BaseModel):
    type: StrictStr | None = None

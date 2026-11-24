from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockModelEnforcement(BaseModel):
    includedModels: list[StrictStr] | None = None
    excludedModels: list[StrictStr] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSlotResolutionSetting(BaseModel):
    slotResolutionStrategy: StrictStr | None = None

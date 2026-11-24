from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexSlotPriority(BaseModel):
    priority: StrictInt | None = None
    slotId: StrictStr | None = None

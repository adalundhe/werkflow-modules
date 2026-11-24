from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSlot(BaseModel):
    SlotId: StrictStr | None = None
    VisualId: StrictStr | None = None

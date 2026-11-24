from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSubSlotTypeComposition(BaseModel):
    name: StrictStr | None = None
    slotTypeId: StrictStr | None = None

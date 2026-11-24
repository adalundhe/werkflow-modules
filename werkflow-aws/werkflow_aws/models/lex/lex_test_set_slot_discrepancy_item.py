from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTestSetSlotDiscrepancyItem(BaseModel):
    intentName: StrictStr | None = None
    slotName: StrictStr | None = None
    errorMessage: StrictStr | None = None

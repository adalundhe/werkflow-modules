from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBuiltInSlotTypeSummary(BaseModel):
    slotTypeSignature: StrictStr | None = None
    description: StrictStr | None = None

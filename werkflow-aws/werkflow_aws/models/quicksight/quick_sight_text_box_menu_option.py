from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTextBoxMenuOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

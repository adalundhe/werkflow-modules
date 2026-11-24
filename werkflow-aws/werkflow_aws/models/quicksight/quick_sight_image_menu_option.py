from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightImageMenuOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

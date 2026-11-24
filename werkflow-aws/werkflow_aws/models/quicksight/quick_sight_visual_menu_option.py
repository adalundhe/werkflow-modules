from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVisualMenuOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

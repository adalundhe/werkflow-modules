from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPointDrillUpDownOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPointMenuLabelOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

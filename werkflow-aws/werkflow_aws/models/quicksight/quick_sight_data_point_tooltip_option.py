from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPointTooltipOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExecutiveSummaryOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

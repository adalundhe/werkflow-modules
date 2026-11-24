from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataQAEnabledOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

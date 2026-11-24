from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAdHocFilteringOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

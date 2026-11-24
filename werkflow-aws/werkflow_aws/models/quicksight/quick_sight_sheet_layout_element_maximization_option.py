from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetLayoutElementMaximizationOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

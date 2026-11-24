from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVisualAxisSortOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

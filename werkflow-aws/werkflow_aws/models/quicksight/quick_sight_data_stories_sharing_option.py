from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataStoriesSharingOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None

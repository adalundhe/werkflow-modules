from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyScannedItemCount(BaseModel):
    TotalGb: StrictInt | None = None
    Files: StrictInt | None = None
    Volumes: StrictInt | None = None

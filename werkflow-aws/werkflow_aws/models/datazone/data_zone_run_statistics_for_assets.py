from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataZoneRunStatisticsForAssets(BaseModel):
    added: StrictInt | None = None
    updated: StrictInt | None = None
    unchanged: StrictInt | None = None
    skipped: StrictInt | None = None
    failed: StrictInt | None = None

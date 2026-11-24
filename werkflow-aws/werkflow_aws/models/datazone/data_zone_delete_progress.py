from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataZoneDeleteProgress(BaseModel):
    successfullyDeletedProjectCount: StrictInt | None = None

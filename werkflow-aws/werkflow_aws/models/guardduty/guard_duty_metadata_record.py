from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyMetadataRecord(BaseModel):
    TotalTimeMilliseconds: StrictInt | None = None

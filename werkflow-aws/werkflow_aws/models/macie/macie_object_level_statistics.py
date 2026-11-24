from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieObjectLevelStatistics(BaseModel):
    fileType: StrictInt | None = None
    storageClass: StrictInt | None = None
    total: StrictInt | None = None

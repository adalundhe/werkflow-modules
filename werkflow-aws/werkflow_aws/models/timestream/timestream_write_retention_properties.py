from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TimestreamWriteRetentionProperties(BaseModel):
    MemoryStoreRetentionPeriodInHours: StrictInt | None = None
    MagneticStoreRetentionPeriodInDays: StrictInt | None = None

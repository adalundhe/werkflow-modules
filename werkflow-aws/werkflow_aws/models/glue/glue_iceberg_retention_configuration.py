from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class GlueIcebergRetentionConfiguration(BaseModel):
    snapshotRetentionPeriodInDays: StrictInt | None = None
    numberOfSnapshotsToRetain: StrictInt | None = None
    cleanExpiredFiles: StrictBool | None = None
    runRateInHours: StrictInt | None = None

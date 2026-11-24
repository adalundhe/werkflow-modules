from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LakeFormationExecutionStatistics(BaseModel):
    AverageExecutionTimeMillis: StrictInt | None = None
    DataScannedBytes: StrictInt | None = None
    WorkUnitsExecutedCount: StrictInt | None = None

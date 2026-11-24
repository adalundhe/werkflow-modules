from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LakeFormationPlanningStatistics(BaseModel):
    EstimatedDataToScanBytes: StrictInt | None = None
    PlanningTimeMillis: StrictInt | None = None
    QueueTimeMillis: StrictInt | None = None
    WorkUnitsGeneratedCount: StrictInt | None = None

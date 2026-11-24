from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTTaskStatisticsForAuditCheck(BaseModel):
    totalFindingsCount: StrictInt | None = None
    failedFindingsCount: StrictInt | None = None
    succeededFindingsCount: StrictInt | None = None
    skippedFindingsCount: StrictInt | None = None
    canceledFindingsCount: StrictInt | None = None

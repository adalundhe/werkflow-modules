from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DMSReplicationTaskAssessmentRunResultStatistic(BaseModel):
    Passed: StrictInt | None = None
    Failed: StrictInt | None = None
    Error: StrictInt | None = None
    Warning: StrictInt | None = None
    Cancelled: StrictInt | None = None
    Skipped: StrictInt | None = None

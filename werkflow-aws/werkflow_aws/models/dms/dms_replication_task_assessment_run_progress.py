from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DMSReplicationTaskAssessmentRunProgress(BaseModel):
    IndividualAssessmentCount: StrictInt | None = None
    IndividualAssessmentCompletedCount: StrictInt | None = None

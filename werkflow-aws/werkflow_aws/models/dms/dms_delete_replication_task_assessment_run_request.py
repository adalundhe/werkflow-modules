from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteReplicationTaskAssessmentRunRequest(BaseModel):
    ReplicationTaskAssessmentRunArn: StrictStr

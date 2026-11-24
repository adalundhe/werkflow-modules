from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSCancelReplicationTaskAssessmentRunRequest(BaseModel):
    ReplicationTaskAssessmentRunArn: StrictStr

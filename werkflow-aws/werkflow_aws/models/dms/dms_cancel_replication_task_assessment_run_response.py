from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication_task_assessment_run import DMSReplicationTaskAssessmentRun


class DMSCancelReplicationTaskAssessmentRunResponse(BaseModel):
    ReplicationTaskAssessmentRun: DMSReplicationTaskAssessmentRun | None = None
    ResponseMetadata: dict[str, Any] | None = None

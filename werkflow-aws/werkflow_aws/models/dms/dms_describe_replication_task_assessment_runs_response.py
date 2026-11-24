from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_task_assessment_run import DMSReplicationTaskAssessmentRun


class DMSDescribeReplicationTaskAssessmentRunsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationTaskAssessmentRuns: list[DMSReplicationTaskAssessmentRun] | None = None
    ResponseMetadata: dict[str, Any] | None = None

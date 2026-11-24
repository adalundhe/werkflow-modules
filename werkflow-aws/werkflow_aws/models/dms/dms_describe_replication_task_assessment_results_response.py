from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_task_assessment_result import DMSReplicationTaskAssessmentResult


class DMSDescribeReplicationTaskAssessmentResultsResponse(BaseModel):
    Marker: StrictStr | None = None
    BucketName: StrictStr | None = None
    ReplicationTaskAssessmentResults: list[DMSReplicationTaskAssessmentResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None

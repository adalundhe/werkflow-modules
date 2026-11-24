from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_task_individual_assessment import DMSReplicationTaskIndividualAssessment


class DMSDescribeReplicationTaskIndividualAssessmentsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationTaskIndividualAssessments: list[DMSReplicationTaskIndividualAssessment] | None = None
    ResponseMetadata: dict[str, Any] | None = None

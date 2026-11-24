from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_entities_detection_job_filter import ComprehendEntitiesDetectionJobFilter


class ComprehendListEntitiesDetectionJobsRequest(BaseModel):
    Filter: ComprehendEntitiesDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

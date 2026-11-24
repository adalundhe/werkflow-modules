from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_pii_entities_detection_job_filter import ComprehendPiiEntitiesDetectionJobFilter


class ComprehendListPiiEntitiesDetectionJobsRequest(BaseModel):
    Filter: ComprehendPiiEntitiesDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

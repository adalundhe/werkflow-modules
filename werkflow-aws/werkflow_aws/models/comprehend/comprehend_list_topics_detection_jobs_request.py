from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_topics_detection_job_filter import ComprehendTopicsDetectionJobFilter


class ComprehendListTopicsDetectionJobsRequest(BaseModel):
    Filter: ComprehendTopicsDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

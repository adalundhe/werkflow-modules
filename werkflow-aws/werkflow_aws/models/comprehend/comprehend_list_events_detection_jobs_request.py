from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_events_detection_job_filter import ComprehendEventsDetectionJobFilter


class ComprehendListEventsDetectionJobsRequest(BaseModel):
    Filter: ComprehendEventsDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

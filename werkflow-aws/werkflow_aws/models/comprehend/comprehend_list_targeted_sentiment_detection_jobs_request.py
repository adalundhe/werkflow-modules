from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_targeted_sentiment_detection_job_filter import ComprehendTargetedSentimentDetectionJobFilter


class ComprehendListTargetedSentimentDetectionJobsRequest(BaseModel):
    Filter: ComprehendTargetedSentimentDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

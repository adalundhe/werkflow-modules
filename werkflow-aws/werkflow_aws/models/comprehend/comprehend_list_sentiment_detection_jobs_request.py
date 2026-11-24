from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_sentiment_detection_job_filter import ComprehendSentimentDetectionJobFilter


class ComprehendListSentimentDetectionJobsRequest(BaseModel):
    Filter: ComprehendSentimentDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

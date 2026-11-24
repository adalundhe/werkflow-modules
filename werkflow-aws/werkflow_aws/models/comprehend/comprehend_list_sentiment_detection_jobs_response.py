from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_sentiment_detection_job_properties import ComprehendSentimentDetectionJobProperties


class ComprehendListSentimentDetectionJobsResponse(BaseModel):
    SentimentDetectionJobPropertiesList: list[ComprehendSentimentDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_targeted_sentiment_detection_job_properties import ComprehendTargetedSentimentDetectionJobProperties


class ComprehendListTargetedSentimentDetectionJobsResponse(BaseModel):
    TargetedSentimentDetectionJobPropertiesList: list[ComprehendTargetedSentimentDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

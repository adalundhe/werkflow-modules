from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_sentiment_detection_job_properties import ComprehendSentimentDetectionJobProperties


class ComprehendDescribeSentimentDetectionJobResponse(BaseModel):
    SentimentDetectionJobProperties: ComprehendSentimentDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

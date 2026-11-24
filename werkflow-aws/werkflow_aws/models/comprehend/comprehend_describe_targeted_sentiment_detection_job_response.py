from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_targeted_sentiment_detection_job_properties import ComprehendTargetedSentimentDetectionJobProperties


class ComprehendDescribeTargetedSentimentDetectionJobResponse(BaseModel):
    TargetedSentimentDetectionJobProperties: ComprehendTargetedSentimentDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

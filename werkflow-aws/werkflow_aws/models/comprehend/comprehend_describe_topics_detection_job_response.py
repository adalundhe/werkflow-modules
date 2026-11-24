from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_topics_detection_job_properties import ComprehendTopicsDetectionJobProperties


class ComprehendDescribeTopicsDetectionJobResponse(BaseModel):
    TopicsDetectionJobProperties: ComprehendTopicsDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

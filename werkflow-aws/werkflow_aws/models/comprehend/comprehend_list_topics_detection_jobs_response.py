from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_topics_detection_job_properties import ComprehendTopicsDetectionJobProperties


class ComprehendListTopicsDetectionJobsResponse(BaseModel):
    TopicsDetectionJobPropertiesList: list[ComprehendTopicsDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

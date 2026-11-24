from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_events_detection_job_properties import ComprehendEventsDetectionJobProperties


class ComprehendDescribeEventsDetectionJobResponse(BaseModel):
    EventsDetectionJobProperties: ComprehendEventsDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

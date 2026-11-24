from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_events_detection_job_properties import ComprehendEventsDetectionJobProperties


class ComprehendListEventsDetectionJobsResponse(BaseModel):
    EventsDetectionJobPropertiesList: list[ComprehendEventsDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

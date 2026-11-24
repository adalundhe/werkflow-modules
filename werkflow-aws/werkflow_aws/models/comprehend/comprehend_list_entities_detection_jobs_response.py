from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_entities_detection_job_properties import ComprehendEntitiesDetectionJobProperties


class ComprehendListEntitiesDetectionJobsResponse(BaseModel):
    EntitiesDetectionJobPropertiesList: list[ComprehendEntitiesDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

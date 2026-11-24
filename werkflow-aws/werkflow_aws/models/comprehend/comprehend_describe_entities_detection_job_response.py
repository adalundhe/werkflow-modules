from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_entities_detection_job_properties import ComprehendEntitiesDetectionJobProperties


class ComprehendDescribeEntitiesDetectionJobResponse(BaseModel):
    EntitiesDetectionJobProperties: ComprehendEntitiesDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

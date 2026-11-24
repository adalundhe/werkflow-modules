from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_pii_entities_detection_job_properties import ComprehendPiiEntitiesDetectionJobProperties


class ComprehendDescribePiiEntitiesDetectionJobResponse(BaseModel):
    PiiEntitiesDetectionJobProperties: ComprehendPiiEntitiesDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

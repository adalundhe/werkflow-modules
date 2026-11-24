from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_pii_entities_detection_job_properties import ComprehendPiiEntitiesDetectionJobProperties


class ComprehendListPiiEntitiesDetectionJobsResponse(BaseModel):
    PiiEntitiesDetectionJobPropertiesList: list[ComprehendPiiEntitiesDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

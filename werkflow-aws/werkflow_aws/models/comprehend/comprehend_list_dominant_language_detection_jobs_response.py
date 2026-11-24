from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_dominant_language_detection_job_properties import ComprehendDominantLanguageDetectionJobProperties


class ComprehendListDominantLanguageDetectionJobsResponse(BaseModel):
    DominantLanguageDetectionJobPropertiesList: list[ComprehendDominantLanguageDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

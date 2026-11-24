from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_dominant_language_detection_job_properties import ComprehendDominantLanguageDetectionJobProperties


class ComprehendDescribeDominantLanguageDetectionJobResponse(BaseModel):
    DominantLanguageDetectionJobProperties: ComprehendDominantLanguageDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

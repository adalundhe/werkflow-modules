from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_dominant_language_detection_job_filter import ComprehendDominantLanguageDetectionJobFilter


class ComprehendListDominantLanguageDetectionJobsRequest(BaseModel):
    Filter: ComprehendDominantLanguageDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

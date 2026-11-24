from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_key_phrases_detection_job_properties import ComprehendKeyPhrasesDetectionJobProperties


class ComprehendListKeyPhrasesDetectionJobsResponse(BaseModel):
    KeyPhrasesDetectionJobPropertiesList: list[ComprehendKeyPhrasesDetectionJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

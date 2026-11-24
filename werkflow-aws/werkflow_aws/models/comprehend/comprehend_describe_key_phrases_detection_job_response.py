from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_key_phrases_detection_job_properties import ComprehendKeyPhrasesDetectionJobProperties


class ComprehendDescribeKeyPhrasesDetectionJobResponse(BaseModel):
    KeyPhrasesDetectionJobProperties: ComprehendKeyPhrasesDetectionJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None

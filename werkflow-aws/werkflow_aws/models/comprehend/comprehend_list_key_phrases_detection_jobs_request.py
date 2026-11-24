from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_key_phrases_detection_job_filter import ComprehendKeyPhrasesDetectionJobFilter


class ComprehendListKeyPhrasesDetectionJobsRequest(BaseModel):
    Filter: ComprehendKeyPhrasesDetectionJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

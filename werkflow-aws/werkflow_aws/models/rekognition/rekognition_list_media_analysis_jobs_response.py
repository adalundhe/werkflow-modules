from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_media_analysis_job_description import RekognitionMediaAnalysisJobDescription


class RekognitionListMediaAnalysisJobsResponse(BaseModel):
    NextToken: StrictStr | None = None
    MediaAnalysisJobs: list[RekognitionMediaAnalysisJobDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None

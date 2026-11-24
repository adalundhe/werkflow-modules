from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_person_detection import RekognitionPersonDetection
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetPersonTrackingResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: RekognitionVideoMetadata | None = None
    NextToken: StrictStr | None = None
    Persons: list[RekognitionPersonDetection] | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

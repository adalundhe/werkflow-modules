from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_celebrity_recognition import RekognitionCelebrityRecognition
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetCelebrityRecognitionResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: RekognitionVideoMetadata | None = None
    NextToken: StrictStr | None = None
    Celebrities: list[RekognitionCelebrityRecognition] | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

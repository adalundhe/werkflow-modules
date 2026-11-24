from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_text_detection_result import RekognitionTextDetectionResult
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetTextDetectionResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: RekognitionVideoMetadata | None = None
    TextDetections: list[RekognitionTextDetectionResult] | None = None
    NextToken: StrictStr | None = None
    TextModelVersion: StrictStr | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

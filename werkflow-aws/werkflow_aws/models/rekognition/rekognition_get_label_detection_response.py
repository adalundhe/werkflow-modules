from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_get_label_detection_request_metadata import RekognitionGetLabelDetectionRequestMetadata
from .rekognition_label_detection import RekognitionLabelDetection
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetLabelDetectionResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: RekognitionVideoMetadata | None = None
    NextToken: StrictStr | None = None
    Labels: list[RekognitionLabelDetection] | None = None
    LabelModelVersion: StrictStr | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    GetRequestMetadata: RekognitionGetLabelDetectionRequestMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None

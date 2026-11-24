from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_content_moderation_detection import RekognitionContentModerationDetection
from .rekognition_get_content_moderation_request_metadata import RekognitionGetContentModerationRequestMetadata
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetContentModerationResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: RekognitionVideoMetadata | None = None
    ModerationLabels: list[RekognitionContentModerationDetection] | None = None
    NextToken: StrictStr | None = None
    ModerationModelVersion: StrictStr | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    GetRequestMetadata: RekognitionGetContentModerationRequestMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None

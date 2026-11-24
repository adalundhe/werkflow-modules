from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_audio_metadata import RekognitionAudioMetadata
from .rekognition_segment_detection import RekognitionSegmentDetection
from .rekognition_segment_type_info import RekognitionSegmentTypeInfo
from .rekognition_video import RekognitionVideo
from .rekognition_video_metadata import RekognitionVideoMetadata


class RekognitionGetSegmentDetectionResponse(BaseModel):
    JobStatus: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    VideoMetadata: list[RekognitionVideoMetadata] | None = None
    AudioMetadata: list[RekognitionAudioMetadata] | None = None
    NextToken: StrictStr | None = None
    Segments: list[RekognitionSegmentDetection] | None = None
    SelectedSegmentTypes: list[RekognitionSegmentTypeInfo] | None = None
    JobId: StrictStr | None = None
    Video: RekognitionVideo | None = None
    JobTag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

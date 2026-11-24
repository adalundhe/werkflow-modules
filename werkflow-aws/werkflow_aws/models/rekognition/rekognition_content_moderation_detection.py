from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_content_type import RekognitionContentType
from .rekognition_moderation_label import RekognitionModerationLabel


class RekognitionContentModerationDetection(BaseModel):
    Timestamp: StrictInt | None = None
    ModerationLabel: RekognitionModerationLabel | None = None
    StartTimestampMillis: StrictInt | None = None
    EndTimestampMillis: StrictInt | None = None
    DurationMillis: StrictInt | None = None
    ContentTypes: list[RekognitionContentType] | None = None

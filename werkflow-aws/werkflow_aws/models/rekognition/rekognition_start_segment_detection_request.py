from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_start_segment_detection_filters import RekognitionStartSegmentDetectionFilters
from .rekognition_video import RekognitionVideo


class RekognitionStartSegmentDetectionRequest(BaseModel):
    Video: RekognitionVideo
    SegmentTypes: list[Literal['TECHNICAL_CUE', 'SHOT']]
    ClientRequestToken: StrictStr | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    JobTag: StrictStr | None = None
    Filters: RekognitionStartSegmentDetectionFilters | None = None

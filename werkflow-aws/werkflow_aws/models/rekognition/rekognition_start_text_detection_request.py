from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_start_text_detection_filters import RekognitionStartTextDetectionFilters
from .rekognition_video import RekognitionVideo


class RekognitionStartTextDetectionRequest(BaseModel):
    Video: RekognitionVideo
    ClientRequestToken: StrictStr | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    JobTag: StrictStr | None = None
    Filters: RekognitionStartTextDetectionFilters | None = None

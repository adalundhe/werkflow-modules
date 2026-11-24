from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_video import RekognitionVideo


class RekognitionStartFaceDetectionRequest(BaseModel):
    Video: RekognitionVideo
    ClientRequestToken: StrictStr | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    FaceAttributes: Literal['DEFAULT', 'ALL'] | None = None
    JobTag: StrictStr | None = None

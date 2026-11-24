from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_label_detection_settings import RekognitionLabelDetectionSettings
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_video import RekognitionVideo


class RekognitionStartLabelDetectionRequest(BaseModel):
    Video: RekognitionVideo
    ClientRequestToken: StrictStr | None = None
    MinConfidence: StrictFloat | StrictInt | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    JobTag: StrictStr | None = None
    Features: list[Literal['GENERAL_LABELS']] | None = None
    Settings: RekognitionLabelDetectionSettings | None = None

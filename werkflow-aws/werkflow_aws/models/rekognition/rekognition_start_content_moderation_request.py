from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_video import RekognitionVideo


class RekognitionStartContentModerationRequest(BaseModel):
    Video: RekognitionVideo
    MinConfidence: StrictFloat | StrictInt | None = None
    ClientRequestToken: StrictStr | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    JobTag: StrictStr | None = None

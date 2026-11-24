from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_notification_channel import RekognitionNotificationChannel
from .rekognition_video import RekognitionVideo


class RekognitionStartFaceSearchRequest(BaseModel):
    Video: RekognitionVideo
    CollectionId: StrictStr
    ClientRequestToken: StrictStr | None = None
    FaceMatchThreshold: StrictFloat | StrictInt | None = None
    NotificationChannel: RekognitionNotificationChannel | None = None
    JobTag: StrictStr | None = None

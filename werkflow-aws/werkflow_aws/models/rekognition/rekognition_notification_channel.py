from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionNotificationChannel(BaseModel):
    SNSTopicArn: StrictStr
    RoleArn: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractNotificationChannel(BaseModel):
    SNSTopicArn: StrictStr
    RoleArn: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSPutNotificationChannelRequest(BaseModel):
    SnsTopicArn: StrictStr
    SnsRoleName: StrictStr

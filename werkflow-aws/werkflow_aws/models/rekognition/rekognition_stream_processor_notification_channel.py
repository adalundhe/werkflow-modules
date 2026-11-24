from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionStreamProcessorNotificationChannel(BaseModel):
    SNSTopicArn: StrictStr | None = None

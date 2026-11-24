from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerNotificationConfiguration(BaseModel):
    NotificationTopicArn: StrictStr | None = None

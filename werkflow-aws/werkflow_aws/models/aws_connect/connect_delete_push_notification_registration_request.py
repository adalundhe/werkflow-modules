from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeletePushNotificationRegistrationRequest(BaseModel):
    InstanceId: StrictStr
    RegistrationId: StrictStr
    ContactId: StrictStr

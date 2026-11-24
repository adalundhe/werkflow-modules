from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_contact_configuration import ConnectContactConfiguration


class ConnectCreatePushNotificationRegistrationRequest(BaseModel):
    InstanceId: StrictStr
    PinpointAppArn: StrictStr
    DeviceToken: StrictStr
    DeviceType: Literal['GCM', 'APNS', 'APNS_SANDBOX']
    ContactConfiguration: ConnectContactConfiguration
    ClientToken: StrictStr | None = None

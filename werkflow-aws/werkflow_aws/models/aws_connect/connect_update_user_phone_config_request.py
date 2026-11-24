from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_user_phone_config import ConnectUserPhoneConfig


class ConnectUpdateUserPhoneConfigRequest(BaseModel):
    PhoneConfig: ConnectUserPhoneConfig
    UserId: StrictStr
    InstanceId: StrictStr

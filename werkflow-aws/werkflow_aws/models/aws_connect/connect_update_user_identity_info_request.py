from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_user_identity_info import ConnectUserIdentityInfo


class ConnectUpdateUserIdentityInfoRequest(BaseModel):
    IdentityInfo: ConnectUserIdentityInfo
    UserId: StrictStr
    InstanceId: StrictStr

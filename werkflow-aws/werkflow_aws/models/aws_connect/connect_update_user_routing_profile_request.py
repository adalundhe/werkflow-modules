from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateUserRoutingProfileRequest(BaseModel):
    RoutingProfileId: StrictStr
    UserId: StrictStr
    InstanceId: StrictStr

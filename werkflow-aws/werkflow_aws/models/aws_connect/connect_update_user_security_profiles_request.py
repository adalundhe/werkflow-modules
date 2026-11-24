from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateUserSecurityProfilesRequest(BaseModel):
    SecurityProfileIds: list[StrictStr]
    UserId: StrictStr
    InstanceId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteRoutingProfileRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeRoutingProfileRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr

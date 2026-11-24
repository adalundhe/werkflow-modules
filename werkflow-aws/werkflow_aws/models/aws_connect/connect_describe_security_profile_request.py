from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeSecurityProfileRequest(BaseModel):
    SecurityProfileId: StrictStr
    InstanceId: StrictStr

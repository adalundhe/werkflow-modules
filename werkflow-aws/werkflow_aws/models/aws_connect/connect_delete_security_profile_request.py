from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteSecurityProfileRequest(BaseModel):
    InstanceId: StrictStr
    SecurityProfileId: StrictStr

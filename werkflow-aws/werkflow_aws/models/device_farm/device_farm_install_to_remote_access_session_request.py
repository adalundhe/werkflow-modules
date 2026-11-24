from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmInstallToRemoteAccessSessionRequest(BaseModel):
    remoteAccessSessionArn: StrictStr
    appArn: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmCreateTestGridUrlRequest(BaseModel):
    projectArn: StrictStr
    expiresInSeconds: StrictInt

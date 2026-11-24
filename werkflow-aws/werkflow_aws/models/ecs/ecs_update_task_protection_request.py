from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ECSUpdateTaskProtectionRequest(BaseModel):
    cluster: StrictStr
    tasks: list[StrictStr]
    protectionEnabled: StrictBool
    expiresInMinutes: StrictInt | None = None

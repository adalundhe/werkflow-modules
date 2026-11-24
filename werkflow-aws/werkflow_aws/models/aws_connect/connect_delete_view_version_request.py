from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeleteViewVersionRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
    ViewVersion: StrictInt

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteViewRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteQuickConnectRequest(BaseModel):
    InstanceId: StrictStr
    QuickConnectId: StrictStr

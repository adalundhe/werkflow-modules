from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeQuickConnectRequest(BaseModel):
    InstanceId: StrictStr
    QuickConnectId: StrictStr

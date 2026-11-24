from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_quick_connect_config import ConnectQuickConnectConfig


class ConnectCreateQuickConnectRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    QuickConnectConfig: ConnectQuickConnectConfig
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None

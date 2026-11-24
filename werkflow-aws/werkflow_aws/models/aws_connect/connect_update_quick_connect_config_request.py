from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_quick_connect_config import ConnectQuickConnectConfig


class ConnectUpdateQuickConnectConfigRequest(BaseModel):
    InstanceId: StrictStr
    QuickConnectId: StrictStr
    QuickConnectConfig: ConnectQuickConnectConfig

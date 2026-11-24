from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_quick_connect_config import ConnectQuickConnectConfig


class ConnectQuickConnect(BaseModel):
    QuickConnectARN: StrictStr | None = None
    QuickConnectId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    QuickConnectConfig: ConnectQuickConnectConfig | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateQuickConnectNameRequest(BaseModel):
    InstanceId: StrictStr
    QuickConnectId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None

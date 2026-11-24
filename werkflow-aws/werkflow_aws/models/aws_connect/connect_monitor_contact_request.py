from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectMonitorContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    UserId: StrictStr
    AllowedMonitorCapabilities: list[Literal['SILENT_MONITOR', 'BARGE']] | None = None
    ClientToken: StrictStr | None = None

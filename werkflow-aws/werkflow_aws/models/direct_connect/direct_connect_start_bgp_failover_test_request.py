from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectStartBgpFailoverTestRequest(BaseModel):
    virtualInterfaceId: StrictStr
    bgpPeers: list[StrictStr] | None = None
    testDurationInMinutes: StrictInt | None = None

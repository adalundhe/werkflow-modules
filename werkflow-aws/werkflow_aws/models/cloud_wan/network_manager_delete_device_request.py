from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteDeviceRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr

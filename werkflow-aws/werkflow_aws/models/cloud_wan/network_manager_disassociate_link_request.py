from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDisassociateLinkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr
    LinkId: StrictStr

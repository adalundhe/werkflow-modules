from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteLinkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    LinkId: StrictStr

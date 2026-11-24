from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteGlobalNetworkRequest(BaseModel):
    GlobalNetworkId: StrictStr

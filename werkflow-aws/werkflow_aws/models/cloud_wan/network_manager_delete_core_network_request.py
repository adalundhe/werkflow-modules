from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteCoreNetworkRequest(BaseModel):
    CoreNetworkId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetCoreNetworkRequest(BaseModel):
    CoreNetworkId: StrictStr

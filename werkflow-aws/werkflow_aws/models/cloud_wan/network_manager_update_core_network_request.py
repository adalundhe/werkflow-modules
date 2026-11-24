from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateCoreNetworkRequest(BaseModel):
    CoreNetworkId: StrictStr
    Description: StrictStr | None = None

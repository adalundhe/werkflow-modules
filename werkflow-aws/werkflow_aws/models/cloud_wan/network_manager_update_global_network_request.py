from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateGlobalNetworkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    Description: StrictStr | None = None

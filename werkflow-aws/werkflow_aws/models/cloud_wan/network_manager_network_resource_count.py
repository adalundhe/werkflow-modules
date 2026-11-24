from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerNetworkResourceCount(BaseModel):
    ResourceType: StrictStr | None = None
    Count: StrictInt | None = None

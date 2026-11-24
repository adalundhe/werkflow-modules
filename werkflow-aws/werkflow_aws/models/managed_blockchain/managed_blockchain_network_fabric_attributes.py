from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNetworkFabricAttributes(BaseModel):
    OrderingServiceEndpoint: StrictStr | None = None
    Edition: StrictStr | None = None

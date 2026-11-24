from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNodeEthereumAttributes(BaseModel):
    HttpEndpoint: StrictStr | None = None
    WebSocketEndpoint: StrictStr | None = None

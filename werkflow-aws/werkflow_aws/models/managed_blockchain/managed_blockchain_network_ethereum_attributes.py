from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNetworkEthereumAttributes(BaseModel):
    ChainId: StrictStr | None = None

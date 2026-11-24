from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_network_configuration import IdentityStoreNetworkConfiguration


class IdentityStoreUpdateIdentityStoreRequest(BaseModel):
    IdentityStoreId: StrictStr
    NetworkConfiguration: IdentityStoreNetworkConfiguration | None = None

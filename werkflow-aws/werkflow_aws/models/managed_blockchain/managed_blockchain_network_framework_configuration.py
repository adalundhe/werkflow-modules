from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_network_fabric_configuration import ManagedBlockchainNetworkFabricConfiguration


class ManagedBlockchainNetworkFrameworkConfiguration(BaseModel):
    Fabric: ManagedBlockchainNetworkFabricConfiguration | None = None

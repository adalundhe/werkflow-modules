from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_network_ethereum_attributes import ManagedBlockchainNetworkEthereumAttributes
from .managed_blockchain_network_fabric_attributes import ManagedBlockchainNetworkFabricAttributes


class ManagedBlockchainNetworkFrameworkAttributes(BaseModel):
    Fabric: ManagedBlockchainNetworkFabricAttributes | None = None
    Ethereum: ManagedBlockchainNetworkEthereumAttributes | None = None

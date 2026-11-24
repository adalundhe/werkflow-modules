from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_node_ethereum_attributes import ManagedBlockchainNodeEthereumAttributes
from .managed_blockchain_node_fabric_attributes import ManagedBlockchainNodeFabricAttributes


class ManagedBlockchainNodeFrameworkAttributes(BaseModel):
    Fabric: ManagedBlockchainNodeFabricAttributes | None = None
    Ethereum: ManagedBlockchainNodeEthereumAttributes | None = None

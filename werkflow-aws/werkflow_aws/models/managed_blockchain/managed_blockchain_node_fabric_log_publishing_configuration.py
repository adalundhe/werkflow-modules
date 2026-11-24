from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_log_configurations import ManagedBlockchainLogConfigurations


class ManagedBlockchainNodeFabricLogPublishingConfiguration(BaseModel):
    ChaincodeLogs: ManagedBlockchainLogConfigurations | None = None
    PeerLogs: ManagedBlockchainLogConfigurations | None = None

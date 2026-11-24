from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_log_configurations import ManagedBlockchainLogConfigurations


class ManagedBlockchainMemberFabricLogPublishingConfiguration(BaseModel):
    CaLogs: ManagedBlockchainLogConfigurations | None = None

from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_member_fabric_configuration import ManagedBlockchainMemberFabricConfiguration


class ManagedBlockchainMemberFrameworkConfiguration(BaseModel):
    Fabric: ManagedBlockchainMemberFabricConfiguration | None = None

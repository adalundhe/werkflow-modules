from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_member_fabric_attributes import ManagedBlockchainMemberFabricAttributes


class ManagedBlockchainMemberFrameworkAttributes(BaseModel):
    Fabric: ManagedBlockchainMemberFabricAttributes | None = None

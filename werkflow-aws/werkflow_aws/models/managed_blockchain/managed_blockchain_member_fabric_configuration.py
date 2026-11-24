from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainMemberFabricConfiguration(BaseModel):
    AdminUsername: StrictStr
    AdminPassword: StrictStr

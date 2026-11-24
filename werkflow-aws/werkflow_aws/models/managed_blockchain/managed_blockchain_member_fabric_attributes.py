from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainMemberFabricAttributes(BaseModel):
    AdminUsername: StrictStr | None = None
    CaEndpoint: StrictStr | None = None

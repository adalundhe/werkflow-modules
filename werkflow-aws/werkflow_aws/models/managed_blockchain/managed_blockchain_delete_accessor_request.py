from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainDeleteAccessorRequest(BaseModel):
    AccessorId: StrictStr

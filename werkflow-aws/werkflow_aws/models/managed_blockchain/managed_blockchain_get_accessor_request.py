from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainGetAccessorRequest(BaseModel):
    AccessorId: StrictStr

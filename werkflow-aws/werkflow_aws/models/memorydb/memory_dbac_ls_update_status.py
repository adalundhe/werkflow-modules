from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBACLsUpdateStatus(BaseModel):
    ACLToApply: StrictStr | None = None

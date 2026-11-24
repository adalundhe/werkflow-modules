from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAcceptDelegationRequestRequest(BaseModel):
    DelegationRequestId: StrictStr

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMRejectDelegationRequestRequest(BaseModel):
    DelegationRequestId: StrictStr
    Notes: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateDelegationRequestRequest(BaseModel):
    DelegationRequestId: StrictStr
    Notes: StrictStr | None = None

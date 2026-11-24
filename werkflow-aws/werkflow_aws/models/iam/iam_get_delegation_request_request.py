from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IAMGetDelegationRequestRequest(BaseModel):
    DelegationRequestId: StrictStr
    DelegationPermissionCheck: StrictBool | None = None

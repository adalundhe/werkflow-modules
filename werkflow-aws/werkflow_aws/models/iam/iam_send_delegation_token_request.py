from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMSendDelegationTokenRequest(BaseModel):
    DelegationRequestId: StrictStr

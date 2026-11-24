from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMCreateServiceSpecificCredentialRequest(BaseModel):
    UserName: StrictStr
    ServiceName: StrictStr
    CredentialAgeDays: StrictInt | None = None

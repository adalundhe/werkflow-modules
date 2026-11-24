from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMResetServiceSpecificCredentialRequest(BaseModel):
    ServiceSpecificCredentialId: StrictStr
    UserName: StrictStr | None = None

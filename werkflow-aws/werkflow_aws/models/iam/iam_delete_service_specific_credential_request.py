from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteServiceSpecificCredentialRequest(BaseModel):
    ServiceSpecificCredentialId: StrictStr
    UserName: StrictStr | None = None

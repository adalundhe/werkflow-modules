from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMUpdateServiceSpecificCredentialRequest(BaseModel):
    ServiceSpecificCredentialId: StrictStr
    Status: Literal['Active', 'Inactive', 'Expired']
    UserName: StrictStr | None = None

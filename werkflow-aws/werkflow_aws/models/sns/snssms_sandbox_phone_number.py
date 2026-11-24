from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSMSSandboxPhoneNumber(BaseModel):
    PhoneNumber: StrictStr | None = None
    Status: StrictStr | None = None

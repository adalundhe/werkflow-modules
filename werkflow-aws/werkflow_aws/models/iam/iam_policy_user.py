from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPolicyUser(BaseModel):
    UserName: StrictStr | None = None
    UserId: StrictStr | None = None

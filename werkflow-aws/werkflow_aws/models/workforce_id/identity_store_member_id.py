from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreMemberId(BaseModel):
    UserId: StrictStr | None = None

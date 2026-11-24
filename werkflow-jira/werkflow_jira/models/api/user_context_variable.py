from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UserContextVariable(BaseModel):
    accountId: StrictStr | None = None
    type: StrictStr | None = None

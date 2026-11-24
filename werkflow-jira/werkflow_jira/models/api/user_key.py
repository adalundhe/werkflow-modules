from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UserKey(BaseModel):
    accountId: StrictStr | None = None
    key: StrictStr | None = None

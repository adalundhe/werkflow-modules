from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ChangeFilterOwner(BaseModel):
    accountId: StrictStr | None = None

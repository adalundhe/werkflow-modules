from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraUserField(BaseModel):
    accountId: StrictStr | None = None

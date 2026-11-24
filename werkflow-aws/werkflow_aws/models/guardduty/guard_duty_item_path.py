from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyItemPath(BaseModel):
    NestedItemPath: StrictStr | None = None
    Hash: StrictStr | None = None

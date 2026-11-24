from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBACLPendingChanges(BaseModel):
    UserNamesToRemove: list[StrictStr] | None = None
    UserNamesToAdd: list[StrictStr] | None = None

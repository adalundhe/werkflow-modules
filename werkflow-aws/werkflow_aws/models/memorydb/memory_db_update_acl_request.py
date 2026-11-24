from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBUpdateACLRequest(BaseModel):
    ACLName: StrictStr
    UserNamesToAdd: list[StrictStr] | None = None
    UserNamesToRemove: list[StrictStr] | None = None

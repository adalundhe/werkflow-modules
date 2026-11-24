from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheUserGroupPendingChanges(BaseModel):
    UserIdsToRemove: list[StrictStr] | None = None
    UserIdsToAdd: list[StrictStr] | None = None

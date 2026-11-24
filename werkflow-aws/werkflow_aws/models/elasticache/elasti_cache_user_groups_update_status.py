from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheUserGroupsUpdateStatus(BaseModel):
    UserGroupIdsToAdd: list[StrictStr] | None = None
    UserGroupIdsToRemove: list[StrictStr] | None = None

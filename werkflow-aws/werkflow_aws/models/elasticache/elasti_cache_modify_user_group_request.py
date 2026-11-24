from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheModifyUserGroupRequest(BaseModel):
    UserGroupId: StrictStr
    UserIdsToAdd: list[StrictStr] | None = None
    UserIdsToRemove: list[StrictStr] | None = None
    Engine: StrictStr | None = None

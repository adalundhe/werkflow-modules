from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteUserGroupRequest(BaseModel):
    UserGroupId: StrictStr

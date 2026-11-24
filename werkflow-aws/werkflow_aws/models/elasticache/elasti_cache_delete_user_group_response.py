from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_user_group_pending_changes import ElastiCacheUserGroupPendingChanges


class ElastiCacheDeleteUserGroupResponse(BaseModel):
    UserGroupId: StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    UserIds: list[StrictStr] | None = None
    MinimumEngineVersion: StrictStr | None = None
    PendingChanges: ElastiCacheUserGroupPendingChanges | None = None
    ReplicationGroups: list[StrictStr] | None = None
    ServerlessCaches: list[StrictStr] | None = None
    ARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

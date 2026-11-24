from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_authentication import ElastiCacheAuthentication


class ElastiCacheCreateUserResponse(BaseModel):
    UserId: StrictStr | None = None
    UserName: StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    MinimumEngineVersion: StrictStr | None = None
    AccessString: StrictStr | None = None
    UserGroupIds: list[StrictStr] | None = None
    Authentication: ElastiCacheAuthentication | None = None
    ARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

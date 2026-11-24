from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_authentication_mode import ElastiCacheAuthenticationMode
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateUserRequest(BaseModel):
    UserId: StrictStr
    UserName: StrictStr
    Engine: StrictStr
    AccessString: StrictStr
    Passwords: list[StrictStr] | None = None
    NoPasswordRequired: StrictBool | None = None
    Tags: list[ElastiCacheTag] | None = None
    AuthenticationMode: ElastiCacheAuthenticationMode | None = None

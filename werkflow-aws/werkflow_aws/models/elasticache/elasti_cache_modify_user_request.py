from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_authentication_mode import ElastiCacheAuthenticationMode


class ElastiCacheModifyUserRequest(BaseModel):
    UserId: StrictStr
    AccessString: StrictStr | None = None
    AppendAccessString: StrictStr | None = None
    Passwords: list[StrictStr] | None = None
    NoPasswordRequired: StrictBool | None = None
    AuthenticationMode: ElastiCacheAuthenticationMode | None = None
    Engine: StrictStr | None = None

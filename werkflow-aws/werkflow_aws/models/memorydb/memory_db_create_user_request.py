from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_authentication_mode import MemoryDBAuthenticationMode
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateUserRequest(BaseModel):
    UserName: StrictStr
    AuthenticationMode: MemoryDBAuthenticationMode
    AccessString: StrictStr
    Tags: list[MemoryDBTag] | None = None

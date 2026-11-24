from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_authentication_mode import MemoryDBAuthenticationMode


class MemoryDBUpdateUserRequest(BaseModel):
    UserName: StrictStr
    AuthenticationMode: MemoryDBAuthenticationMode | None = None
    AccessString: StrictStr | None = None

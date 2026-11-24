from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_authentication import MemoryDBAuthentication


class MemoryDBUser(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    AccessString: StrictStr | None = None
    ACLNames: list[StrictStr] | None = None
    MinimumEngineVersion: StrictStr | None = None
    Authentication: MemoryDBAuthentication | None = None
    ARN: StrictStr | None = None

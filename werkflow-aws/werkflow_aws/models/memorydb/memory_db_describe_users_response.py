from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_user import MemoryDBUser


class MemoryDBDescribeUsersResponse(BaseModel):
    Users: list[MemoryDBUser] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_user import MemoryDBUser


class MemoryDBCreateUserResponse(BaseModel):
    User: MemoryDBUser | None = None
    ResponseMetadata: dict[str, Any] | None = None

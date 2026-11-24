from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_dbacl import MemoryDBACL


class MemoryDBCreateACLResponse(BaseModel):
    ACL: MemoryDBACL | None = None
    ResponseMetadata: dict[str, Any] | None = None

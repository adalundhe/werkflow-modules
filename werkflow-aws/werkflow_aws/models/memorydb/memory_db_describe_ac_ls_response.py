from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_dbacl import MemoryDBACL


class MemoryDBDescribeACLsResponse(BaseModel):
    ACLs: list[MemoryDBACL] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

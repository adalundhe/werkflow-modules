from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_subnet_group import MemoryDBSubnetGroup


class MemoryDBDeleteSubnetGroupResponse(BaseModel):
    SubnetGroup: MemoryDBSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

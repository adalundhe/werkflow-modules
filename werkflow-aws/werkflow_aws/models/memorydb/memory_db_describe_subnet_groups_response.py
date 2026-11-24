from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_subnet_group import MemoryDBSubnetGroup


class MemoryDBDescribeSubnetGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    SubnetGroups: list[MemoryDBSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

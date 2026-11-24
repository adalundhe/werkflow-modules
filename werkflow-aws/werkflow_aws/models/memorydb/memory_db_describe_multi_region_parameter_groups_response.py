from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_multi_region_parameter_group import MemoryDBMultiRegionParameterGroup


class MemoryDBDescribeMultiRegionParameterGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    MultiRegionParameterGroups: list[MemoryDBMultiRegionParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

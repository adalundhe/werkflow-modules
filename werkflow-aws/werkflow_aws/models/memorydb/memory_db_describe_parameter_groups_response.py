from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_parameter_group import MemoryDBParameterGroup


class MemoryDBDescribeParameterGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ParameterGroups: list[MemoryDBParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

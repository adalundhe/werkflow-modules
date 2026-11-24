from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_parameter_group import MemoryDBParameterGroup


class MemoryDBResetParameterGroupResponse(BaseModel):
    ParameterGroup: MemoryDBParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

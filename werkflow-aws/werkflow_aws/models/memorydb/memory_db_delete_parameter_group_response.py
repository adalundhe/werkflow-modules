from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_parameter_group import MemoryDBParameterGroup


class MemoryDBDeleteParameterGroupResponse(BaseModel):
    ParameterGroup: MemoryDBParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

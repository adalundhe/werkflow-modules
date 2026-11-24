from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_parameter_name_value import MemoryDBParameterNameValue


class MemoryDBUpdateParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
    ParameterNameValues: list[MemoryDBParameterNameValue]

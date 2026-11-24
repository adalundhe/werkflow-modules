from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MemoryDBResetParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
    AllParameters: StrictBool | None = None
    ParameterNames: list[StrictStr] | None = None

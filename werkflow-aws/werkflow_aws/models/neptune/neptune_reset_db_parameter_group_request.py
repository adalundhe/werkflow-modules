from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneResetDBParameterGroupRequest(BaseModel):
    DBParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    Parameters: list[NeptuneParameter] | None = None

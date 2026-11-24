from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneResetDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    Parameters: list[NeptuneParameter] | None = None

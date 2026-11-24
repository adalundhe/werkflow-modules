from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneModifyDBParameterGroupRequest(BaseModel):
    DBParameterGroupName: StrictStr
    Parameters: list[NeptuneParameter]

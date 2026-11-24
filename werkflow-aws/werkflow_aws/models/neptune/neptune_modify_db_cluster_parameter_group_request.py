from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneModifyDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    Parameters: list[NeptuneParameter]

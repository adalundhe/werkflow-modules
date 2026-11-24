from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    DBParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[NeptuneTag] | None = None

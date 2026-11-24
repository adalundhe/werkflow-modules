from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBParameterGroupRequest(BaseModel):
    DBParameterGroupName: StrictStr
    DBParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[NeptuneTag] | None = None

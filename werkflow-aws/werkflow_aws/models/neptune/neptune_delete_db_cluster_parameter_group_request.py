from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDeleteDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr

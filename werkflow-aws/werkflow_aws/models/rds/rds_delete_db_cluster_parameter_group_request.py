from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr

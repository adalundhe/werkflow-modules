from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr

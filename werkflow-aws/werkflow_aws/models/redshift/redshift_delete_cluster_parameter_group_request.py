from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteClusterParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr

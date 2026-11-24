from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_parameter import RDSParameter


class RDSModifyDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    Parameters: list[RDSParameter]

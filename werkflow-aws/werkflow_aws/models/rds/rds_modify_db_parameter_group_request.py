from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_parameter import RDSParameter


class RDSModifyDBParameterGroupRequest(BaseModel):
    DBParameterGroupName: StrictStr
    Parameters: list[RDSParameter]

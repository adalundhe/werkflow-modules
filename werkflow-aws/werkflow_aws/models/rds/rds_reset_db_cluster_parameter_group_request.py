from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_parameter import RDSParameter


class RDSResetDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    Parameters: list[RDSParameter] | None = None

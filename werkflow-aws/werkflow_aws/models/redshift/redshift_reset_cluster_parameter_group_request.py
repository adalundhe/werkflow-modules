from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_parameter import RedshiftParameter


class RedshiftResetClusterParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    Parameters: list[RedshiftParameter] | None = None

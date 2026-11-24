from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_parameter import RedshiftParameter


class RedshiftModifyClusterParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
    Parameters: list[RedshiftParameter]

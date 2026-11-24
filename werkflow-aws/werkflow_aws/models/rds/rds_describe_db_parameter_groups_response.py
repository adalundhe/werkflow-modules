from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_parameter_group import RDSDBParameterGroup


class RDSDescribeDBParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBParameterGroups: list[RDSDBParameterGroup] | None = None

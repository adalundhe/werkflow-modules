from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_parameter_group import RDSDBClusterParameterGroup


class RDSDescribeDBClusterParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterParameterGroups: list[RDSDBClusterParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

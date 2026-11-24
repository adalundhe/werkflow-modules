from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_cluster_parameter_group import NeptuneDBClusterParameterGroup


class NeptuneDescribeDBClusterParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterParameterGroups: list[NeptuneDBClusterParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

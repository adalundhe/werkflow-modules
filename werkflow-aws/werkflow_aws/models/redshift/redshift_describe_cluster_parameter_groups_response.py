from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster_parameter_group import RedshiftClusterParameterGroup


class RedshiftDescribeClusterParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    ParameterGroups: list[RedshiftClusterParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

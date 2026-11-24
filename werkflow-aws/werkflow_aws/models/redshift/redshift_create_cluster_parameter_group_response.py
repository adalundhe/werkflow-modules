from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster_parameter_group import RedshiftClusterParameterGroup


class RedshiftCreateClusterParameterGroupResponse(BaseModel):
    ClusterParameterGroup: RedshiftClusterParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

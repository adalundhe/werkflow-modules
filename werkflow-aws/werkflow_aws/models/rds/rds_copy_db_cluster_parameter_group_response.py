from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_cluster_parameter_group import RDSDBClusterParameterGroup


class RDSCopyDBClusterParameterGroupResponse(BaseModel):
    DBClusterParameterGroup: RDSDBClusterParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

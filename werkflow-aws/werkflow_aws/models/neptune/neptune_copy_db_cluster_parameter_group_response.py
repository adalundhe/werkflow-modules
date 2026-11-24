from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_cluster_parameter_group import NeptuneDBClusterParameterGroup


class NeptuneCopyDBClusterParameterGroupResponse(BaseModel):
    DBClusterParameterGroup: NeptuneDBClusterParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

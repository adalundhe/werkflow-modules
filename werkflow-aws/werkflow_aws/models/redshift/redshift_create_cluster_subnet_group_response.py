from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster_subnet_group import RedshiftClusterSubnetGroup


class RedshiftCreateClusterSubnetGroupResponse(BaseModel):
    ClusterSubnetGroup: RedshiftClusterSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

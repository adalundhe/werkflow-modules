from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster_subnet_group import RedshiftClusterSubnetGroup


class RedshiftDescribeClusterSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    ClusterSubnetGroups: list[RedshiftClusterSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

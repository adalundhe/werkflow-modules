from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster_security_group import RedshiftClusterSecurityGroup


class RedshiftDescribeClusterSecurityGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    ClusterSecurityGroups: list[RedshiftClusterSecurityGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None

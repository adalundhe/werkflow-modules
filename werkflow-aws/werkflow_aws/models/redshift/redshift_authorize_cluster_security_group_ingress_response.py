from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster_security_group import RedshiftClusterSecurityGroup


class RedshiftAuthorizeClusterSecurityGroupIngressResponse(BaseModel):
    ClusterSecurityGroup: RedshiftClusterSecurityGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None

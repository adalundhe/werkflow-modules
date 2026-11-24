from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_msk_cluster_cluster_info_details import SecurityHubAwsMskClusterClusterInfoDetails


class SecurityHubAwsMskClusterDetails(BaseModel):
    ClusterInfo: SecurityHubAwsMskClusterClusterInfoDetails | None = None

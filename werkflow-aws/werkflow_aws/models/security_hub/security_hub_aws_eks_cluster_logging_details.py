from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_eks_cluster_logging_cluster_logging_details import SecurityHubAwsEksClusterLoggingClusterLoggingDetails


class SecurityHubAwsEksClusterLoggingDetails(BaseModel):
    ClusterLogging: list[SecurityHubAwsEksClusterLoggingClusterLoggingDetails] | None = None

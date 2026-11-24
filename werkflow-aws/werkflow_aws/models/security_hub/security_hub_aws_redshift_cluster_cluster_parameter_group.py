from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_redshift_cluster_cluster_parameter_status import SecurityHubAwsRedshiftClusterClusterParameterStatus


class SecurityHubAwsRedshiftClusterClusterParameterGroup(BaseModel):
    ClusterParameterStatusList: list[SecurityHubAwsRedshiftClusterClusterParameterStatus] | None = None
    ParameterApplyStatus: StrictStr | None = None
    ParameterGroupName: StrictStr | None = None

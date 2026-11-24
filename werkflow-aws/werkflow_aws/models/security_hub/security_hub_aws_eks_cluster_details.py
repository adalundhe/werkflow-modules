from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_eks_cluster_logging_details import SecurityHubAwsEksClusterLoggingDetails
from .security_hub_aws_eks_cluster_resources_vpc_config_details import SecurityHubAwsEksClusterResourcesVpcConfigDetails


class SecurityHubAwsEksClusterDetails(BaseModel):
    Arn: StrictStr | None = None
    CertificateAuthorityData: StrictStr | None = None
    ClusterStatus: StrictStr | None = None
    Endpoint: StrictStr | None = None
    Name: StrictStr | None = None
    ResourcesVpcConfig: SecurityHubAwsEksClusterResourcesVpcConfigDetails | None = None
    RoleArn: StrictStr | None = None
    Version: StrictStr | None = None
    Logging: SecurityHubAwsEksClusterLoggingDetails | None = None

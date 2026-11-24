from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_msk_cluster_cluster_info_client_authentication_details import SecurityHubAwsMskClusterClusterInfoClientAuthenticationDetails
from .security_hub_aws_msk_cluster_cluster_info_encryption_info_details import SecurityHubAwsMskClusterClusterInfoEncryptionInfoDetails


class SecurityHubAwsMskClusterClusterInfoDetails(BaseModel):
    EncryptionInfo: SecurityHubAwsMskClusterClusterInfoEncryptionInfoDetails | None = None
    CurrentVersion: StrictStr | None = None
    NumberOfBrokerNodes: StrictInt | None = None
    ClusterName: StrictStr | None = None
    ClientAuthentication: SecurityHubAwsMskClusterClusterInfoClientAuthenticationDetails | None = None
    EnhancedMonitoring: StrictStr | None = None

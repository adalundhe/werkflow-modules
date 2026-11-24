from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_open_search_service_domain_cluster_config_zone_awareness_config_details import SecurityHubAwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails


class SecurityHubAwsOpenSearchServiceDomainClusterConfigDetails(BaseModel):
    InstanceCount: StrictInt | None = None
    WarmEnabled: StrictBool | None = None
    WarmCount: StrictInt | None = None
    DedicatedMasterEnabled: StrictBool | None = None
    ZoneAwarenessConfig: SecurityHubAwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails | None = None
    DedicatedMasterCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    WarmType: StrictStr | None = None
    ZoneAwarenessEnabled: StrictBool | None = None
    DedicatedMasterType: StrictStr | None = None

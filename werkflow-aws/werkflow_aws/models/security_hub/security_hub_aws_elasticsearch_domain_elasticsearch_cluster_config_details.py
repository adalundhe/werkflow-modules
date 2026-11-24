from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_elasticsearch_domain_elasticsearch_cluster_config_zone_awareness_config_details import SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails


class SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigDetails(BaseModel):
    DedicatedMasterCount: StrictInt | None = None
    DedicatedMasterEnabled: StrictBool | None = None
    DedicatedMasterType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    ZoneAwarenessConfig: SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails | None = None
    ZoneAwarenessEnabled: StrictBool | None = None

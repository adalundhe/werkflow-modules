from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_elasticsearch_domain_domain_endpoint_options import SecurityHubAwsElasticsearchDomainDomainEndpointOptions
from .security_hub_aws_elasticsearch_domain_elasticsearch_cluster_config_details import SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigDetails
from .security_hub_aws_elasticsearch_domain_encryption_at_rest_options import SecurityHubAwsElasticsearchDomainEncryptionAtRestOptions
from .security_hub_aws_elasticsearch_domain_log_publishing_options import SecurityHubAwsElasticsearchDomainLogPublishingOptions
from .security_hub_aws_elasticsearch_domain_node_to_node_encryption_options import SecurityHubAwsElasticsearchDomainNodeToNodeEncryptionOptions
from .security_hub_aws_elasticsearch_domain_service_software_options import SecurityHubAwsElasticsearchDomainServiceSoftwareOptions
from .security_hub_aws_elasticsearch_domain_vpc_options import SecurityHubAwsElasticsearchDomainVPCOptions


class SecurityHubAwsElasticsearchDomainDetails(BaseModel):
    AccessPolicies: StrictStr | None = None
    DomainEndpointOptions: SecurityHubAwsElasticsearchDomainDomainEndpointOptions | None = None
    DomainId: StrictStr | None = None
    DomainName: StrictStr | None = None
    Endpoint: StrictStr | None = None
    Endpoints: dict[StrictStr, StrictStr] | None = None
    ElasticsearchVersion: StrictStr | None = None
    ElasticsearchClusterConfig: SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigDetails | None = None
    EncryptionAtRestOptions: SecurityHubAwsElasticsearchDomainEncryptionAtRestOptions | None = None
    LogPublishingOptions: SecurityHubAwsElasticsearchDomainLogPublishingOptions | None = None
    NodeToNodeEncryptionOptions: SecurityHubAwsElasticsearchDomainNodeToNodeEncryptionOptions | None = None
    ServiceSoftwareOptions: SecurityHubAwsElasticsearchDomainServiceSoftwareOptions | None = None
    VPCOptions: SecurityHubAwsElasticsearchDomainVPCOptions | None = None

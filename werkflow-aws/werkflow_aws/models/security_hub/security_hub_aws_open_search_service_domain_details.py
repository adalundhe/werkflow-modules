from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_open_search_service_domain_advanced_security_options_details import SecurityHubAwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails
from .security_hub_aws_open_search_service_domain_cluster_config_details import SecurityHubAwsOpenSearchServiceDomainClusterConfigDetails
from .security_hub_aws_open_search_service_domain_domain_endpoint_options_details import SecurityHubAwsOpenSearchServiceDomainDomainEndpointOptionsDetails
from .security_hub_aws_open_search_service_domain_encryption_at_rest_options_details import SecurityHubAwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails
from .security_hub_aws_open_search_service_domain_log_publishing_options_details import SecurityHubAwsOpenSearchServiceDomainLogPublishingOptionsDetails
from .security_hub_aws_open_search_service_domain_node_to_node_encryption_options_details import SecurityHubAwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails
from .security_hub_aws_open_search_service_domain_service_software_options_details import SecurityHubAwsOpenSearchServiceDomainServiceSoftwareOptionsDetails
from .security_hub_aws_open_search_service_domain_vpc_options_details import SecurityHubAwsOpenSearchServiceDomainVpcOptionsDetails


class SecurityHubAwsOpenSearchServiceDomainDetails(BaseModel):
    Arn: StrictStr | None = None
    AccessPolicies: StrictStr | None = None
    DomainName: StrictStr | None = None
    Id: StrictStr | None = None
    DomainEndpoint: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EncryptionAtRestOptions: SecurityHubAwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails | None = None
    NodeToNodeEncryptionOptions: SecurityHubAwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails | None = None
    ServiceSoftwareOptions: SecurityHubAwsOpenSearchServiceDomainServiceSoftwareOptionsDetails | None = None
    ClusterConfig: SecurityHubAwsOpenSearchServiceDomainClusterConfigDetails | None = None
    DomainEndpointOptions: SecurityHubAwsOpenSearchServiceDomainDomainEndpointOptionsDetails | None = None
    VpcOptions: SecurityHubAwsOpenSearchServiceDomainVpcOptionsDetails | None = None
    LogPublishingOptions: SecurityHubAwsOpenSearchServiceDomainLogPublishingOptionsDetails | None = None
    DomainEndpoints: dict[StrictStr, StrictStr] | None = None
    AdvancedSecurityOptions: SecurityHubAwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails | None = None

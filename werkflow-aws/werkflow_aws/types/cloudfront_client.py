from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class CloudFrontClient(ABC):

    @abstractmethod
    def associate_alias(
        self,
        *,
        TargetDistributionId: str,
        Alias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_distribution_tenant_web_acl(
        self,
        *,
        Id: str,
        WebACLArn: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_distribution_web_acl(
        self,
        *,
        Id: str,
        WebACLArn: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_distribution(
        self,
        *,
        PrimaryDistributionId: str,
        CallerReference: str,
        Staging: bool | None = None,
        IfMatch: str | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_anycast_ip_list(
        self,
        *,
        Name: str,
        IpCount: int,
        Tags: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
        IpamCidrConfigs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cache_policy(
        self,
        *,
        CachePolicyConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cloud_front_origin_access_identity(
        self,
        *,
        CloudFrontOriginAccessIdentityConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection_function(
        self,
        *,
        Name: str,
        ConnectionFunctionConfig: dict[str, Any],
        ConnectionFunctionCode: bytes | BinaryIO | str,
        Tags: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection_group(
        self,
        *,
        Name: str,
        Ipv6Enabled: bool | None = None,
        Tags: dict[str, Any] | None = None,
        AnycastIpListId: str | None = None,
        Enabled: bool | None = None,
        ViewerFallback: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_continuous_deployment_policy(
        self,
        *,
        ContinuousDeploymentPolicyConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_distribution(
        self,
        *,
        DistributionConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_distribution_tenant(
        self,
        *,
        DistributionId: str,
        Name: str,
        Domains: list[dict[str, Any]],
        Tags: dict[str, Any] | None = None,
        Customizations: dict[str, Any] | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        ConnectionGroupId: str | None = None,
        ManagedCertificateRequest: dict[str, Any] | None = None,
        Enabled: bool | None = None,
        OnDomainTakeover: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_distribution_with_tags(
        self,
        *,
        DistributionConfigWithTags: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_field_level_encryption_config(
        self,
        *,
        FieldLevelEncryptionConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_field_level_encryption_profile(
        self,
        *,
        FieldLevelEncryptionProfileConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_function(
        self,
        *,
        Name: str,
        FunctionConfig: dict[str, Any],
        FunctionCode: bytes | BinaryIO | str,
        Tags: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_invalidation(
        self,
        *,
        DistributionId: str,
        InvalidationBatch: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_invalidation_for_distribution_tenant(
        self,
        *,
        Id: str,
        InvalidationBatch: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key_group(
        self,
        *,
        KeyGroupConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key_value_store(
        self,
        *,
        Name: str,
        Comment: str | None = None,
        ImportSource: dict[str, Any] | None = None,
        Tags: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_monitoring_subscription(
        self,
        *,
        DistributionId: str,
        MonitoringSubscription: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_origin_access_control(
        self,
        *,
        OriginAccessControlConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_origin_request_policy(
        self,
        *,
        OriginRequestPolicyConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_public_key(
        self,
        *,
        PublicKeyConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_realtime_log_config(
        self,
        *,
        EndPoints: list[dict[str, Any]],
        Fields: list[str],
        Name: str,
        SamplingRate: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_response_headers_policy(
        self,
        *,
        ResponseHeadersPolicyConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_streaming_distribution(
        self,
        *,
        StreamingDistributionConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_streaming_distribution_with_tags(
        self,
        *,
        StreamingDistributionConfigWithTags: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trust_store(
        self,
        *,
        Name: str,
        CaCertificatesBundleSource: dict[str, Any],
        UseClientCertificateOCSPEndpoint: bool | None = None,
        Tags: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_origin(
        self,
        *,
        VpcOriginEndpointConfig: dict[str, Any],
        Tags: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_anycast_ip_list(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_policy(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cloud_front_origin_access_identity(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection_function(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection_group(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_continuous_deployment_policy(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_distribution(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_distribution_tenant(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_field_level_encryption_config(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_field_level_encryption_profile(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function(
        self,
        *,
        Name: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key_group(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key_value_store(
        self,
        *,
        Name: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_monitoring_subscription(
        self,
        *,
        DistributionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_origin_access_control(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_origin_request_policy(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_public_key(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_realtime_log_config(
        self,
        *,
        Name: str | None = None,
        ARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_response_headers_policy(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_streaming_distribution(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trust_store(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_origin(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection_function(
        self,
        *,
        Identifier: str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_function(
        self,
        *,
        Name: str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key_value_store(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_distribution_tenant_web_acl(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_distribution_web_acl(
        self,
        *,
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_anycast_ip_list(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cache_policy(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cache_policy_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cloud_front_origin_access_identity(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cloud_front_origin_access_identity_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection_function(
        self,
        *,
        Identifier: str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection_group(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection_group_by_routing_endpoint(
        self,
        *,
        RoutingEndpoint: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_continuous_deployment_policy(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_continuous_deployment_policy_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_tenant(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_tenant_by_domain(
        self,
        *,
        Domain: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_field_level_encryption(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_field_level_encryption_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_field_level_encryption_profile(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_field_level_encryption_profile_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function(
        self,
        *,
        Name: str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_invalidation(
        self,
        *,
        DistributionId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_invalidation_for_distribution_tenant(
        self,
        *,
        DistributionTenantId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_group(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_group_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_certificate_details(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_monitoring_subscription(
        self,
        *,
        DistributionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_origin_access_control(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_origin_access_control_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_origin_request_policy(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_origin_request_policy_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_public_key(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_public_key_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_realtime_log_config(
        self,
        *,
        Name: str | None = None,
        ARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_response_headers_policy(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_response_headers_policy_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_streaming_distribution(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_streaming_distribution_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trust_store(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_origin(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_anycast_ip_lists(
        self,
        *,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cache_policies(
        self,
        *,
        Type: str | None = None,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cloud_front_origin_access_identities(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_conflicting_aliases(
        self,
        *,
        DistributionId: str,
        Alias: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connection_functions(
        self,
        *,
        Marker: str | None = None,
        MaxItems: int | None = None,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connection_groups(
        self,
        *,
        AssociationFilter: dict[str, Any] | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_continuous_deployment_policies(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distribution_tenants(
        self,
        *,
        AssociationFilter: dict[str, Any] | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distribution_tenants_by_customization(
        self,
        *,
        WebACLArn: str | None = None,
        CertificateArn: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_anycast_ip_list_id(
        self,
        *,
        AnycastIpListId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_cache_policy_id(
        self,
        *,
        CachePolicyId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_connection_function(
        self,
        *,
        ConnectionFunctionIdentifier: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_connection_mode(
        self,
        *,
        ConnectionMode: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_key_group(
        self,
        *,
        KeyGroupId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_origin_request_policy_id(
        self,
        *,
        OriginRequestPolicyId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_owned_resource(
        self,
        *,
        ResourceArn: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_realtime_log_config(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
        RealtimeLogConfigName: str | None = None,
        RealtimeLogConfigArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_response_headers_policy_id(
        self,
        *,
        ResponseHeadersPolicyId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_trust_store(
        self,
        *,
        TrustStoreIdentifier: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_vpc_origin_id(
        self,
        *,
        VpcOriginId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_distributions_by_web_acl_id(
        self,
        *,
        WebACLId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_conflicts(
        self,
        *,
        Domain: str,
        DomainControlValidationResource: dict[str, Any],
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_field_level_encryption_configs(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_field_level_encryption_profiles(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_functions(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invalidations(
        self,
        *,
        DistributionId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invalidations_for_distribution_tenant(
        self,
        *,
        Id: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_key_groups(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_key_value_stores(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_origin_access_controls(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_origin_request_policies(
        self,
        *,
        Type: str | None = None,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_public_keys(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_realtime_log_configs(
        self,
        *,
        MaxItems: str | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_response_headers_policies(
        self,
        *,
        Type: str | None = None,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_streaming_distributions(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        Resource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trust_stores(
        self,
        *,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_origins(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_connection_function(
        self,
        *,
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_function(
        self,
        *,
        Name: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        PolicyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        Resource: str,
        Tags: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_connection_function(
        self,
        *,
        Id: str,
        IfMatch: str,
        ConnectionObject: bytes | BinaryIO | str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_function(
        self,
        *,
        Name: str,
        IfMatch: str,
        EventObject: bytes | BinaryIO | str,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        Resource: str,
        TagKeys: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_anycast_ip_list(
        self,
        *,
        Id: str,
        IfMatch: str,
        IpAddressType: str | None = None,
        IpamCidrConfigs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cache_policy(
        self,
        *,
        CachePolicyConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cloud_front_origin_access_identity(
        self,
        *,
        CloudFrontOriginAccessIdentityConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection_function(
        self,
        *,
        Id: str,
        IfMatch: str,
        ConnectionFunctionConfig: dict[str, Any],
        ConnectionFunctionCode: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection_group(
        self,
        *,
        Id: str,
        IfMatch: str,
        Ipv6Enabled: bool | None = None,
        AnycastIpListId: str | None = None,
        Enabled: bool | None = None,
        ViewerFallback: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_continuous_deployment_policy(
        self,
        *,
        ContinuousDeploymentPolicyConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_distribution(
        self,
        *,
        DistributionConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_distribution_tenant(
        self,
        *,
        Id: str,
        IfMatch: str,
        DistributionId: str | None = None,
        Domains: list[dict[str, Any]] | None = None,
        Customizations: dict[str, Any] | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        ConnectionGroupId: str | None = None,
        ManagedCertificateRequest: dict[str, Any] | None = None,
        Enabled: bool | None = None,
        OnDomainTakeover: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_distribution_with_staging_config(
        self,
        *,
        Id: str,
        StagingDistributionId: str | None = None,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_association(
        self,
        *,
        Domain: str,
        TargetResource: dict[str, Any],
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_field_level_encryption_config(
        self,
        *,
        FieldLevelEncryptionConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_field_level_encryption_profile(
        self,
        *,
        FieldLevelEncryptionProfileConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function(
        self,
        *,
        Name: str,
        IfMatch: str,
        FunctionConfig: dict[str, Any],
        FunctionCode: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_key_group(
        self,
        *,
        KeyGroupConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_key_value_store(
        self,
        *,
        Name: str,
        Comment: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_origin_access_control(
        self,
        *,
        OriginAccessControlConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_origin_request_policy(
        self,
        *,
        OriginRequestPolicyConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_public_key(
        self,
        *,
        PublicKeyConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_realtime_log_config(
        self,
        *,
        EndPoints: list[dict[str, Any]] | None = None,
        Fields: list[str] | None = None,
        Name: str | None = None,
        ARN: str | None = None,
        SamplingRate: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_response_headers_policy(
        self,
        *,
        ResponseHeadersPolicyConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_streaming_distribution(
        self,
        *,
        StreamingDistributionConfig: dict[str, Any],
        Id: str,
        IfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trust_store(
        self,
        *,
        Id: str,
        IfMatch: str,
        CaCertificatesBundleSource: dict[str, Any] | None = None,
        UseClientCertificateOCSPEndpoint: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_origin(
        self,
        *,
        VpcOriginEndpointConfig: dict[str, Any],
        Id: str,
        IfMatch: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_dns_configuration(
        self,
        *,
        Identifier: str,
        Domain: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

from werkflow_aws.models.cloudfront import (
    CloudFrontAssociateAliasRequest,
    CloudFrontAssociateAliasResponse,
    CloudFrontAssociateDistributionTenantWebACLRequest,
    CloudFrontAssociateDistributionTenantWebACLResponse,
    CloudFrontAssociateDistributionWebACLRequest,
    CloudFrontAssociateDistributionWebACLResponse,
    CloudFrontCopyDistributionRequest,
    CloudFrontCopyDistributionResponse,
    CloudFrontCreateAnycastIpListRequest,
    CloudFrontCreateAnycastIpListResponse,
    CloudFrontCreateCachePolicyRequest,
    CloudFrontCreateCachePolicyResponse,
    CloudFrontCreateCloudFrontOriginAccessIdentityRequest,
    CloudFrontCreateCloudFrontOriginAccessIdentityResponse,
    CloudFrontCreateConnectionFunctionRequest,
    CloudFrontCreateConnectionFunctionResponse,
    CloudFrontCreateConnectionGroupRequest,
    CloudFrontCreateConnectionGroupResponse,
    CloudFrontCreateContinuousDeploymentPolicyRequest,
    CloudFrontCreateContinuousDeploymentPolicyResponse,
    CloudFrontCreateDistributionRequest,
    CloudFrontCreateDistributionResponse,
    CloudFrontCreateDistributionTenantRequest,
    CloudFrontCreateDistributionTenantResponse,
    CloudFrontCreateDistributionWithTagsRequest,
    CloudFrontCreateDistributionWithTagsResponse,
    CloudFrontCreateFieldLevelEncryptionConfigRequest,
    CloudFrontCreateFieldLevelEncryptionConfigResponse,
    CloudFrontCreateFieldLevelEncryptionProfileRequest,
    CloudFrontCreateFieldLevelEncryptionProfileResponse,
    CloudFrontCreateFunctionRequest,
    CloudFrontCreateFunctionResponse,
    CloudFrontCreateInvalidationForDistributionTenantRequest,
    CloudFrontCreateInvalidationForDistributionTenantResponse,
    CloudFrontCreateInvalidationRequest,
    CloudFrontCreateInvalidationResponse,
    CloudFrontCreateKeyGroupRequest,
    CloudFrontCreateKeyGroupResponse,
    CloudFrontCreateKeyValueStoreRequest,
    CloudFrontCreateKeyValueStoreResponse,
    CloudFrontCreateMonitoringSubscriptionRequest,
    CloudFrontCreateMonitoringSubscriptionResponse,
    CloudFrontCreateOriginAccessControlRequest,
    CloudFrontCreateOriginAccessControlResponse,
    CloudFrontCreateOriginRequestPolicyRequest,
    CloudFrontCreateOriginRequestPolicyResponse,
    CloudFrontCreatePublicKeyRequest,
    CloudFrontCreatePublicKeyResponse,
    CloudFrontCreateRealtimeLogConfigRequest,
    CloudFrontCreateRealtimeLogConfigResponse,
    CloudFrontCreateResponseHeadersPolicyRequest,
    CloudFrontCreateResponseHeadersPolicyResponse,
    CloudFrontCreateStreamingDistributionRequest,
    CloudFrontCreateStreamingDistributionResponse,
    CloudFrontCreateStreamingDistributionWithTagsRequest,
    CloudFrontCreateStreamingDistributionWithTagsResponse,
    CloudFrontCreateTrustStoreRequest,
    CloudFrontCreateTrustStoreResponse,
    CloudFrontCreateVpcOriginRequest,
    CloudFrontCreateVpcOriginResponse,
    CloudFrontDeleteAnycastIpListRequest,
    CloudFrontDeleteAnycastIpListResponse,
    CloudFrontDeleteCachePolicyRequest,
    CloudFrontDeleteCachePolicyResponse,
    CloudFrontDeleteCloudFrontOriginAccessIdentityRequest,
    CloudFrontDeleteCloudFrontOriginAccessIdentityResponse,
    CloudFrontDeleteConnectionFunctionRequest,
    CloudFrontDeleteConnectionFunctionResponse,
    CloudFrontDeleteConnectionGroupRequest,
    CloudFrontDeleteConnectionGroupResponse,
    CloudFrontDeleteContinuousDeploymentPolicyRequest,
    CloudFrontDeleteContinuousDeploymentPolicyResponse,
    CloudFrontDeleteDistributionRequest,
    CloudFrontDeleteDistributionResponse,
    CloudFrontDeleteDistributionTenantRequest,
    CloudFrontDeleteDistributionTenantResponse,
    CloudFrontDeleteFieldLevelEncryptionConfigRequest,
    CloudFrontDeleteFieldLevelEncryptionConfigResponse,
    CloudFrontDeleteFieldLevelEncryptionProfileRequest,
    CloudFrontDeleteFieldLevelEncryptionProfileResponse,
    CloudFrontDeleteFunctionRequest,
    CloudFrontDeleteFunctionResponse,
    CloudFrontDeleteKeyGroupRequest,
    CloudFrontDeleteKeyGroupResponse,
    CloudFrontDeleteKeyValueStoreRequest,
    CloudFrontDeleteKeyValueStoreResponse,
    CloudFrontDeleteMonitoringSubscriptionRequest,
    CloudFrontDeleteMonitoringSubscriptionResponse,
    CloudFrontDeleteOriginAccessControlRequest,
    CloudFrontDeleteOriginAccessControlResponse,
    CloudFrontDeleteOriginRequestPolicyRequest,
    CloudFrontDeleteOriginRequestPolicyResponse,
    CloudFrontDeletePublicKeyRequest,
    CloudFrontDeletePublicKeyResponse,
    CloudFrontDeleteRealtimeLogConfigRequest,
    CloudFrontDeleteRealtimeLogConfigResponse,
    CloudFrontDeleteResourcePolicyRequest,
    CloudFrontDeleteResourcePolicyResponse,
    CloudFrontDeleteResponseHeadersPolicyRequest,
    CloudFrontDeleteResponseHeadersPolicyResponse,
    CloudFrontDeleteStreamingDistributionRequest,
    CloudFrontDeleteStreamingDistributionResponse,
    CloudFrontDeleteTrustStoreRequest,
    CloudFrontDeleteTrustStoreResponse,
    CloudFrontDeleteVpcOriginRequest,
    CloudFrontDeleteVpcOriginResponse,
    CloudFrontDescribeConnectionFunctionRequest,
    CloudFrontDescribeConnectionFunctionResponse,
    CloudFrontDescribeFunctionRequest,
    CloudFrontDescribeFunctionResponse,
    CloudFrontDescribeKeyValueStoreRequest,
    CloudFrontDescribeKeyValueStoreResponse,
    CloudFrontDisassociateDistributionTenantWebACLRequest,
    CloudFrontDisassociateDistributionTenantWebACLResponse,
    CloudFrontDisassociateDistributionWebACLRequest,
    CloudFrontDisassociateDistributionWebACLResponse,
    CloudFrontGetAnycastIpListRequest,
    CloudFrontGetAnycastIpListResponse,
    CloudFrontGetCachePolicyConfigRequest,
    CloudFrontGetCachePolicyConfigResponse,
    CloudFrontGetCachePolicyRequest,
    CloudFrontGetCachePolicyResponse,
    CloudFrontGetCloudFrontOriginAccessIdentityConfigRequest,
    CloudFrontGetCloudFrontOriginAccessIdentityConfigResponse,
    CloudFrontGetCloudFrontOriginAccessIdentityRequest,
    CloudFrontGetCloudFrontOriginAccessIdentityResponse,
    CloudFrontGetConnectionFunctionRequest,
    CloudFrontGetConnectionFunctionResponse,
    CloudFrontGetConnectionGroupByRoutingEndpointRequest,
    CloudFrontGetConnectionGroupByRoutingEndpointResponse,
    CloudFrontGetConnectionGroupRequest,
    CloudFrontGetConnectionGroupResponse,
    CloudFrontGetContinuousDeploymentPolicyConfigRequest,
    CloudFrontGetContinuousDeploymentPolicyConfigResponse,
    CloudFrontGetContinuousDeploymentPolicyRequest,
    CloudFrontGetContinuousDeploymentPolicyResponse,
    CloudFrontGetDistributionConfigRequest,
    CloudFrontGetDistributionConfigResponse,
    CloudFrontGetDistributionRequest,
    CloudFrontGetDistributionResponse,
    CloudFrontGetDistributionTenantByDomainRequest,
    CloudFrontGetDistributionTenantByDomainResponse,
    CloudFrontGetDistributionTenantRequest,
    CloudFrontGetDistributionTenantResponse,
    CloudFrontGetFieldLevelEncryptionConfigRequest,
    CloudFrontGetFieldLevelEncryptionConfigResponse,
    CloudFrontGetFieldLevelEncryptionProfileConfigRequest,
    CloudFrontGetFieldLevelEncryptionProfileConfigResponse,
    CloudFrontGetFieldLevelEncryptionProfileRequest,
    CloudFrontGetFieldLevelEncryptionProfileResponse,
    CloudFrontGetFieldLevelEncryptionRequest,
    CloudFrontGetFieldLevelEncryptionResponse,
    CloudFrontGetFunctionRequest,
    CloudFrontGetFunctionResponse,
    CloudFrontGetInvalidationForDistributionTenantRequest,
    CloudFrontGetInvalidationForDistributionTenantResponse,
    CloudFrontGetInvalidationRequest,
    CloudFrontGetInvalidationResponse,
    CloudFrontGetKeyGroupConfigRequest,
    CloudFrontGetKeyGroupConfigResponse,
    CloudFrontGetKeyGroupRequest,
    CloudFrontGetKeyGroupResponse,
    CloudFrontGetManagedCertificateDetailsRequest,
    CloudFrontGetManagedCertificateDetailsResponse,
    CloudFrontGetMonitoringSubscriptionRequest,
    CloudFrontGetMonitoringSubscriptionResponse,
    CloudFrontGetOriginAccessControlConfigRequest,
    CloudFrontGetOriginAccessControlConfigResponse,
    CloudFrontGetOriginAccessControlRequest,
    CloudFrontGetOriginAccessControlResponse,
    CloudFrontGetOriginRequestPolicyConfigRequest,
    CloudFrontGetOriginRequestPolicyConfigResponse,
    CloudFrontGetOriginRequestPolicyRequest,
    CloudFrontGetOriginRequestPolicyResponse,
    CloudFrontGetPublicKeyConfigRequest,
    CloudFrontGetPublicKeyConfigResponse,
    CloudFrontGetPublicKeyRequest,
    CloudFrontGetPublicKeyResponse,
    CloudFrontGetRealtimeLogConfigRequest,
    CloudFrontGetRealtimeLogConfigResponse,
    CloudFrontGetResourcePolicyRequest,
    CloudFrontGetResourcePolicyResponse,
    CloudFrontGetResponseHeadersPolicyConfigRequest,
    CloudFrontGetResponseHeadersPolicyConfigResponse,
    CloudFrontGetResponseHeadersPolicyRequest,
    CloudFrontGetResponseHeadersPolicyResponse,
    CloudFrontGetStreamingDistributionConfigRequest,
    CloudFrontGetStreamingDistributionConfigResponse,
    CloudFrontGetStreamingDistributionRequest,
    CloudFrontGetStreamingDistributionResponse,
    CloudFrontGetTrustStoreRequest,
    CloudFrontGetTrustStoreResponse,
    CloudFrontGetVpcOriginRequest,
    CloudFrontGetVpcOriginResponse,
    CloudFrontListAnycastIpListsRequest,
    CloudFrontListAnycastIpListsResponse,
    CloudFrontListCachePoliciesRequest,
    CloudFrontListCachePoliciesResponse,
    CloudFrontListCloudFrontOriginAccessIdentitiesRequest,
    CloudFrontListCloudFrontOriginAccessIdentitiesResponse,
    CloudFrontListConflictingAliasesRequest,
    CloudFrontListConflictingAliasesResponse,
    CloudFrontListConnectionFunctionsRequest,
    CloudFrontListConnectionFunctionsResponse,
    CloudFrontListConnectionGroupsRequest,
    CloudFrontListConnectionGroupsResponse,
    CloudFrontListContinuousDeploymentPoliciesRequest,
    CloudFrontListContinuousDeploymentPoliciesResponse,
    CloudFrontListDistributionTenantsByCustomizationRequest,
    CloudFrontListDistributionTenantsByCustomizationResponse,
    CloudFrontListDistributionTenantsRequest,
    CloudFrontListDistributionTenantsResponse,
    CloudFrontListDistributionsByAnycastIpListIdRequest,
    CloudFrontListDistributionsByAnycastIpListIdResponse,
    CloudFrontListDistributionsByCachePolicyIdRequest,
    CloudFrontListDistributionsByCachePolicyIdResponse,
    CloudFrontListDistributionsByConnectionFunctionRequest,
    CloudFrontListDistributionsByConnectionFunctionResponse,
    CloudFrontListDistributionsByConnectionModeRequest,
    CloudFrontListDistributionsByConnectionModeResponse,
    CloudFrontListDistributionsByKeyGroupRequest,
    CloudFrontListDistributionsByKeyGroupResponse,
    CloudFrontListDistributionsByOriginRequestPolicyIdRequest,
    CloudFrontListDistributionsByOriginRequestPolicyIdResponse,
    CloudFrontListDistributionsByOwnedResourceRequest,
    CloudFrontListDistributionsByOwnedResourceResponse,
    CloudFrontListDistributionsByRealtimeLogConfigRequest,
    CloudFrontListDistributionsByRealtimeLogConfigResponse,
    CloudFrontListDistributionsByResponseHeadersPolicyIdRequest,
    CloudFrontListDistributionsByResponseHeadersPolicyIdResponse,
    CloudFrontListDistributionsByTrustStoreRequest,
    CloudFrontListDistributionsByTrustStoreResponse,
    CloudFrontListDistributionsByVpcOriginIdRequest,
    CloudFrontListDistributionsByVpcOriginIdResponse,
    CloudFrontListDistributionsByWebACLIdRequest,
    CloudFrontListDistributionsByWebACLIdResponse,
    CloudFrontListDistributionsRequest,
    CloudFrontListDistributionsResponse,
    CloudFrontListDomainConflictsRequest,
    CloudFrontListDomainConflictsResponse,
    CloudFrontListFieldLevelEncryptionConfigsRequest,
    CloudFrontListFieldLevelEncryptionConfigsResponse,
    CloudFrontListFieldLevelEncryptionProfilesRequest,
    CloudFrontListFieldLevelEncryptionProfilesResponse,
    CloudFrontListFunctionsRequest,
    CloudFrontListFunctionsResponse,
    CloudFrontListInvalidationsForDistributionTenantRequest,
    CloudFrontListInvalidationsForDistributionTenantResponse,
    CloudFrontListInvalidationsRequest,
    CloudFrontListInvalidationsResponse,
    CloudFrontListKeyGroupsRequest,
    CloudFrontListKeyGroupsResponse,
    CloudFrontListKeyValueStoresRequest,
    CloudFrontListKeyValueStoresResponse,
    CloudFrontListOriginAccessControlsRequest,
    CloudFrontListOriginAccessControlsResponse,
    CloudFrontListOriginRequestPoliciesRequest,
    CloudFrontListOriginRequestPoliciesResponse,
    CloudFrontListPublicKeysRequest,
    CloudFrontListPublicKeysResponse,
    CloudFrontListRealtimeLogConfigsRequest,
    CloudFrontListRealtimeLogConfigsResponse,
    CloudFrontListResponseHeadersPoliciesRequest,
    CloudFrontListResponseHeadersPoliciesResponse,
    CloudFrontListStreamingDistributionsRequest,
    CloudFrontListStreamingDistributionsResponse,
    CloudFrontListTagsForResourceRequest,
    CloudFrontListTagsForResourceResponse,
    CloudFrontListTrustStoresRequest,
    CloudFrontListTrustStoresResponse,
    CloudFrontListVpcOriginsRequest,
    CloudFrontListVpcOriginsResponse,
    CloudFrontPublishConnectionFunctionRequest,
    CloudFrontPublishConnectionFunctionResponse,
    CloudFrontPublishFunctionRequest,
    CloudFrontPublishFunctionResponse,
    CloudFrontPutResourcePolicyRequest,
    CloudFrontPutResourcePolicyResponse,
    CloudFrontTagResourceRequest,
    CloudFrontTagResourceResponse,
    CloudFrontTestConnectionFunctionRequest,
    CloudFrontTestConnectionFunctionResponse,
    CloudFrontTestFunctionRequest,
    CloudFrontTestFunctionResponse,
    CloudFrontUntagResourceRequest,
    CloudFrontUntagResourceResponse,
    CloudFrontUpdateAnycastIpListRequest,
    CloudFrontUpdateAnycastIpListResponse,
    CloudFrontUpdateCachePolicyRequest,
    CloudFrontUpdateCachePolicyResponse,
    CloudFrontUpdateCloudFrontOriginAccessIdentityRequest,
    CloudFrontUpdateCloudFrontOriginAccessIdentityResponse,
    CloudFrontUpdateConnectionFunctionRequest,
    CloudFrontUpdateConnectionFunctionResponse,
    CloudFrontUpdateConnectionGroupRequest,
    CloudFrontUpdateConnectionGroupResponse,
    CloudFrontUpdateContinuousDeploymentPolicyRequest,
    CloudFrontUpdateContinuousDeploymentPolicyResponse,
    CloudFrontUpdateDistributionRequest,
    CloudFrontUpdateDistributionResponse,
    CloudFrontUpdateDistributionTenantRequest,
    CloudFrontUpdateDistributionTenantResponse,
    CloudFrontUpdateDistributionWithStagingConfigRequest,
    CloudFrontUpdateDistributionWithStagingConfigResponse,
    CloudFrontUpdateDomainAssociationRequest,
    CloudFrontUpdateDomainAssociationResponse,
    CloudFrontUpdateFieldLevelEncryptionConfigRequest,
    CloudFrontUpdateFieldLevelEncryptionConfigResponse,
    CloudFrontUpdateFieldLevelEncryptionProfileRequest,
    CloudFrontUpdateFieldLevelEncryptionProfileResponse,
    CloudFrontUpdateFunctionRequest,
    CloudFrontUpdateFunctionResponse,
    CloudFrontUpdateKeyGroupRequest,
    CloudFrontUpdateKeyGroupResponse,
    CloudFrontUpdateKeyValueStoreRequest,
    CloudFrontUpdateKeyValueStoreResponse,
    CloudFrontUpdateOriginAccessControlRequest,
    CloudFrontUpdateOriginAccessControlResponse,
    CloudFrontUpdateOriginRequestPolicyRequest,
    CloudFrontUpdateOriginRequestPolicyResponse,
    CloudFrontUpdatePublicKeyRequest,
    CloudFrontUpdatePublicKeyResponse,
    CloudFrontUpdateRealtimeLogConfigRequest,
    CloudFrontUpdateRealtimeLogConfigResponse,
    CloudFrontUpdateResponseHeadersPolicyRequest,
    CloudFrontUpdateResponseHeadersPolicyResponse,
    CloudFrontUpdateStreamingDistributionRequest,
    CloudFrontUpdateStreamingDistributionResponse,
    CloudFrontUpdateTrustStoreRequest,
    CloudFrontUpdateTrustStoreResponse,
    CloudFrontUpdateVpcOriginRequest,
    CloudFrontUpdateVpcOriginResponse,
    CloudFrontVerifyDnsConfigurationRequest,
    CloudFrontVerifyDnsConfigurationResponse,
)
from werkflow_aws.types.cloudfront_client import CloudFrontClient
from .base import AWSBaseService


class AWSCloudFront(AWSBaseService[CloudFrontClient]):
    service_name = 'cloudfront'
    boto3_service_name = 'cloudfront'

    def __init__(self) -> None:
        super().__init__(service_name='cloudfront', boto3_service_name='cloudfront')

    async def associate_alias(
        self,
        request: CloudFrontAssociateAliasRequest,
    ) -> CloudFrontAssociateAliasResponse:
        client = self._require_client()
        return await self._execute(client.associate_alias, request, CloudFrontAssociateAliasResponse)

    async def associate_distribution_tenant_web_acl(
        self,
        request: CloudFrontAssociateDistributionTenantWebACLRequest,
    ) -> CloudFrontAssociateDistributionTenantWebACLResponse:
        client = self._require_client()
        return await self._execute(client.associate_distribution_tenant_web_acl, request, CloudFrontAssociateDistributionTenantWebACLResponse)

    async def associate_distribution_web_acl(
        self,
        request: CloudFrontAssociateDistributionWebACLRequest,
    ) -> CloudFrontAssociateDistributionWebACLResponse:
        client = self._require_client()
        return await self._execute(client.associate_distribution_web_acl, request, CloudFrontAssociateDistributionWebACLResponse)

    async def copy_distribution(
        self,
        request: CloudFrontCopyDistributionRequest,
    ) -> CloudFrontCopyDistributionResponse:
        client = self._require_client()
        return await self._execute(client.copy_distribution, request, CloudFrontCopyDistributionResponse)

    async def create_anycast_ip_list(
        self,
        request: CloudFrontCreateAnycastIpListRequest,
    ) -> CloudFrontCreateAnycastIpListResponse:
        client = self._require_client()
        return await self._execute(client.create_anycast_ip_list, request, CloudFrontCreateAnycastIpListResponse)

    async def create_cache_policy(
        self,
        request: CloudFrontCreateCachePolicyRequest,
    ) -> CloudFrontCreateCachePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_cache_policy, request, CloudFrontCreateCachePolicyResponse)

    async def create_cloud_front_origin_access_identity(
        self,
        request: CloudFrontCreateCloudFrontOriginAccessIdentityRequest,
    ) -> CloudFrontCreateCloudFrontOriginAccessIdentityResponse:
        client = self._require_client()
        return await self._execute(client.create_cloud_front_origin_access_identity, request, CloudFrontCreateCloudFrontOriginAccessIdentityResponse)

    async def create_connection_function(
        self,
        request: CloudFrontCreateConnectionFunctionRequest,
    ) -> CloudFrontCreateConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection_function, request, CloudFrontCreateConnectionFunctionResponse)

    async def create_connection_group(
        self,
        request: CloudFrontCreateConnectionGroupRequest,
    ) -> CloudFrontCreateConnectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_connection_group, request, CloudFrontCreateConnectionGroupResponse)

    async def create_continuous_deployment_policy(
        self,
        request: CloudFrontCreateContinuousDeploymentPolicyRequest,
    ) -> CloudFrontCreateContinuousDeploymentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_continuous_deployment_policy, request, CloudFrontCreateContinuousDeploymentPolicyResponse)

    async def create_distribution(
        self,
        request: CloudFrontCreateDistributionRequest,
    ) -> CloudFrontCreateDistributionResponse:
        client = self._require_client()
        return await self._execute(client.create_distribution, request, CloudFrontCreateDistributionResponse)

    async def create_distribution_tenant(
        self,
        request: CloudFrontCreateDistributionTenantRequest,
    ) -> CloudFrontCreateDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.create_distribution_tenant, request, CloudFrontCreateDistributionTenantResponse)

    async def create_distribution_with_tags(
        self,
        request: CloudFrontCreateDistributionWithTagsRequest,
    ) -> CloudFrontCreateDistributionWithTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_distribution_with_tags, request, CloudFrontCreateDistributionWithTagsResponse)

    async def create_field_level_encryption_config(
        self,
        request: CloudFrontCreateFieldLevelEncryptionConfigRequest,
    ) -> CloudFrontCreateFieldLevelEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_field_level_encryption_config, request, CloudFrontCreateFieldLevelEncryptionConfigResponse)

    async def create_field_level_encryption_profile(
        self,
        request: CloudFrontCreateFieldLevelEncryptionProfileRequest,
    ) -> CloudFrontCreateFieldLevelEncryptionProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_field_level_encryption_profile, request, CloudFrontCreateFieldLevelEncryptionProfileResponse)

    async def create_function(
        self,
        request: CloudFrontCreateFunctionRequest,
    ) -> CloudFrontCreateFunctionResponse:
        client = self._require_client()
        return await self._execute(client.create_function, request, CloudFrontCreateFunctionResponse)

    async def create_invalidation(
        self,
        request: CloudFrontCreateInvalidationRequest,
    ) -> CloudFrontCreateInvalidationResponse:
        client = self._require_client()
        return await self._execute(client.create_invalidation, request, CloudFrontCreateInvalidationResponse)

    async def create_invalidation_for_distribution_tenant(
        self,
        request: CloudFrontCreateInvalidationForDistributionTenantRequest,
    ) -> CloudFrontCreateInvalidationForDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.create_invalidation_for_distribution_tenant, request, CloudFrontCreateInvalidationForDistributionTenantResponse)

    async def create_key_group(
        self,
        request: CloudFrontCreateKeyGroupRequest,
    ) -> CloudFrontCreateKeyGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_key_group, request, CloudFrontCreateKeyGroupResponse)

    async def create_key_value_store(
        self,
        request: CloudFrontCreateKeyValueStoreRequest,
    ) -> CloudFrontCreateKeyValueStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_key_value_store, request, CloudFrontCreateKeyValueStoreResponse)

    async def create_monitoring_subscription(
        self,
        request: CloudFrontCreateMonitoringSubscriptionRequest,
    ) -> CloudFrontCreateMonitoringSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_monitoring_subscription, request, CloudFrontCreateMonitoringSubscriptionResponse)

    async def create_origin_access_control(
        self,
        request: CloudFrontCreateOriginAccessControlRequest,
    ) -> CloudFrontCreateOriginAccessControlResponse:
        client = self._require_client()
        return await self._execute(client.create_origin_access_control, request, CloudFrontCreateOriginAccessControlResponse)

    async def create_origin_request_policy(
        self,
        request: CloudFrontCreateOriginRequestPolicyRequest,
    ) -> CloudFrontCreateOriginRequestPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_origin_request_policy, request, CloudFrontCreateOriginRequestPolicyResponse)

    async def create_public_key(
        self,
        request: CloudFrontCreatePublicKeyRequest,
    ) -> CloudFrontCreatePublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_public_key, request, CloudFrontCreatePublicKeyResponse)

    async def create_realtime_log_config(
        self,
        request: CloudFrontCreateRealtimeLogConfigRequest,
    ) -> CloudFrontCreateRealtimeLogConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_realtime_log_config, request, CloudFrontCreateRealtimeLogConfigResponse)

    async def create_response_headers_policy(
        self,
        request: CloudFrontCreateResponseHeadersPolicyRequest,
    ) -> CloudFrontCreateResponseHeadersPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_response_headers_policy, request, CloudFrontCreateResponseHeadersPolicyResponse)

    async def create_streaming_distribution(
        self,
        request: CloudFrontCreateStreamingDistributionRequest,
    ) -> CloudFrontCreateStreamingDistributionResponse:
        client = self._require_client()
        return await self._execute(client.create_streaming_distribution, request, CloudFrontCreateStreamingDistributionResponse)

    async def create_streaming_distribution_with_tags(
        self,
        request: CloudFrontCreateStreamingDistributionWithTagsRequest,
    ) -> CloudFrontCreateStreamingDistributionWithTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_streaming_distribution_with_tags, request, CloudFrontCreateStreamingDistributionWithTagsResponse)

    async def create_trust_store(
        self,
        request: CloudFrontCreateTrustStoreRequest,
    ) -> CloudFrontCreateTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_trust_store, request, CloudFrontCreateTrustStoreResponse)

    async def create_vpc_origin(
        self,
        request: CloudFrontCreateVpcOriginRequest,
    ) -> CloudFrontCreateVpcOriginResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_origin, request, CloudFrontCreateVpcOriginResponse)

    async def delete_anycast_ip_list(
        self,
        request: CloudFrontDeleteAnycastIpListRequest,
    ) -> CloudFrontDeleteAnycastIpListResponse:
        client = self._require_client()
        return await self._execute(client.delete_anycast_ip_list, request, CloudFrontDeleteAnycastIpListResponse)

    async def delete_cache_policy(
        self,
        request: CloudFrontDeleteCachePolicyRequest,
    ) -> CloudFrontDeleteCachePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_cache_policy, request, CloudFrontDeleteCachePolicyResponse)

    async def delete_cloud_front_origin_access_identity(
        self,
        request: CloudFrontDeleteCloudFrontOriginAccessIdentityRequest,
    ) -> CloudFrontDeleteCloudFrontOriginAccessIdentityResponse:
        client = self._require_client()
        return await self._execute(client.delete_cloud_front_origin_access_identity, request, CloudFrontDeleteCloudFrontOriginAccessIdentityResponse)

    async def delete_connection_function(
        self,
        request: CloudFrontDeleteConnectionFunctionRequest,
    ) -> CloudFrontDeleteConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection_function, request, CloudFrontDeleteConnectionFunctionResponse)

    async def delete_connection_group(
        self,
        request: CloudFrontDeleteConnectionGroupRequest,
    ) -> CloudFrontDeleteConnectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection_group, request, CloudFrontDeleteConnectionGroupResponse)

    async def delete_continuous_deployment_policy(
        self,
        request: CloudFrontDeleteContinuousDeploymentPolicyRequest,
    ) -> CloudFrontDeleteContinuousDeploymentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_continuous_deployment_policy, request, CloudFrontDeleteContinuousDeploymentPolicyResponse)

    async def delete_distribution(
        self,
        request: CloudFrontDeleteDistributionRequest,
    ) -> CloudFrontDeleteDistributionResponse:
        client = self._require_client()
        return await self._execute(client.delete_distribution, request, CloudFrontDeleteDistributionResponse)

    async def delete_distribution_tenant(
        self,
        request: CloudFrontDeleteDistributionTenantRequest,
    ) -> CloudFrontDeleteDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.delete_distribution_tenant, request, CloudFrontDeleteDistributionTenantResponse)

    async def delete_field_level_encryption_config(
        self,
        request: CloudFrontDeleteFieldLevelEncryptionConfigRequest,
    ) -> CloudFrontDeleteFieldLevelEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_field_level_encryption_config, request, CloudFrontDeleteFieldLevelEncryptionConfigResponse)

    async def delete_field_level_encryption_profile(
        self,
        request: CloudFrontDeleteFieldLevelEncryptionProfileRequest,
    ) -> CloudFrontDeleteFieldLevelEncryptionProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_field_level_encryption_profile, request, CloudFrontDeleteFieldLevelEncryptionProfileResponse)

    async def delete_function(
        self,
        request: CloudFrontDeleteFunctionRequest,
    ) -> CloudFrontDeleteFunctionResponse:
        client = self._require_client()
        return await self._execute(client.delete_function, request, CloudFrontDeleteFunctionResponse)

    async def delete_key_group(
        self,
        request: CloudFrontDeleteKeyGroupRequest,
    ) -> CloudFrontDeleteKeyGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_key_group, request, CloudFrontDeleteKeyGroupResponse)

    async def delete_key_value_store(
        self,
        request: CloudFrontDeleteKeyValueStoreRequest,
    ) -> CloudFrontDeleteKeyValueStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_key_value_store, request, CloudFrontDeleteKeyValueStoreResponse)

    async def delete_monitoring_subscription(
        self,
        request: CloudFrontDeleteMonitoringSubscriptionRequest,
    ) -> CloudFrontDeleteMonitoringSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_monitoring_subscription, request, CloudFrontDeleteMonitoringSubscriptionResponse)

    async def delete_origin_access_control(
        self,
        request: CloudFrontDeleteOriginAccessControlRequest,
    ) -> CloudFrontDeleteOriginAccessControlResponse:
        client = self._require_client()
        return await self._execute(client.delete_origin_access_control, request, CloudFrontDeleteOriginAccessControlResponse)

    async def delete_origin_request_policy(
        self,
        request: CloudFrontDeleteOriginRequestPolicyRequest,
    ) -> CloudFrontDeleteOriginRequestPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_origin_request_policy, request, CloudFrontDeleteOriginRequestPolicyResponse)

    async def delete_public_key(
        self,
        request: CloudFrontDeletePublicKeyRequest,
    ) -> CloudFrontDeletePublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_public_key, request, CloudFrontDeletePublicKeyResponse)

    async def delete_realtime_log_config(
        self,
        request: CloudFrontDeleteRealtimeLogConfigRequest | None = None,
    ) -> CloudFrontDeleteRealtimeLogConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_realtime_log_config, request, CloudFrontDeleteRealtimeLogConfigResponse)

    async def delete_resource_policy(
        self,
        request: CloudFrontDeleteResourcePolicyRequest,
    ) -> CloudFrontDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, CloudFrontDeleteResourcePolicyResponse)

    async def delete_response_headers_policy(
        self,
        request: CloudFrontDeleteResponseHeadersPolicyRequest,
    ) -> CloudFrontDeleteResponseHeadersPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_response_headers_policy, request, CloudFrontDeleteResponseHeadersPolicyResponse)

    async def delete_streaming_distribution(
        self,
        request: CloudFrontDeleteStreamingDistributionRequest,
    ) -> CloudFrontDeleteStreamingDistributionResponse:
        client = self._require_client()
        return await self._execute(client.delete_streaming_distribution, request, CloudFrontDeleteStreamingDistributionResponse)

    async def delete_trust_store(
        self,
        request: CloudFrontDeleteTrustStoreRequest,
    ) -> CloudFrontDeleteTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_trust_store, request, CloudFrontDeleteTrustStoreResponse)

    async def delete_vpc_origin(
        self,
        request: CloudFrontDeleteVpcOriginRequest,
    ) -> CloudFrontDeleteVpcOriginResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_origin, request, CloudFrontDeleteVpcOriginResponse)

    async def describe_connection_function(
        self,
        request: CloudFrontDescribeConnectionFunctionRequest,
    ) -> CloudFrontDescribeConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection_function, request, CloudFrontDescribeConnectionFunctionResponse)

    async def describe_function(
        self,
        request: CloudFrontDescribeFunctionRequest,
    ) -> CloudFrontDescribeFunctionResponse:
        client = self._require_client()
        return await self._execute(client.describe_function, request, CloudFrontDescribeFunctionResponse)

    async def describe_key_value_store(
        self,
        request: CloudFrontDescribeKeyValueStoreRequest,
    ) -> CloudFrontDescribeKeyValueStoreResponse:
        client = self._require_client()
        return await self._execute(client.describe_key_value_store, request, CloudFrontDescribeKeyValueStoreResponse)

    async def disassociate_distribution_tenant_web_acl(
        self,
        request: CloudFrontDisassociateDistributionTenantWebACLRequest,
    ) -> CloudFrontDisassociateDistributionTenantWebACLResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_distribution_tenant_web_acl, request, CloudFrontDisassociateDistributionTenantWebACLResponse)

    async def disassociate_distribution_web_acl(
        self,
        request: CloudFrontDisassociateDistributionWebACLRequest,
    ) -> CloudFrontDisassociateDistributionWebACLResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_distribution_web_acl, request, CloudFrontDisassociateDistributionWebACLResponse)

    async def get_anycast_ip_list(
        self,
        request: CloudFrontGetAnycastIpListRequest,
    ) -> CloudFrontGetAnycastIpListResponse:
        client = self._require_client()
        return await self._execute(client.get_anycast_ip_list, request, CloudFrontGetAnycastIpListResponse)

    async def get_cache_policy(
        self,
        request: CloudFrontGetCachePolicyRequest,
    ) -> CloudFrontGetCachePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_cache_policy, request, CloudFrontGetCachePolicyResponse)

    async def get_cache_policy_config(
        self,
        request: CloudFrontGetCachePolicyConfigRequest,
    ) -> CloudFrontGetCachePolicyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_cache_policy_config, request, CloudFrontGetCachePolicyConfigResponse)

    async def get_cloud_front_origin_access_identity(
        self,
        request: CloudFrontGetCloudFrontOriginAccessIdentityRequest,
    ) -> CloudFrontGetCloudFrontOriginAccessIdentityResponse:
        client = self._require_client()
        return await self._execute(client.get_cloud_front_origin_access_identity, request, CloudFrontGetCloudFrontOriginAccessIdentityResponse)

    async def get_cloud_front_origin_access_identity_config(
        self,
        request: CloudFrontGetCloudFrontOriginAccessIdentityConfigRequest,
    ) -> CloudFrontGetCloudFrontOriginAccessIdentityConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_cloud_front_origin_access_identity_config, request, CloudFrontGetCloudFrontOriginAccessIdentityConfigResponse)

    async def get_connection_function(
        self,
        request: CloudFrontGetConnectionFunctionRequest,
    ) -> CloudFrontGetConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.get_connection_function, request, CloudFrontGetConnectionFunctionResponse)

    async def get_connection_group(
        self,
        request: CloudFrontGetConnectionGroupRequest,
    ) -> CloudFrontGetConnectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_connection_group, request, CloudFrontGetConnectionGroupResponse)

    async def get_connection_group_by_routing_endpoint(
        self,
        request: CloudFrontGetConnectionGroupByRoutingEndpointRequest,
    ) -> CloudFrontGetConnectionGroupByRoutingEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_connection_group_by_routing_endpoint, request, CloudFrontGetConnectionGroupByRoutingEndpointResponse)

    async def get_continuous_deployment_policy(
        self,
        request: CloudFrontGetContinuousDeploymentPolicyRequest,
    ) -> CloudFrontGetContinuousDeploymentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_continuous_deployment_policy, request, CloudFrontGetContinuousDeploymentPolicyResponse)

    async def get_continuous_deployment_policy_config(
        self,
        request: CloudFrontGetContinuousDeploymentPolicyConfigRequest,
    ) -> CloudFrontGetContinuousDeploymentPolicyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_continuous_deployment_policy_config, request, CloudFrontGetContinuousDeploymentPolicyConfigResponse)

    async def get_distribution(
        self,
        request: CloudFrontGetDistributionRequest,
    ) -> CloudFrontGetDistributionResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution, request, CloudFrontGetDistributionResponse)

    async def get_distribution_config(
        self,
        request: CloudFrontGetDistributionConfigRequest,
    ) -> CloudFrontGetDistributionConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_config, request, CloudFrontGetDistributionConfigResponse)

    async def get_distribution_tenant(
        self,
        request: CloudFrontGetDistributionTenantRequest,
    ) -> CloudFrontGetDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_tenant, request, CloudFrontGetDistributionTenantResponse)

    async def get_distribution_tenant_by_domain(
        self,
        request: CloudFrontGetDistributionTenantByDomainRequest,
    ) -> CloudFrontGetDistributionTenantByDomainResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_tenant_by_domain, request, CloudFrontGetDistributionTenantByDomainResponse)

    async def get_field_level_encryption(
        self,
        request: CloudFrontGetFieldLevelEncryptionRequest,
    ) -> CloudFrontGetFieldLevelEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.get_field_level_encryption, request, CloudFrontGetFieldLevelEncryptionResponse)

    async def get_field_level_encryption_config(
        self,
        request: CloudFrontGetFieldLevelEncryptionConfigRequest,
    ) -> CloudFrontGetFieldLevelEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_field_level_encryption_config, request, CloudFrontGetFieldLevelEncryptionConfigResponse)

    async def get_field_level_encryption_profile(
        self,
        request: CloudFrontGetFieldLevelEncryptionProfileRequest,
    ) -> CloudFrontGetFieldLevelEncryptionProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_field_level_encryption_profile, request, CloudFrontGetFieldLevelEncryptionProfileResponse)

    async def get_field_level_encryption_profile_config(
        self,
        request: CloudFrontGetFieldLevelEncryptionProfileConfigRequest,
    ) -> CloudFrontGetFieldLevelEncryptionProfileConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_field_level_encryption_profile_config, request, CloudFrontGetFieldLevelEncryptionProfileConfigResponse)

    async def get_function(
        self,
        request: CloudFrontGetFunctionRequest,
    ) -> CloudFrontGetFunctionResponse:
        client = self._require_client()
        return await self._execute(client.get_function, request, CloudFrontGetFunctionResponse)

    async def get_invalidation(
        self,
        request: CloudFrontGetInvalidationRequest,
    ) -> CloudFrontGetInvalidationResponse:
        client = self._require_client()
        return await self._execute(client.get_invalidation, request, CloudFrontGetInvalidationResponse)

    async def get_invalidation_for_distribution_tenant(
        self,
        request: CloudFrontGetInvalidationForDistributionTenantRequest,
    ) -> CloudFrontGetInvalidationForDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.get_invalidation_for_distribution_tenant, request, CloudFrontGetInvalidationForDistributionTenantResponse)

    async def get_key_group(
        self,
        request: CloudFrontGetKeyGroupRequest,
    ) -> CloudFrontGetKeyGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_key_group, request, CloudFrontGetKeyGroupResponse)

    async def get_key_group_config(
        self,
        request: CloudFrontGetKeyGroupConfigRequest,
    ) -> CloudFrontGetKeyGroupConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_key_group_config, request, CloudFrontGetKeyGroupConfigResponse)

    async def get_managed_certificate_details(
        self,
        request: CloudFrontGetManagedCertificateDetailsRequest,
    ) -> CloudFrontGetManagedCertificateDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_certificate_details, request, CloudFrontGetManagedCertificateDetailsResponse)

    async def get_monitoring_subscription(
        self,
        request: CloudFrontGetMonitoringSubscriptionRequest,
    ) -> CloudFrontGetMonitoringSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.get_monitoring_subscription, request, CloudFrontGetMonitoringSubscriptionResponse)

    async def get_origin_access_control(
        self,
        request: CloudFrontGetOriginAccessControlRequest,
    ) -> CloudFrontGetOriginAccessControlResponse:
        client = self._require_client()
        return await self._execute(client.get_origin_access_control, request, CloudFrontGetOriginAccessControlResponse)

    async def get_origin_access_control_config(
        self,
        request: CloudFrontGetOriginAccessControlConfigRequest,
    ) -> CloudFrontGetOriginAccessControlConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_origin_access_control_config, request, CloudFrontGetOriginAccessControlConfigResponse)

    async def get_origin_request_policy(
        self,
        request: CloudFrontGetOriginRequestPolicyRequest,
    ) -> CloudFrontGetOriginRequestPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_origin_request_policy, request, CloudFrontGetOriginRequestPolicyResponse)

    async def get_origin_request_policy_config(
        self,
        request: CloudFrontGetOriginRequestPolicyConfigRequest,
    ) -> CloudFrontGetOriginRequestPolicyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_origin_request_policy_config, request, CloudFrontGetOriginRequestPolicyConfigResponse)

    async def get_public_key(
        self,
        request: CloudFrontGetPublicKeyRequest,
    ) -> CloudFrontGetPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_public_key, request, CloudFrontGetPublicKeyResponse)

    async def get_public_key_config(
        self,
        request: CloudFrontGetPublicKeyConfigRequest,
    ) -> CloudFrontGetPublicKeyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_public_key_config, request, CloudFrontGetPublicKeyConfigResponse)

    async def get_realtime_log_config(
        self,
        request: CloudFrontGetRealtimeLogConfigRequest | None = None,
    ) -> CloudFrontGetRealtimeLogConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_realtime_log_config, request, CloudFrontGetRealtimeLogConfigResponse)

    async def get_resource_policy(
        self,
        request: CloudFrontGetResourcePolicyRequest,
    ) -> CloudFrontGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, CloudFrontGetResourcePolicyResponse)

    async def get_response_headers_policy(
        self,
        request: CloudFrontGetResponseHeadersPolicyRequest,
    ) -> CloudFrontGetResponseHeadersPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_response_headers_policy, request, CloudFrontGetResponseHeadersPolicyResponse)

    async def get_response_headers_policy_config(
        self,
        request: CloudFrontGetResponseHeadersPolicyConfigRequest,
    ) -> CloudFrontGetResponseHeadersPolicyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_response_headers_policy_config, request, CloudFrontGetResponseHeadersPolicyConfigResponse)

    async def get_streaming_distribution(
        self,
        request: CloudFrontGetStreamingDistributionRequest,
    ) -> CloudFrontGetStreamingDistributionResponse:
        client = self._require_client()
        return await self._execute(client.get_streaming_distribution, request, CloudFrontGetStreamingDistributionResponse)

    async def get_streaming_distribution_config(
        self,
        request: CloudFrontGetStreamingDistributionConfigRequest,
    ) -> CloudFrontGetStreamingDistributionConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_streaming_distribution_config, request, CloudFrontGetStreamingDistributionConfigResponse)

    async def get_trust_store(
        self,
        request: CloudFrontGetTrustStoreRequest,
    ) -> CloudFrontGetTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.get_trust_store, request, CloudFrontGetTrustStoreResponse)

    async def get_vpc_origin(
        self,
        request: CloudFrontGetVpcOriginRequest,
    ) -> CloudFrontGetVpcOriginResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_origin, request, CloudFrontGetVpcOriginResponse)

    async def list_anycast_ip_lists(
        self,
        request: CloudFrontListAnycastIpListsRequest | None = None,
    ) -> CloudFrontListAnycastIpListsResponse:
        client = self._require_client()
        return await self._execute(client.list_anycast_ip_lists, request, CloudFrontListAnycastIpListsResponse)

    async def list_cache_policies(
        self,
        request: CloudFrontListCachePoliciesRequest | None = None,
    ) -> CloudFrontListCachePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_cache_policies, request, CloudFrontListCachePoliciesResponse)

    async def list_cloud_front_origin_access_identities(
        self,
        request: CloudFrontListCloudFrontOriginAccessIdentitiesRequest | None = None,
    ) -> CloudFrontListCloudFrontOriginAccessIdentitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_cloud_front_origin_access_identities, request, CloudFrontListCloudFrontOriginAccessIdentitiesResponse)

    async def list_cloud_front_origin_access_identities_paginated(
        self,
        request: CloudFrontListCloudFrontOriginAccessIdentitiesRequest | None = None,
    ) -> list[CloudFrontListCloudFrontOriginAccessIdentitiesResponse]:
        return await self._paginate('list_cloud_front_origin_access_identities', request, CloudFrontListCloudFrontOriginAccessIdentitiesResponse)

    async def list_conflicting_aliases(
        self,
        request: CloudFrontListConflictingAliasesRequest,
    ) -> CloudFrontListConflictingAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_conflicting_aliases, request, CloudFrontListConflictingAliasesResponse)

    async def list_connection_functions(
        self,
        request: CloudFrontListConnectionFunctionsRequest | None = None,
    ) -> CloudFrontListConnectionFunctionsResponse:
        client = self._require_client()
        return await self._execute(client.list_connection_functions, request, CloudFrontListConnectionFunctionsResponse)

    async def list_connection_functions_paginated(
        self,
        request: CloudFrontListConnectionFunctionsRequest | None = None,
    ) -> list[CloudFrontListConnectionFunctionsResponse]:
        return await self._paginate('list_connection_functions', request, CloudFrontListConnectionFunctionsResponse)

    async def list_connection_groups(
        self,
        request: CloudFrontListConnectionGroupsRequest | None = None,
    ) -> CloudFrontListConnectionGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_connection_groups, request, CloudFrontListConnectionGroupsResponse)

    async def list_connection_groups_paginated(
        self,
        request: CloudFrontListConnectionGroupsRequest | None = None,
    ) -> list[CloudFrontListConnectionGroupsResponse]:
        return await self._paginate('list_connection_groups', request, CloudFrontListConnectionGroupsResponse)

    async def list_continuous_deployment_policies(
        self,
        request: CloudFrontListContinuousDeploymentPoliciesRequest | None = None,
    ) -> CloudFrontListContinuousDeploymentPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_continuous_deployment_policies, request, CloudFrontListContinuousDeploymentPoliciesResponse)

    async def list_distribution_tenants(
        self,
        request: CloudFrontListDistributionTenantsRequest | None = None,
    ) -> CloudFrontListDistributionTenantsResponse:
        client = self._require_client()
        return await self._execute(client.list_distribution_tenants, request, CloudFrontListDistributionTenantsResponse)

    async def list_distribution_tenants_paginated(
        self,
        request: CloudFrontListDistributionTenantsRequest | None = None,
    ) -> list[CloudFrontListDistributionTenantsResponse]:
        return await self._paginate('list_distribution_tenants', request, CloudFrontListDistributionTenantsResponse)

    async def list_distribution_tenants_by_customization(
        self,
        request: CloudFrontListDistributionTenantsByCustomizationRequest | None = None,
    ) -> CloudFrontListDistributionTenantsByCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.list_distribution_tenants_by_customization, request, CloudFrontListDistributionTenantsByCustomizationResponse)

    async def list_distribution_tenants_by_customization_paginated(
        self,
        request: CloudFrontListDistributionTenantsByCustomizationRequest | None = None,
    ) -> list[CloudFrontListDistributionTenantsByCustomizationResponse]:
        return await self._paginate('list_distribution_tenants_by_customization', request, CloudFrontListDistributionTenantsByCustomizationResponse)

    async def list_distributions(
        self,
        request: CloudFrontListDistributionsRequest | None = None,
    ) -> CloudFrontListDistributionsResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions, request, CloudFrontListDistributionsResponse)

    async def list_distributions_paginated(
        self,
        request: CloudFrontListDistributionsRequest | None = None,
    ) -> list[CloudFrontListDistributionsResponse]:
        return await self._paginate('list_distributions', request, CloudFrontListDistributionsResponse)

    async def list_distributions_by_anycast_ip_list_id(
        self,
        request: CloudFrontListDistributionsByAnycastIpListIdRequest,
    ) -> CloudFrontListDistributionsByAnycastIpListIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_anycast_ip_list_id, request, CloudFrontListDistributionsByAnycastIpListIdResponse)

    async def list_distributions_by_cache_policy_id(
        self,
        request: CloudFrontListDistributionsByCachePolicyIdRequest,
    ) -> CloudFrontListDistributionsByCachePolicyIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_cache_policy_id, request, CloudFrontListDistributionsByCachePolicyIdResponse)

    async def list_distributions_by_connection_function(
        self,
        request: CloudFrontListDistributionsByConnectionFunctionRequest,
    ) -> CloudFrontListDistributionsByConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_connection_function, request, CloudFrontListDistributionsByConnectionFunctionResponse)

    async def list_distributions_by_connection_function_paginated(
        self,
        request: CloudFrontListDistributionsByConnectionFunctionRequest,
    ) -> list[CloudFrontListDistributionsByConnectionFunctionResponse]:
        return await self._paginate('list_distributions_by_connection_function', request, CloudFrontListDistributionsByConnectionFunctionResponse)

    async def list_distributions_by_connection_mode(
        self,
        request: CloudFrontListDistributionsByConnectionModeRequest,
    ) -> CloudFrontListDistributionsByConnectionModeResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_connection_mode, request, CloudFrontListDistributionsByConnectionModeResponse)

    async def list_distributions_by_connection_mode_paginated(
        self,
        request: CloudFrontListDistributionsByConnectionModeRequest,
    ) -> list[CloudFrontListDistributionsByConnectionModeResponse]:
        return await self._paginate('list_distributions_by_connection_mode', request, CloudFrontListDistributionsByConnectionModeResponse)

    async def list_distributions_by_key_group(
        self,
        request: CloudFrontListDistributionsByKeyGroupRequest,
    ) -> CloudFrontListDistributionsByKeyGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_key_group, request, CloudFrontListDistributionsByKeyGroupResponse)

    async def list_distributions_by_origin_request_policy_id(
        self,
        request: CloudFrontListDistributionsByOriginRequestPolicyIdRequest,
    ) -> CloudFrontListDistributionsByOriginRequestPolicyIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_origin_request_policy_id, request, CloudFrontListDistributionsByOriginRequestPolicyIdResponse)

    async def list_distributions_by_owned_resource(
        self,
        request: CloudFrontListDistributionsByOwnedResourceRequest,
    ) -> CloudFrontListDistributionsByOwnedResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_owned_resource, request, CloudFrontListDistributionsByOwnedResourceResponse)

    async def list_distributions_by_realtime_log_config(
        self,
        request: CloudFrontListDistributionsByRealtimeLogConfigRequest | None = None,
    ) -> CloudFrontListDistributionsByRealtimeLogConfigResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_realtime_log_config, request, CloudFrontListDistributionsByRealtimeLogConfigResponse)

    async def list_distributions_by_response_headers_policy_id(
        self,
        request: CloudFrontListDistributionsByResponseHeadersPolicyIdRequest,
    ) -> CloudFrontListDistributionsByResponseHeadersPolicyIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_response_headers_policy_id, request, CloudFrontListDistributionsByResponseHeadersPolicyIdResponse)

    async def list_distributions_by_trust_store(
        self,
        request: CloudFrontListDistributionsByTrustStoreRequest,
    ) -> CloudFrontListDistributionsByTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_trust_store, request, CloudFrontListDistributionsByTrustStoreResponse)

    async def list_distributions_by_trust_store_paginated(
        self,
        request: CloudFrontListDistributionsByTrustStoreRequest,
    ) -> list[CloudFrontListDistributionsByTrustStoreResponse]:
        return await self._paginate('list_distributions_by_trust_store', request, CloudFrontListDistributionsByTrustStoreResponse)

    async def list_distributions_by_vpc_origin_id(
        self,
        request: CloudFrontListDistributionsByVpcOriginIdRequest,
    ) -> CloudFrontListDistributionsByVpcOriginIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_vpc_origin_id, request, CloudFrontListDistributionsByVpcOriginIdResponse)

    async def list_distributions_by_web_acl_id(
        self,
        request: CloudFrontListDistributionsByWebACLIdRequest,
    ) -> CloudFrontListDistributionsByWebACLIdResponse:
        client = self._require_client()
        return await self._execute(client.list_distributions_by_web_acl_id, request, CloudFrontListDistributionsByWebACLIdResponse)

    async def list_domain_conflicts(
        self,
        request: CloudFrontListDomainConflictsRequest,
    ) -> CloudFrontListDomainConflictsResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_conflicts, request, CloudFrontListDomainConflictsResponse)

    async def list_domain_conflicts_paginated(
        self,
        request: CloudFrontListDomainConflictsRequest,
    ) -> list[CloudFrontListDomainConflictsResponse]:
        return await self._paginate('list_domain_conflicts', request, CloudFrontListDomainConflictsResponse)

    async def list_field_level_encryption_configs(
        self,
        request: CloudFrontListFieldLevelEncryptionConfigsRequest | None = None,
    ) -> CloudFrontListFieldLevelEncryptionConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_field_level_encryption_configs, request, CloudFrontListFieldLevelEncryptionConfigsResponse)

    async def list_field_level_encryption_profiles(
        self,
        request: CloudFrontListFieldLevelEncryptionProfilesRequest | None = None,
    ) -> CloudFrontListFieldLevelEncryptionProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_field_level_encryption_profiles, request, CloudFrontListFieldLevelEncryptionProfilesResponse)

    async def list_functions(
        self,
        request: CloudFrontListFunctionsRequest | None = None,
    ) -> CloudFrontListFunctionsResponse:
        client = self._require_client()
        return await self._execute(client.list_functions, request, CloudFrontListFunctionsResponse)

    async def list_invalidations(
        self,
        request: CloudFrontListInvalidationsRequest,
    ) -> CloudFrontListInvalidationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invalidations, request, CloudFrontListInvalidationsResponse)

    async def list_invalidations_paginated(
        self,
        request: CloudFrontListInvalidationsRequest,
    ) -> list[CloudFrontListInvalidationsResponse]:
        return await self._paginate('list_invalidations', request, CloudFrontListInvalidationsResponse)

    async def list_invalidations_for_distribution_tenant(
        self,
        request: CloudFrontListInvalidationsForDistributionTenantRequest,
    ) -> CloudFrontListInvalidationsForDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.list_invalidations_for_distribution_tenant, request, CloudFrontListInvalidationsForDistributionTenantResponse)

    async def list_invalidations_for_distribution_tenant_paginated(
        self,
        request: CloudFrontListInvalidationsForDistributionTenantRequest,
    ) -> list[CloudFrontListInvalidationsForDistributionTenantResponse]:
        return await self._paginate('list_invalidations_for_distribution_tenant', request, CloudFrontListInvalidationsForDistributionTenantResponse)

    async def list_key_groups(
        self,
        request: CloudFrontListKeyGroupsRequest | None = None,
    ) -> CloudFrontListKeyGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_key_groups, request, CloudFrontListKeyGroupsResponse)

    async def list_key_value_stores(
        self,
        request: CloudFrontListKeyValueStoresRequest | None = None,
    ) -> CloudFrontListKeyValueStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_key_value_stores, request, CloudFrontListKeyValueStoresResponse)

    async def list_key_value_stores_paginated(
        self,
        request: CloudFrontListKeyValueStoresRequest | None = None,
    ) -> list[CloudFrontListKeyValueStoresResponse]:
        return await self._paginate('list_key_value_stores', request, CloudFrontListKeyValueStoresResponse)

    async def list_origin_access_controls(
        self,
        request: CloudFrontListOriginAccessControlsRequest | None = None,
    ) -> CloudFrontListOriginAccessControlsResponse:
        client = self._require_client()
        return await self._execute(client.list_origin_access_controls, request, CloudFrontListOriginAccessControlsResponse)

    async def list_origin_access_controls_paginated(
        self,
        request: CloudFrontListOriginAccessControlsRequest | None = None,
    ) -> list[CloudFrontListOriginAccessControlsResponse]:
        return await self._paginate('list_origin_access_controls', request, CloudFrontListOriginAccessControlsResponse)

    async def list_origin_request_policies(
        self,
        request: CloudFrontListOriginRequestPoliciesRequest | None = None,
    ) -> CloudFrontListOriginRequestPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_origin_request_policies, request, CloudFrontListOriginRequestPoliciesResponse)

    async def list_public_keys(
        self,
        request: CloudFrontListPublicKeysRequest | None = None,
    ) -> CloudFrontListPublicKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_public_keys, request, CloudFrontListPublicKeysResponse)

    async def list_public_keys_paginated(
        self,
        request: CloudFrontListPublicKeysRequest | None = None,
    ) -> list[CloudFrontListPublicKeysResponse]:
        return await self._paginate('list_public_keys', request, CloudFrontListPublicKeysResponse)

    async def list_realtime_log_configs(
        self,
        request: CloudFrontListRealtimeLogConfigsRequest | None = None,
    ) -> CloudFrontListRealtimeLogConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_realtime_log_configs, request, CloudFrontListRealtimeLogConfigsResponse)

    async def list_response_headers_policies(
        self,
        request: CloudFrontListResponseHeadersPoliciesRequest | None = None,
    ) -> CloudFrontListResponseHeadersPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_response_headers_policies, request, CloudFrontListResponseHeadersPoliciesResponse)

    async def list_streaming_distributions(
        self,
        request: CloudFrontListStreamingDistributionsRequest | None = None,
    ) -> CloudFrontListStreamingDistributionsResponse:
        client = self._require_client()
        return await self._execute(client.list_streaming_distributions, request, CloudFrontListStreamingDistributionsResponse)

    async def list_streaming_distributions_paginated(
        self,
        request: CloudFrontListStreamingDistributionsRequest | None = None,
    ) -> list[CloudFrontListStreamingDistributionsResponse]:
        return await self._paginate('list_streaming_distributions', request, CloudFrontListStreamingDistributionsResponse)

    async def list_tags_for_resource(
        self,
        request: CloudFrontListTagsForResourceRequest,
    ) -> CloudFrontListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CloudFrontListTagsForResourceResponse)

    async def list_trust_stores(
        self,
        request: CloudFrontListTrustStoresRequest | None = None,
    ) -> CloudFrontListTrustStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_trust_stores, request, CloudFrontListTrustStoresResponse)

    async def list_trust_stores_paginated(
        self,
        request: CloudFrontListTrustStoresRequest | None = None,
    ) -> list[CloudFrontListTrustStoresResponse]:
        return await self._paginate('list_trust_stores', request, CloudFrontListTrustStoresResponse)

    async def list_vpc_origins(
        self,
        request: CloudFrontListVpcOriginsRequest | None = None,
    ) -> CloudFrontListVpcOriginsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_origins, request, CloudFrontListVpcOriginsResponse)

    async def publish_connection_function(
        self,
        request: CloudFrontPublishConnectionFunctionRequest,
    ) -> CloudFrontPublishConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.publish_connection_function, request, CloudFrontPublishConnectionFunctionResponse)

    async def publish_function(
        self,
        request: CloudFrontPublishFunctionRequest,
    ) -> CloudFrontPublishFunctionResponse:
        client = self._require_client()
        return await self._execute(client.publish_function, request, CloudFrontPublishFunctionResponse)

    async def put_resource_policy(
        self,
        request: CloudFrontPutResourcePolicyRequest,
    ) -> CloudFrontPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, CloudFrontPutResourcePolicyResponse)

    async def tag_resource(
        self,
        request: CloudFrontTagResourceRequest,
    ) -> CloudFrontTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CloudFrontTagResourceResponse)

    async def test_connection_function(
        self,
        request: CloudFrontTestConnectionFunctionRequest,
    ) -> CloudFrontTestConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.test_connection_function, request, CloudFrontTestConnectionFunctionResponse)

    async def test_function(
        self,
        request: CloudFrontTestFunctionRequest,
    ) -> CloudFrontTestFunctionResponse:
        client = self._require_client()
        return await self._execute(client.test_function, request, CloudFrontTestFunctionResponse)

    async def untag_resource(
        self,
        request: CloudFrontUntagResourceRequest,
    ) -> CloudFrontUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CloudFrontUntagResourceResponse)

    async def update_anycast_ip_list(
        self,
        request: CloudFrontUpdateAnycastIpListRequest,
    ) -> CloudFrontUpdateAnycastIpListResponse:
        client = self._require_client()
        return await self._execute(client.update_anycast_ip_list, request, CloudFrontUpdateAnycastIpListResponse)

    async def update_cache_policy(
        self,
        request: CloudFrontUpdateCachePolicyRequest,
    ) -> CloudFrontUpdateCachePolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_cache_policy, request, CloudFrontUpdateCachePolicyResponse)

    async def update_cloud_front_origin_access_identity(
        self,
        request: CloudFrontUpdateCloudFrontOriginAccessIdentityRequest,
    ) -> CloudFrontUpdateCloudFrontOriginAccessIdentityResponse:
        client = self._require_client()
        return await self._execute(client.update_cloud_front_origin_access_identity, request, CloudFrontUpdateCloudFrontOriginAccessIdentityResponse)

    async def update_connection_function(
        self,
        request: CloudFrontUpdateConnectionFunctionRequest,
    ) -> CloudFrontUpdateConnectionFunctionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection_function, request, CloudFrontUpdateConnectionFunctionResponse)

    async def update_connection_group(
        self,
        request: CloudFrontUpdateConnectionGroupRequest,
    ) -> CloudFrontUpdateConnectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_connection_group, request, CloudFrontUpdateConnectionGroupResponse)

    async def update_continuous_deployment_policy(
        self,
        request: CloudFrontUpdateContinuousDeploymentPolicyRequest,
    ) -> CloudFrontUpdateContinuousDeploymentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_continuous_deployment_policy, request, CloudFrontUpdateContinuousDeploymentPolicyResponse)

    async def update_distribution(
        self,
        request: CloudFrontUpdateDistributionRequest,
    ) -> CloudFrontUpdateDistributionResponse:
        client = self._require_client()
        return await self._execute(client.update_distribution, request, CloudFrontUpdateDistributionResponse)

    async def update_distribution_tenant(
        self,
        request: CloudFrontUpdateDistributionTenantRequest,
    ) -> CloudFrontUpdateDistributionTenantResponse:
        client = self._require_client()
        return await self._execute(client.update_distribution_tenant, request, CloudFrontUpdateDistributionTenantResponse)

    async def update_distribution_with_staging_config(
        self,
        request: CloudFrontUpdateDistributionWithStagingConfigRequest,
    ) -> CloudFrontUpdateDistributionWithStagingConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_distribution_with_staging_config, request, CloudFrontUpdateDistributionWithStagingConfigResponse)

    async def update_domain_association(
        self,
        request: CloudFrontUpdateDomainAssociationRequest,
    ) -> CloudFrontUpdateDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_association, request, CloudFrontUpdateDomainAssociationResponse)

    async def update_field_level_encryption_config(
        self,
        request: CloudFrontUpdateFieldLevelEncryptionConfigRequest,
    ) -> CloudFrontUpdateFieldLevelEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_field_level_encryption_config, request, CloudFrontUpdateFieldLevelEncryptionConfigResponse)

    async def update_field_level_encryption_profile(
        self,
        request: CloudFrontUpdateFieldLevelEncryptionProfileRequest,
    ) -> CloudFrontUpdateFieldLevelEncryptionProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_field_level_encryption_profile, request, CloudFrontUpdateFieldLevelEncryptionProfileResponse)

    async def update_function(
        self,
        request: CloudFrontUpdateFunctionRequest,
    ) -> CloudFrontUpdateFunctionResponse:
        client = self._require_client()
        return await self._execute(client.update_function, request, CloudFrontUpdateFunctionResponse)

    async def update_key_group(
        self,
        request: CloudFrontUpdateKeyGroupRequest,
    ) -> CloudFrontUpdateKeyGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_key_group, request, CloudFrontUpdateKeyGroupResponse)

    async def update_key_value_store(
        self,
        request: CloudFrontUpdateKeyValueStoreRequest,
    ) -> CloudFrontUpdateKeyValueStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_key_value_store, request, CloudFrontUpdateKeyValueStoreResponse)

    async def update_origin_access_control(
        self,
        request: CloudFrontUpdateOriginAccessControlRequest,
    ) -> CloudFrontUpdateOriginAccessControlResponse:
        client = self._require_client()
        return await self._execute(client.update_origin_access_control, request, CloudFrontUpdateOriginAccessControlResponse)

    async def update_origin_request_policy(
        self,
        request: CloudFrontUpdateOriginRequestPolicyRequest,
    ) -> CloudFrontUpdateOriginRequestPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_origin_request_policy, request, CloudFrontUpdateOriginRequestPolicyResponse)

    async def update_public_key(
        self,
        request: CloudFrontUpdatePublicKeyRequest,
    ) -> CloudFrontUpdatePublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_public_key, request, CloudFrontUpdatePublicKeyResponse)

    async def update_realtime_log_config(
        self,
        request: CloudFrontUpdateRealtimeLogConfigRequest | None = None,
    ) -> CloudFrontUpdateRealtimeLogConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_realtime_log_config, request, CloudFrontUpdateRealtimeLogConfigResponse)

    async def update_response_headers_policy(
        self,
        request: CloudFrontUpdateResponseHeadersPolicyRequest,
    ) -> CloudFrontUpdateResponseHeadersPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_response_headers_policy, request, CloudFrontUpdateResponseHeadersPolicyResponse)

    async def update_streaming_distribution(
        self,
        request: CloudFrontUpdateStreamingDistributionRequest,
    ) -> CloudFrontUpdateStreamingDistributionResponse:
        client = self._require_client()
        return await self._execute(client.update_streaming_distribution, request, CloudFrontUpdateStreamingDistributionResponse)

    async def update_trust_store(
        self,
        request: CloudFrontUpdateTrustStoreRequest,
    ) -> CloudFrontUpdateTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_trust_store, request, CloudFrontUpdateTrustStoreResponse)

    async def update_vpc_origin(
        self,
        request: CloudFrontUpdateVpcOriginRequest,
    ) -> CloudFrontUpdateVpcOriginResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_origin, request, CloudFrontUpdateVpcOriginResponse)

    async def verify_dns_configuration(
        self,
        request: CloudFrontVerifyDnsConfigurationRequest,
    ) -> CloudFrontVerifyDnsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.verify_dns_configuration, request, CloudFrontVerifyDnsConfigurationResponse)

from werkflow_aws.models.eks import (
    EKSCreateAddonRequest,
    EKSCreateAddonResponse,
    EKSCreateClusterRequest,
    EKSCreateClusterResponse,
    EKSCreateFargateProfileRequest,
    EKSCreateFargateProfileResponse,
    EKSCreateNodegroupRequest,
    EKSCreateNodegroupResponse,
    EKSDeleteAddonRequest,
    EKSDeleteAddonResponse,
    EKSDeleteClusterRequest,
    EKSDeleteClusterResponse,
    EKSDeleteFargateProfileRequest,
    EKSDeleteFargateProfileResponse,
    EKSDeleteNodegroupRequest,
    EKSDeleteNodegroupResponse,
    EKSDescribeAddonRequest,
    EKSDescribeAddonResponse,
    EKSDescribeClusterRequest,
    EKSDescribeClusterResponse,
    EKSDescribeFargateProfileRequest,
    EKSDescribeFargateProfileResponse,
    EKSDescribeNodegroupRequest,
    EKSDescribeNodegroupResponse,
    EKSDescribeUpdateRequest,
    EKSDescribeUpdateResponse,
    EKSListAddonsRequest,
    EKSListAddonsResponse,
    EKSListClustersRequest,
    EKSListClustersResponse,
    EKSListFargateProfilesRequest,
    EKSListFargateProfilesResponse,
    EKSListNodegroupsRequest,
    EKSListNodegroupsResponse,
    EKSListTagsForResourceRequest,
    EKSListTagsForResourceResponse,
    EKSListUpdatesRequest,
    EKSListUpdatesResponse,
    EKSTagResourceRequest,
    EKSTagResourceResponse,
    EKSUntagResourceRequest,
    EKSUntagResourceResponse,
    EKSUpdateAddonRequest,
    EKSUpdateAddonResponse,
    EKSUpdateClusterConfigRequest,
    EKSUpdateClusterConfigResponse,
    EKSUpdateClusterVersionRequest,
    EKSUpdateClusterVersionResponse,
    EKSUpdateNodegroupConfigRequest,
    EKSUpdateNodegroupConfigResponse,
    EKSUpdateNodegroupVersionRequest,
    EKSUpdateNodegroupVersionResponse,
)
from werkflow_aws.types.eks_client import EKSClient
from .base import AWSBaseService
from werkflow_aws.models.eks import (
    EKSActivateCertificateAuthorityRequest,
    EKSActivateCertificateAuthorityResponse,
    EKSAssociateAccessPolicyRequest,
    EKSAssociateAccessPolicyResponse,
    EKSAssociateEncryptionConfigRequest,
    EKSAssociateEncryptionConfigResponse,
    EKSAssociateIdentityProviderConfigRequest,
    EKSAssociateIdentityProviderConfigResponse,
    EKSCancelUpdateRequest,
    EKSCancelUpdateResponse,
    EKSCreateAccessEntryRequest,
    EKSCreateAccessEntryResponse,
    EKSCreateCapabilityRequest,
    EKSCreateCapabilityResponse,
    EKSCreateCertificateAuthorityRequest,
    EKSCreateCertificateAuthorityResponse,
    EKSCreateEksAnywhereSubscriptionRequest,
    EKSCreateEksAnywhereSubscriptionResponse,
    EKSCreatePodIdentityAssociationRequest,
    EKSCreatePodIdentityAssociationResponse,
    EKSDeleteAccessEntryRequest,
    EKSDeleteAccessEntryResponse,
    EKSDeleteCapabilityRequest,
    EKSDeleteCapabilityResponse,
    EKSDeleteCertificateAuthorityRequest,
    EKSDeleteCertificateAuthorityResponse,
    EKSDeleteEksAnywhereSubscriptionRequest,
    EKSDeleteEksAnywhereSubscriptionResponse,
    EKSDeletePodIdentityAssociationRequest,
    EKSDeletePodIdentityAssociationResponse,
    EKSDeregisterClusterRequest,
    EKSDeregisterClusterResponse,
    EKSDescribeAccessEntryRequest,
    EKSDescribeAccessEntryResponse,
    EKSDescribeAddonConfigurationRequest,
    EKSDescribeAddonConfigurationResponse,
    EKSDescribeAddonVersionsRequest,
    EKSDescribeAddonVersionsResponse,
    EKSDescribeCapabilityRequest,
    EKSDescribeCapabilityResponse,
    EKSDescribeCertificateAuthorityRequest,
    EKSDescribeCertificateAuthorityResponse,
    EKSDescribeClusterVersionsRequest,
    EKSDescribeClusterVersionsResponse,
    EKSDescribeEksAnywhereSubscriptionRequest,
    EKSDescribeEksAnywhereSubscriptionResponse,
    EKSDescribeIdentityProviderConfigRequest,
    EKSDescribeIdentityProviderConfigResponse,
    EKSDescribeInsightRequest,
    EKSDescribeInsightResponse,
    EKSDescribeInsightsRefreshRequest,
    EKSDescribeInsightsRefreshResponse,
    EKSDescribePodIdentityAssociationRequest,
    EKSDescribePodIdentityAssociationResponse,
    EKSDisassociateAccessPolicyRequest,
    EKSDisassociateAccessPolicyResponse,
    EKSDisassociateIdentityProviderConfigRequest,
    EKSDisassociateIdentityProviderConfigResponse,
    EKSListAccessEntriesRequest,
    EKSListAccessEntriesResponse,
    EKSListAccessPoliciesRequest,
    EKSListAccessPoliciesResponse,
    EKSListAssociatedAccessPoliciesRequest,
    EKSListAssociatedAccessPoliciesResponse,
    EKSListCapabilitiesRequest,
    EKSListCapabilitiesResponse,
    EKSListCertificateAuthoritiesRequest,
    EKSListCertificateAuthoritiesResponse,
    EKSListEksAnywhereSubscriptionsRequest,
    EKSListEksAnywhereSubscriptionsResponse,
    EKSListIdentityProviderConfigsRequest,
    EKSListIdentityProviderConfigsResponse,
    EKSListInsightsRequest,
    EKSListInsightsResponse,
    EKSListPodIdentityAssociationsRequest,
    EKSListPodIdentityAssociationsResponse,
    EKSRegisterClusterRequest,
    EKSRegisterClusterResponse,
    EKSStartInsightsRefreshRequest,
    EKSStartInsightsRefreshResponse,
    EKSUpdateAccessEntryRequest,
    EKSUpdateAccessEntryResponse,
    EKSUpdateCapabilityRequest,
    EKSUpdateCapabilityResponse,
    EKSUpdateEksAnywhereSubscriptionRequest,
    EKSUpdateEksAnywhereSubscriptionResponse,
    EKSUpdatePodIdentityAssociationRequest,
    EKSUpdatePodIdentityAssociationResponse,
)


class AWSEKS(AWSBaseService[EKSClient]):
    service_name = 'EKS'
    boto3_service_name = 'eks'

    def __init__(self) -> None:
        super().__init__(
            service_name='EKS',
            boto3_service_name='eks',
        )

    async def list_clusters(
        self,
        request: EKSListClustersRequest | None = None,
    ) -> EKSListClustersResponse:
        client = self._require_client()
        return await self._execute(
            client.list_clusters,
            request or EKSListClustersRequest(),
            EKSListClustersResponse,
        )

    async def list_clusters_paginated(
        self,
        request: EKSListClustersRequest | None = None,
    ) -> list[EKSListClustersResponse]:
        return await self._paginate(
            'list_clusters',
            request or EKSListClustersRequest(),
            EKSListClustersResponse,
        )

    async def describe_cluster(
        self,
        request: EKSDescribeClusterRequest,
    ) -> EKSDescribeClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_cluster,
            request,
            EKSDescribeClusterResponse,
        )

    async def create_cluster(
        self,
        request: EKSCreateClusterRequest,
    ) -> EKSCreateClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.create_cluster,
            request,
            EKSCreateClusterResponse,
        )

    async def delete_cluster(
        self,
        request: EKSDeleteClusterRequest,
    ) -> EKSDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_cluster,
            request,
            EKSDeleteClusterResponse,
        )

    async def update_cluster_config(
        self,
        request: EKSUpdateClusterConfigRequest,
    ) -> EKSUpdateClusterConfigResponse:
        client = self._require_client()
        return await self._execute(
            client.update_cluster_config,
            request,
            EKSUpdateClusterConfigResponse,
        )

    async def update_cluster_version(
        self,
        request: EKSUpdateClusterVersionRequest,
    ) -> EKSUpdateClusterVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.update_cluster_version,
            request,
            EKSUpdateClusterVersionResponse,
        )

    async def list_nodegroups(
        self,
        request: EKSListNodegroupsRequest,
    ) -> EKSListNodegroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_nodegroups,
            request,
            EKSListNodegroupsResponse,
        )

    async def list_nodegroups_paginated(
        self,
        request: EKSListNodegroupsRequest,
    ) -> list[EKSListNodegroupsResponse]:
        return await self._paginate(
            'list_nodegroups',
            request,
            EKSListNodegroupsResponse,
        )

    async def describe_nodegroup(
        self,
        request: EKSDescribeNodegroupRequest,
    ) -> EKSDescribeNodegroupResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_nodegroup,
            request,
            EKSDescribeNodegroupResponse,
        )

    async def create_nodegroup(
        self,
        request: EKSCreateNodegroupRequest,
    ) -> EKSCreateNodegroupResponse:
        client = self._require_client()
        return await self._execute(
            client.create_nodegroup,
            request,
            EKSCreateNodegroupResponse,
        )

    async def update_nodegroup_config(
        self,
        request: EKSUpdateNodegroupConfigRequest,
    ) -> EKSUpdateNodegroupConfigResponse:
        client = self._require_client()
        return await self._execute(
            client.update_nodegroup_config,
            request,
            EKSUpdateNodegroupConfigResponse,
        )

    async def update_nodegroup_version(
        self,
        request: EKSUpdateNodegroupVersionRequest,
    ) -> EKSUpdateNodegroupVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.update_nodegroup_version,
            request,
            EKSUpdateNodegroupVersionResponse,
        )

    async def delete_nodegroup(
        self,
        request: EKSDeleteNodegroupRequest,
    ) -> EKSDeleteNodegroupResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_nodegroup,
            request,
            EKSDeleteNodegroupResponse,
        )

    async def list_fargate_profiles(
        self,
        request: EKSListFargateProfilesRequest,
    ) -> EKSListFargateProfilesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_fargate_profiles,
            request,
            EKSListFargateProfilesResponse,
        )

    async def list_fargate_profiles_paginated(
        self,
        request: EKSListFargateProfilesRequest,
    ) -> list[EKSListFargateProfilesResponse]:
        return await self._paginate(
            'list_fargate_profiles',
            request,
            EKSListFargateProfilesResponse,
        )

    async def describe_fargate_profile(
        self,
        request: EKSDescribeFargateProfileRequest,
    ) -> EKSDescribeFargateProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_fargate_profile,
            request,
            EKSDescribeFargateProfileResponse,
        )

    async def create_fargate_profile(
        self,
        request: EKSCreateFargateProfileRequest,
    ) -> EKSCreateFargateProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.create_fargate_profile,
            request,
            EKSCreateFargateProfileResponse,
        )

    async def delete_fargate_profile(
        self,
        request: EKSDeleteFargateProfileRequest,
    ) -> EKSDeleteFargateProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_fargate_profile,
            request,
            EKSDeleteFargateProfileResponse,
        )

    async def list_addons(
        self,
        request: EKSListAddonsRequest,
    ) -> EKSListAddonsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_addons,
            request,
            EKSListAddonsResponse,
        )

    async def list_addons_paginated(
        self,
        request: EKSListAddonsRequest,
    ) -> list[EKSListAddonsResponse]:
        return await self._paginate(
            'list_addons',
            request,
            EKSListAddonsResponse,
        )

    async def describe_addon(
        self,
        request: EKSDescribeAddonRequest,
    ) -> EKSDescribeAddonResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_addon,
            request,
            EKSDescribeAddonResponse,
        )

    async def create_addon(
        self,
        request: EKSCreateAddonRequest,
    ) -> EKSCreateAddonResponse:
        client = self._require_client()
        return await self._execute(
            client.create_addon,
            request,
            EKSCreateAddonResponse,
        )

    async def update_addon(
        self,
        request: EKSUpdateAddonRequest,
    ) -> EKSUpdateAddonResponse:
        client = self._require_client()
        return await self._execute(
            client.update_addon,
            request,
            EKSUpdateAddonResponse,
        )

    async def delete_addon(
        self,
        request: EKSDeleteAddonRequest,
    ) -> EKSDeleteAddonResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_addon,
            request,
            EKSDeleteAddonResponse,
        )

    async def list_updates(
        self,
        request: EKSListUpdatesRequest,
    ) -> EKSListUpdatesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_updates,
            request,
            EKSListUpdatesResponse,
        )

    async def list_updates_paginated(
        self,
        request: EKSListUpdatesRequest,
    ) -> list[EKSListUpdatesResponse]:
        return await self._paginate(
            'list_updates',
            request,
            EKSListUpdatesResponse,
        )

    async def describe_update(
        self,
        request: EKSDescribeUpdateRequest,
    ) -> EKSDescribeUpdateResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_update,
            request,
            EKSDescribeUpdateResponse,
        )

    async def list_tags_for_resource(
        self,
        request: EKSListTagsForResourceRequest,
    ) -> EKSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_for_resource,
            request,
            EKSListTagsForResourceResponse,
        )

    async def tag_resource(
        self,
        request: EKSTagResourceRequest,
    ) -> EKSTagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            EKSTagResourceResponse,
        )

    async def untag_resource(
        self,
        request: EKSUntagResourceRequest,
    ) -> EKSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            EKSUntagResourceResponse,
        )

    async def activate_certificate_authority(
        self,
        request: EKSActivateCertificateAuthorityRequest,
    ) -> EKSActivateCertificateAuthorityResponse:
        client = self._require_client()
        return await self._execute(client.activate_certificate_authority, request, EKSActivateCertificateAuthorityResponse)

    async def associate_access_policy(
        self,
        request: EKSAssociateAccessPolicyRequest,
    ) -> EKSAssociateAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.associate_access_policy, request, EKSAssociateAccessPolicyResponse)

    async def associate_encryption_config(
        self,
        request: EKSAssociateEncryptionConfigRequest,
    ) -> EKSAssociateEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.associate_encryption_config, request, EKSAssociateEncryptionConfigResponse)

    async def associate_identity_provider_config(
        self,
        request: EKSAssociateIdentityProviderConfigRequest,
    ) -> EKSAssociateIdentityProviderConfigResponse:
        client = self._require_client()
        return await self._execute(client.associate_identity_provider_config, request, EKSAssociateIdentityProviderConfigResponse)

    async def cancel_update(
        self,
        request: EKSCancelUpdateRequest,
    ) -> EKSCancelUpdateResponse:
        client = self._require_client()
        return await self._execute(client.cancel_update, request, EKSCancelUpdateResponse)

    async def create_access_entry(
        self,
        request: EKSCreateAccessEntryRequest,
    ) -> EKSCreateAccessEntryResponse:
        client = self._require_client()
        return await self._execute(client.create_access_entry, request, EKSCreateAccessEntryResponse)

    async def create_capability(
        self,
        request: EKSCreateCapabilityRequest,
    ) -> EKSCreateCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.create_capability, request, EKSCreateCapabilityResponse)

    async def create_certificate_authority(
        self,
        request: EKSCreateCertificateAuthorityRequest,
    ) -> EKSCreateCertificateAuthorityResponse:
        client = self._require_client()
        return await self._execute(client.create_certificate_authority, request, EKSCreateCertificateAuthorityResponse)

    async def create_eks_anywhere_subscription(
        self,
        request: EKSCreateEksAnywhereSubscriptionRequest,
    ) -> EKSCreateEksAnywhereSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_eks_anywhere_subscription, request, EKSCreateEksAnywhereSubscriptionResponse)

    async def create_pod_identity_association(
        self,
        request: EKSCreatePodIdentityAssociationRequest,
    ) -> EKSCreatePodIdentityAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_pod_identity_association, request, EKSCreatePodIdentityAssociationResponse)

    async def delete_access_entry(
        self,
        request: EKSDeleteAccessEntryRequest,
    ) -> EKSDeleteAccessEntryResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_entry, request, EKSDeleteAccessEntryResponse)

    async def delete_capability(
        self,
        request: EKSDeleteCapabilityRequest,
    ) -> EKSDeleteCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.delete_capability, request, EKSDeleteCapabilityResponse)

    async def delete_certificate_authority(
        self,
        request: EKSDeleteCertificateAuthorityRequest,
    ) -> EKSDeleteCertificateAuthorityResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate_authority, request, EKSDeleteCertificateAuthorityResponse)

    async def delete_eks_anywhere_subscription(
        self,
        request: EKSDeleteEksAnywhereSubscriptionRequest,
    ) -> EKSDeleteEksAnywhereSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_eks_anywhere_subscription, request, EKSDeleteEksAnywhereSubscriptionResponse)

    async def delete_pod_identity_association(
        self,
        request: EKSDeletePodIdentityAssociationRequest,
    ) -> EKSDeletePodIdentityAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_pod_identity_association, request, EKSDeletePodIdentityAssociationResponse)

    async def deregister_cluster(
        self,
        request: EKSDeregisterClusterRequest,
    ) -> EKSDeregisterClusterResponse:
        client = self._require_client()
        return await self._execute(client.deregister_cluster, request, EKSDeregisterClusterResponse)

    async def describe_access_entry(
        self,
        request: EKSDescribeAccessEntryRequest,
    ) -> EKSDescribeAccessEntryResponse:
        client = self._require_client()
        return await self._execute(client.describe_access_entry, request, EKSDescribeAccessEntryResponse)

    async def describe_addon_configuration(
        self,
        request: EKSDescribeAddonConfigurationRequest,
    ) -> EKSDescribeAddonConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_addon_configuration, request, EKSDescribeAddonConfigurationResponse)

    async def describe_addon_versions(
        self,
        request: EKSDescribeAddonVersionsRequest | None = None,
    ) -> EKSDescribeAddonVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_addon_versions, request, EKSDescribeAddonVersionsResponse)

    async def describe_addon_versions_paginated(
        self,
        request: EKSDescribeAddonVersionsRequest | None = None,
    ) -> list[EKSDescribeAddonVersionsResponse]:
        return await self._paginate('describe_addon_versions', request, EKSDescribeAddonVersionsResponse)

    async def describe_capability(
        self,
        request: EKSDescribeCapabilityRequest,
    ) -> EKSDescribeCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.describe_capability, request, EKSDescribeCapabilityResponse)

    async def describe_certificate_authority(
        self,
        request: EKSDescribeCertificateAuthorityRequest,
    ) -> EKSDescribeCertificateAuthorityResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate_authority, request, EKSDescribeCertificateAuthorityResponse)

    async def describe_cluster_versions(
        self,
        request: EKSDescribeClusterVersionsRequest | None = None,
    ) -> EKSDescribeClusterVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_versions, request, EKSDescribeClusterVersionsResponse)

    async def describe_cluster_versions_paginated(
        self,
        request: EKSDescribeClusterVersionsRequest | None = None,
    ) -> list[EKSDescribeClusterVersionsResponse]:
        return await self._paginate('describe_cluster_versions', request, EKSDescribeClusterVersionsResponse)

    async def describe_eks_anywhere_subscription(
        self,
        request: EKSDescribeEksAnywhereSubscriptionRequest,
    ) -> EKSDescribeEksAnywhereSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.describe_eks_anywhere_subscription, request, EKSDescribeEksAnywhereSubscriptionResponse)

    async def describe_identity_provider_config(
        self,
        request: EKSDescribeIdentityProviderConfigRequest,
    ) -> EKSDescribeIdentityProviderConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_provider_config, request, EKSDescribeIdentityProviderConfigResponse)

    async def describe_insight(
        self,
        request: EKSDescribeInsightRequest,
    ) -> EKSDescribeInsightResponse:
        client = self._require_client()
        return await self._execute(client.describe_insight, request, EKSDescribeInsightResponse)

    async def describe_insights_refresh(
        self,
        request: EKSDescribeInsightsRefreshRequest,
    ) -> EKSDescribeInsightsRefreshResponse:
        client = self._require_client()
        return await self._execute(client.describe_insights_refresh, request, EKSDescribeInsightsRefreshResponse)

    async def describe_pod_identity_association(
        self,
        request: EKSDescribePodIdentityAssociationRequest,
    ) -> EKSDescribePodIdentityAssociationResponse:
        client = self._require_client()
        return await self._execute(client.describe_pod_identity_association, request, EKSDescribePodIdentityAssociationResponse)

    async def disassociate_access_policy(
        self,
        request: EKSDisassociateAccessPolicyRequest,
    ) -> EKSDisassociateAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_access_policy, request, EKSDisassociateAccessPolicyResponse)

    async def disassociate_identity_provider_config(
        self,
        request: EKSDisassociateIdentityProviderConfigRequest,
    ) -> EKSDisassociateIdentityProviderConfigResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_identity_provider_config, request, EKSDisassociateIdentityProviderConfigResponse)

    async def list_access_entries(
        self,
        request: EKSListAccessEntriesRequest,
    ) -> EKSListAccessEntriesResponse:
        client = self._require_client()
        return await self._execute(client.list_access_entries, request, EKSListAccessEntriesResponse)

    async def list_access_entries_paginated(
        self,
        request: EKSListAccessEntriesRequest,
    ) -> list[EKSListAccessEntriesResponse]:
        return await self._paginate('list_access_entries', request, EKSListAccessEntriesResponse)

    async def list_access_policies(
        self,
        request: EKSListAccessPoliciesRequest | None = None,
    ) -> EKSListAccessPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_access_policies, request, EKSListAccessPoliciesResponse)

    async def list_access_policies_paginated(
        self,
        request: EKSListAccessPoliciesRequest | None = None,
    ) -> list[EKSListAccessPoliciesResponse]:
        return await self._paginate('list_access_policies', request, EKSListAccessPoliciesResponse)

    async def list_associated_access_policies(
        self,
        request: EKSListAssociatedAccessPoliciesRequest,
    ) -> EKSListAssociatedAccessPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_access_policies, request, EKSListAssociatedAccessPoliciesResponse)

    async def list_associated_access_policies_paginated(
        self,
        request: EKSListAssociatedAccessPoliciesRequest,
    ) -> list[EKSListAssociatedAccessPoliciesResponse]:
        return await self._paginate('list_associated_access_policies', request, EKSListAssociatedAccessPoliciesResponse)

    async def list_capabilities(
        self,
        request: EKSListCapabilitiesRequest,
    ) -> EKSListCapabilitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_capabilities, request, EKSListCapabilitiesResponse)

    async def list_capabilities_paginated(
        self,
        request: EKSListCapabilitiesRequest,
    ) -> list[EKSListCapabilitiesResponse]:
        return await self._paginate('list_capabilities', request, EKSListCapabilitiesResponse)

    async def list_certificate_authorities(
        self,
        request: EKSListCertificateAuthoritiesRequest,
    ) -> EKSListCertificateAuthoritiesResponse:
        client = self._require_client()
        return await self._execute(client.list_certificate_authorities, request, EKSListCertificateAuthoritiesResponse)

    async def list_certificate_authorities_paginated(
        self,
        request: EKSListCertificateAuthoritiesRequest,
    ) -> list[EKSListCertificateAuthoritiesResponse]:
        return await self._paginate('list_certificate_authorities', request, EKSListCertificateAuthoritiesResponse)

    async def list_eks_anywhere_subscriptions(
        self,
        request: EKSListEksAnywhereSubscriptionsRequest | None = None,
    ) -> EKSListEksAnywhereSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_eks_anywhere_subscriptions, request, EKSListEksAnywhereSubscriptionsResponse)

    async def list_eks_anywhere_subscriptions_paginated(
        self,
        request: EKSListEksAnywhereSubscriptionsRequest | None = None,
    ) -> list[EKSListEksAnywhereSubscriptionsResponse]:
        return await self._paginate('list_eks_anywhere_subscriptions', request, EKSListEksAnywhereSubscriptionsResponse)

    async def list_identity_provider_configs(
        self,
        request: EKSListIdentityProviderConfigsRequest,
    ) -> EKSListIdentityProviderConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_provider_configs, request, EKSListIdentityProviderConfigsResponse)

    async def list_identity_provider_configs_paginated(
        self,
        request: EKSListIdentityProviderConfigsRequest,
    ) -> list[EKSListIdentityProviderConfigsResponse]:
        return await self._paginate('list_identity_provider_configs', request, EKSListIdentityProviderConfigsResponse)

    async def list_insights(
        self,
        request: EKSListInsightsRequest,
    ) -> EKSListInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_insights, request, EKSListInsightsResponse)

    async def list_insights_paginated(
        self,
        request: EKSListInsightsRequest,
    ) -> list[EKSListInsightsResponse]:
        return await self._paginate('list_insights', request, EKSListInsightsResponse)

    async def list_pod_identity_associations(
        self,
        request: EKSListPodIdentityAssociationsRequest,
    ) -> EKSListPodIdentityAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_pod_identity_associations, request, EKSListPodIdentityAssociationsResponse)

    async def list_pod_identity_associations_paginated(
        self,
        request: EKSListPodIdentityAssociationsRequest,
    ) -> list[EKSListPodIdentityAssociationsResponse]:
        return await self._paginate('list_pod_identity_associations', request, EKSListPodIdentityAssociationsResponse)

    async def register_cluster(
        self,
        request: EKSRegisterClusterRequest,
    ) -> EKSRegisterClusterResponse:
        client = self._require_client()
        return await self._execute(client.register_cluster, request, EKSRegisterClusterResponse)

    async def start_insights_refresh(
        self,
        request: EKSStartInsightsRefreshRequest,
    ) -> EKSStartInsightsRefreshResponse:
        client = self._require_client()
        return await self._execute(client.start_insights_refresh, request, EKSStartInsightsRefreshResponse)

    async def update_access_entry(
        self,
        request: EKSUpdateAccessEntryRequest,
    ) -> EKSUpdateAccessEntryResponse:
        client = self._require_client()
        return await self._execute(client.update_access_entry, request, EKSUpdateAccessEntryResponse)

    async def update_capability(
        self,
        request: EKSUpdateCapabilityRequest,
    ) -> EKSUpdateCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.update_capability, request, EKSUpdateCapabilityResponse)

    async def update_eks_anywhere_subscription(
        self,
        request: EKSUpdateEksAnywhereSubscriptionRequest,
    ) -> EKSUpdateEksAnywhereSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_eks_anywhere_subscription, request, EKSUpdateEksAnywhereSubscriptionResponse)

    async def update_pod_identity_association(
        self,
        request: EKSUpdatePodIdentityAssociationRequest,
    ) -> EKSUpdatePodIdentityAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_pod_identity_association, request, EKSUpdatePodIdentityAssociationResponse)


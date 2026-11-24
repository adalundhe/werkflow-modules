from werkflow_aws.models.redshift import (
    RedshiftAcceptReservedNodeExchangeRequest,
    RedshiftAcceptReservedNodeExchangeResponse,
    RedshiftAddPartnerRequest,
    RedshiftAddPartnerResponse,
    RedshiftAssociateDataShareConsumerRequest,
    RedshiftAssociateDataShareConsumerResponse,
    RedshiftAuthorizeClusterSecurityGroupIngressRequest,
    RedshiftAuthorizeClusterSecurityGroupIngressResponse,
    RedshiftAuthorizeDataShareRequest,
    RedshiftAuthorizeDataShareResponse,
    RedshiftAuthorizeEndpointAccessRequest,
    RedshiftAuthorizeEndpointAccessResponse,
    RedshiftAuthorizeSnapshotAccessRequest,
    RedshiftAuthorizeSnapshotAccessResponse,
    RedshiftBatchDeleteClusterSnapshotsRequest,
    RedshiftBatchDeleteClusterSnapshotsResponse,
    RedshiftBatchModifyClusterSnapshotsRequest,
    RedshiftBatchModifyClusterSnapshotsResponse,
    RedshiftCancelResizeRequest,
    RedshiftCancelResizeResponse,
    RedshiftCopyClusterSnapshotRequest,
    RedshiftCopyClusterSnapshotResponse,
    RedshiftCreateAuthenticationProfileRequest,
    RedshiftCreateAuthenticationProfileResponse,
    RedshiftCreateClusterParameterGroupRequest,
    RedshiftCreateClusterParameterGroupResponse,
    RedshiftCreateClusterRequest,
    RedshiftCreateClusterResponse,
    RedshiftCreateClusterSecurityGroupRequest,
    RedshiftCreateClusterSecurityGroupResponse,
    RedshiftCreateClusterSnapshotRequest,
    RedshiftCreateClusterSnapshotResponse,
    RedshiftCreateClusterSubnetGroupRequest,
    RedshiftCreateClusterSubnetGroupResponse,
    RedshiftCreateCustomDomainAssociationRequest,
    RedshiftCreateCustomDomainAssociationResponse,
    RedshiftCreateEndpointAccessRequest,
    RedshiftCreateEndpointAccessResponse,
    RedshiftCreateEventSubscriptionRequest,
    RedshiftCreateEventSubscriptionResponse,
    RedshiftCreateHsmClientCertificateRequest,
    RedshiftCreateHsmClientCertificateResponse,
    RedshiftCreateHsmConfigurationRequest,
    RedshiftCreateHsmConfigurationResponse,
    RedshiftCreateIntegrationRequest,
    RedshiftCreateIntegrationResponse,
    RedshiftCreateQev2IdcApplicationRequest,
    RedshiftCreateQev2IdcApplicationResponse,
    RedshiftCreateRedshiftIdcApplicationRequest,
    RedshiftCreateRedshiftIdcApplicationResponse,
    RedshiftCreateScheduledActionRequest,
    RedshiftCreateScheduledActionResponse,
    RedshiftCreateSnapshotCopyGrantRequest,
    RedshiftCreateSnapshotCopyGrantResponse,
    RedshiftCreateSnapshotScheduleRequest,
    RedshiftCreateSnapshotScheduleResponse,
    RedshiftCreateTagsRequest,
    RedshiftCreateTagsResponse,
    RedshiftCreateUsageLimitRequest,
    RedshiftCreateUsageLimitResponse,
    RedshiftDeauthorizeDataShareRequest,
    RedshiftDeauthorizeDataShareResponse,
    RedshiftDeleteAuthenticationProfileRequest,
    RedshiftDeleteAuthenticationProfileResponse,
    RedshiftDeleteClusterParameterGroupRequest,
    RedshiftDeleteClusterParameterGroupResponse,
    RedshiftDeleteClusterRequest,
    RedshiftDeleteClusterResponse,
    RedshiftDeleteClusterSecurityGroupRequest,
    RedshiftDeleteClusterSecurityGroupResponse,
    RedshiftDeleteClusterSnapshotRequest,
    RedshiftDeleteClusterSnapshotResponse,
    RedshiftDeleteClusterSubnetGroupRequest,
    RedshiftDeleteClusterSubnetGroupResponse,
    RedshiftDeleteCustomDomainAssociationRequest,
    RedshiftDeleteCustomDomainAssociationResponse,
    RedshiftDeleteEndpointAccessRequest,
    RedshiftDeleteEndpointAccessResponse,
    RedshiftDeleteEventSubscriptionRequest,
    RedshiftDeleteEventSubscriptionResponse,
    RedshiftDeleteHsmClientCertificateRequest,
    RedshiftDeleteHsmClientCertificateResponse,
    RedshiftDeleteHsmConfigurationRequest,
    RedshiftDeleteHsmConfigurationResponse,
    RedshiftDeleteIntegrationRequest,
    RedshiftDeleteIntegrationResponse,
    RedshiftDeletePartnerRequest,
    RedshiftDeletePartnerResponse,
    RedshiftDeleteQev2IdcApplicationRequest,
    RedshiftDeleteQev2IdcApplicationResponse,
    RedshiftDeleteRedshiftIdcApplicationRequest,
    RedshiftDeleteRedshiftIdcApplicationResponse,
    RedshiftDeleteResourcePolicyRequest,
    RedshiftDeleteResourcePolicyResponse,
    RedshiftDeleteScheduledActionRequest,
    RedshiftDeleteScheduledActionResponse,
    RedshiftDeleteSnapshotCopyGrantRequest,
    RedshiftDeleteSnapshotCopyGrantResponse,
    RedshiftDeleteSnapshotScheduleRequest,
    RedshiftDeleteSnapshotScheduleResponse,
    RedshiftDeleteTagsRequest,
    RedshiftDeleteTagsResponse,
    RedshiftDeleteUsageLimitRequest,
    RedshiftDeleteUsageLimitResponse,
    RedshiftDeregisterNamespaceRequest,
    RedshiftDeregisterNamespaceResponse,
    RedshiftDescribeAccountAttributesRequest,
    RedshiftDescribeAccountAttributesResponse,
    RedshiftDescribeAuthenticationProfilesRequest,
    RedshiftDescribeAuthenticationProfilesResponse,
    RedshiftDescribeClusterDbRevisionsRequest,
    RedshiftDescribeClusterDbRevisionsResponse,
    RedshiftDescribeClusterParameterGroupsRequest,
    RedshiftDescribeClusterParameterGroupsResponse,
    RedshiftDescribeClusterParametersRequest,
    RedshiftDescribeClusterParametersResponse,
    RedshiftDescribeClusterSecurityGroupsRequest,
    RedshiftDescribeClusterSecurityGroupsResponse,
    RedshiftDescribeClusterSnapshotsRequest,
    RedshiftDescribeClusterSnapshotsResponse,
    RedshiftDescribeClusterSubnetGroupsRequest,
    RedshiftDescribeClusterSubnetGroupsResponse,
    RedshiftDescribeClusterTracksRequest,
    RedshiftDescribeClusterTracksResponse,
    RedshiftDescribeClusterVersionsRequest,
    RedshiftDescribeClusterVersionsResponse,
    RedshiftDescribeClustersRequest,
    RedshiftDescribeClustersResponse,
    RedshiftDescribeCustomDomainAssociationsRequest,
    RedshiftDescribeCustomDomainAssociationsResponse,
    RedshiftDescribeDataSharesForConsumerRequest,
    RedshiftDescribeDataSharesForConsumerResponse,
    RedshiftDescribeDataSharesForProducerRequest,
    RedshiftDescribeDataSharesForProducerResponse,
    RedshiftDescribeDataSharesRequest,
    RedshiftDescribeDataSharesResponse,
    RedshiftDescribeDefaultClusterParametersRequest,
    RedshiftDescribeDefaultClusterParametersResponse,
    RedshiftDescribeEndpointAccessRequest,
    RedshiftDescribeEndpointAccessResponse,
    RedshiftDescribeEndpointAuthorizationRequest,
    RedshiftDescribeEndpointAuthorizationResponse,
    RedshiftDescribeEventCategoriesRequest,
    RedshiftDescribeEventCategoriesResponse,
    RedshiftDescribeEventSubscriptionsRequest,
    RedshiftDescribeEventSubscriptionsResponse,
    RedshiftDescribeEventsRequest,
    RedshiftDescribeEventsResponse,
    RedshiftDescribeHsmClientCertificatesRequest,
    RedshiftDescribeHsmClientCertificatesResponse,
    RedshiftDescribeHsmConfigurationsRequest,
    RedshiftDescribeHsmConfigurationsResponse,
    RedshiftDescribeInboundIntegrationsRequest,
    RedshiftDescribeInboundIntegrationsResponse,
    RedshiftDescribeIntegrationsRequest,
    RedshiftDescribeIntegrationsResponse,
    RedshiftDescribeLoggingStatusRequest,
    RedshiftDescribeLoggingStatusResponse,
    RedshiftDescribeNodeConfigurationOptionsRequest,
    RedshiftDescribeNodeConfigurationOptionsResponse,
    RedshiftDescribeOrderableClusterOptionsRequest,
    RedshiftDescribeOrderableClusterOptionsResponse,
    RedshiftDescribePartnersRequest,
    RedshiftDescribePartnersResponse,
    RedshiftDescribeQev2IdcApplicationsRequest,
    RedshiftDescribeQev2IdcApplicationsResponse,
    RedshiftDescribeRedshiftIdcApplicationsRequest,
    RedshiftDescribeRedshiftIdcApplicationsResponse,
    RedshiftDescribeReservedNodeExchangeStatusRequest,
    RedshiftDescribeReservedNodeExchangeStatusResponse,
    RedshiftDescribeReservedNodeOfferingsRequest,
    RedshiftDescribeReservedNodeOfferingsResponse,
    RedshiftDescribeReservedNodesRequest,
    RedshiftDescribeReservedNodesResponse,
    RedshiftDescribeResizeRequest,
    RedshiftDescribeResizeResponse,
    RedshiftDescribeScheduledActionsRequest,
    RedshiftDescribeScheduledActionsResponse,
    RedshiftDescribeSnapshotCopyGrantsRequest,
    RedshiftDescribeSnapshotCopyGrantsResponse,
    RedshiftDescribeSnapshotSchedulesRequest,
    RedshiftDescribeSnapshotSchedulesResponse,
    RedshiftDescribeStorageRequest,
    RedshiftDescribeStorageResponse,
    RedshiftDescribeTableRestoreStatusRequest,
    RedshiftDescribeTableRestoreStatusResponse,
    RedshiftDescribeTagsRequest,
    RedshiftDescribeTagsResponse,
    RedshiftDescribeUsageLimitsRequest,
    RedshiftDescribeUsageLimitsResponse,
    RedshiftDisableLoggingRequest,
    RedshiftDisableLoggingResponse,
    RedshiftDisableSnapshotCopyRequest,
    RedshiftDisableSnapshotCopyResponse,
    RedshiftDisassociateDataShareConsumerRequest,
    RedshiftDisassociateDataShareConsumerResponse,
    RedshiftEnableLoggingRequest,
    RedshiftEnableLoggingResponse,
    RedshiftEnableSnapshotCopyRequest,
    RedshiftEnableSnapshotCopyResponse,
    RedshiftFailoverPrimaryComputeRequest,
    RedshiftFailoverPrimaryComputeResponse,
    RedshiftGetClusterCredentialsRequest,
    RedshiftGetClusterCredentialsResponse,
    RedshiftGetClusterCredentialsWithIAMRequest,
    RedshiftGetClusterCredentialsWithIAMResponse,
    RedshiftGetIdentityCenterAuthTokenRequest,
    RedshiftGetIdentityCenterAuthTokenResponse,
    RedshiftGetReservedNodeExchangeConfigurationOptionsRequest,
    RedshiftGetReservedNodeExchangeConfigurationOptionsResponse,
    RedshiftGetReservedNodeExchangeOfferingsRequest,
    RedshiftGetReservedNodeExchangeOfferingsResponse,
    RedshiftGetResourcePolicyRequest,
    RedshiftGetResourcePolicyResponse,
    RedshiftListRecommendationsRequest,
    RedshiftListRecommendationsResponse,
    RedshiftModifyAquaConfigurationRequest,
    RedshiftModifyAquaConfigurationResponse,
    RedshiftModifyAuthenticationProfileRequest,
    RedshiftModifyAuthenticationProfileResponse,
    RedshiftModifyClusterDbRevisionRequest,
    RedshiftModifyClusterDbRevisionResponse,
    RedshiftModifyClusterIamRolesRequest,
    RedshiftModifyClusterIamRolesResponse,
    RedshiftModifyClusterMaintenanceRequest,
    RedshiftModifyClusterMaintenanceResponse,
    RedshiftModifyClusterParameterGroupRequest,
    RedshiftModifyClusterParameterGroupResponse,
    RedshiftModifyClusterRequest,
    RedshiftModifyClusterResponse,
    RedshiftModifyClusterSnapshotRequest,
    RedshiftModifyClusterSnapshotResponse,
    RedshiftModifyClusterSnapshotScheduleRequest,
    RedshiftModifyClusterSnapshotScheduleResponse,
    RedshiftModifyClusterSubnetGroupRequest,
    RedshiftModifyClusterSubnetGroupResponse,
    RedshiftModifyCustomDomainAssociationRequest,
    RedshiftModifyCustomDomainAssociationResponse,
    RedshiftModifyEndpointAccessRequest,
    RedshiftModifyEndpointAccessResponse,
    RedshiftModifyEventSubscriptionRequest,
    RedshiftModifyEventSubscriptionResponse,
    RedshiftModifyIntegrationRequest,
    RedshiftModifyIntegrationResponse,
    RedshiftModifyLakehouseConfigurationRequest,
    RedshiftModifyLakehouseConfigurationResponse,
    RedshiftModifyQev2IdcApplicationRequest,
    RedshiftModifyQev2IdcApplicationResponse,
    RedshiftModifyRedshiftIdcApplicationRequest,
    RedshiftModifyRedshiftIdcApplicationResponse,
    RedshiftModifyScheduledActionRequest,
    RedshiftModifyScheduledActionResponse,
    RedshiftModifySnapshotCopyRetentionPeriodRequest,
    RedshiftModifySnapshotCopyRetentionPeriodResponse,
    RedshiftModifySnapshotScheduleRequest,
    RedshiftModifySnapshotScheduleResponse,
    RedshiftModifyUsageLimitRequest,
    RedshiftModifyUsageLimitResponse,
    RedshiftPauseClusterRequest,
    RedshiftPauseClusterResponse,
    RedshiftPurchaseReservedNodeOfferingRequest,
    RedshiftPurchaseReservedNodeOfferingResponse,
    RedshiftPutResourcePolicyRequest,
    RedshiftPutResourcePolicyResponse,
    RedshiftRebootClusterRequest,
    RedshiftRebootClusterResponse,
    RedshiftRegisterNamespaceRequest,
    RedshiftRegisterNamespaceResponse,
    RedshiftRejectDataShareRequest,
    RedshiftRejectDataShareResponse,
    RedshiftResetClusterParameterGroupRequest,
    RedshiftResetClusterParameterGroupResponse,
    RedshiftResizeClusterRequest,
    RedshiftResizeClusterResponse,
    RedshiftRestoreFromClusterSnapshotRequest,
    RedshiftRestoreFromClusterSnapshotResponse,
    RedshiftRestoreTableFromClusterSnapshotRequest,
    RedshiftRestoreTableFromClusterSnapshotResponse,
    RedshiftResumeClusterRequest,
    RedshiftResumeClusterResponse,
    RedshiftRevokeClusterSecurityGroupIngressRequest,
    RedshiftRevokeClusterSecurityGroupIngressResponse,
    RedshiftRevokeEndpointAccessRequest,
    RedshiftRevokeEndpointAccessResponse,
    RedshiftRevokeSnapshotAccessRequest,
    RedshiftRevokeSnapshotAccessResponse,
    RedshiftRotateEncryptionKeyRequest,
    RedshiftRotateEncryptionKeyResponse,
    RedshiftUpdatePartnerStatusRequest,
    RedshiftUpdatePartnerStatusResponse,
)
from werkflow_aws.types.redshift_client import RedshiftClient
from .base import AWSBaseService


class AWSRedshift(AWSBaseService[RedshiftClient]):
    service_name = 'redshift'
    boto3_service_name = 'redshift'

    def __init__(self) -> None:
        super().__init__(service_name='redshift', boto3_service_name='redshift')

    async def accept_reserved_node_exchange(
        self,
        request: RedshiftAcceptReservedNodeExchangeRequest,
    ) -> RedshiftAcceptReservedNodeExchangeResponse:
        client = self._require_client()
        return await self._execute(client.accept_reserved_node_exchange, request, RedshiftAcceptReservedNodeExchangeResponse)

    async def add_partner(
        self,
        request: RedshiftAddPartnerRequest,
    ) -> RedshiftAddPartnerResponse:
        client = self._require_client()
        return await self._execute(client.add_partner, request, RedshiftAddPartnerResponse)

    async def associate_data_share_consumer(
        self,
        request: RedshiftAssociateDataShareConsumerRequest,
    ) -> RedshiftAssociateDataShareConsumerResponse:
        client = self._require_client()
        return await self._execute(client.associate_data_share_consumer, request, RedshiftAssociateDataShareConsumerResponse)

    async def authorize_cluster_security_group_ingress(
        self,
        request: RedshiftAuthorizeClusterSecurityGroupIngressRequest,
    ) -> RedshiftAuthorizeClusterSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_cluster_security_group_ingress, request, RedshiftAuthorizeClusterSecurityGroupIngressResponse)

    async def authorize_data_share(
        self,
        request: RedshiftAuthorizeDataShareRequest,
    ) -> RedshiftAuthorizeDataShareResponse:
        client = self._require_client()
        return await self._execute(client.authorize_data_share, request, RedshiftAuthorizeDataShareResponse)

    async def authorize_endpoint_access(
        self,
        request: RedshiftAuthorizeEndpointAccessRequest,
    ) -> RedshiftAuthorizeEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.authorize_endpoint_access, request, RedshiftAuthorizeEndpointAccessResponse)

    async def authorize_snapshot_access(
        self,
        request: RedshiftAuthorizeSnapshotAccessRequest,
    ) -> RedshiftAuthorizeSnapshotAccessResponse:
        client = self._require_client()
        return await self._execute(client.authorize_snapshot_access, request, RedshiftAuthorizeSnapshotAccessResponse)

    async def batch_delete_cluster_snapshots(
        self,
        request: RedshiftBatchDeleteClusterSnapshotsRequest,
    ) -> RedshiftBatchDeleteClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_cluster_snapshots, request, RedshiftBatchDeleteClusterSnapshotsResponse)

    async def batch_modify_cluster_snapshots(
        self,
        request: RedshiftBatchModifyClusterSnapshotsRequest,
    ) -> RedshiftBatchModifyClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.batch_modify_cluster_snapshots, request, RedshiftBatchModifyClusterSnapshotsResponse)

    async def cancel_resize(
        self,
        request: RedshiftCancelResizeRequest,
    ) -> RedshiftCancelResizeResponse:
        client = self._require_client()
        return await self._execute(client.cancel_resize, request, RedshiftCancelResizeResponse)

    async def copy_cluster_snapshot(
        self,
        request: RedshiftCopyClusterSnapshotRequest,
    ) -> RedshiftCopyClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_cluster_snapshot, request, RedshiftCopyClusterSnapshotResponse)

    async def create_authentication_profile(
        self,
        request: RedshiftCreateAuthenticationProfileRequest,
    ) -> RedshiftCreateAuthenticationProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_authentication_profile, request, RedshiftCreateAuthenticationProfileResponse)

    async def create_cluster(
        self,
        request: RedshiftCreateClusterRequest,
    ) -> RedshiftCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, RedshiftCreateClusterResponse)

    async def create_cluster_parameter_group(
        self,
        request: RedshiftCreateClusterParameterGroupRequest,
    ) -> RedshiftCreateClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_parameter_group, request, RedshiftCreateClusterParameterGroupResponse)

    async def create_cluster_security_group(
        self,
        request: RedshiftCreateClusterSecurityGroupRequest,
    ) -> RedshiftCreateClusterSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_security_group, request, RedshiftCreateClusterSecurityGroupResponse)

    async def create_cluster_snapshot(
        self,
        request: RedshiftCreateClusterSnapshotRequest,
    ) -> RedshiftCreateClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_snapshot, request, RedshiftCreateClusterSnapshotResponse)

    async def create_cluster_subnet_group(
        self,
        request: RedshiftCreateClusterSubnetGroupRequest,
    ) -> RedshiftCreateClusterSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_subnet_group, request, RedshiftCreateClusterSubnetGroupResponse)

    async def create_custom_domain_association(
        self,
        request: RedshiftCreateCustomDomainAssociationRequest,
    ) -> RedshiftCreateCustomDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_domain_association, request, RedshiftCreateCustomDomainAssociationResponse)

    async def create_endpoint_access(
        self,
        request: RedshiftCreateEndpointAccessRequest,
    ) -> RedshiftCreateEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.create_endpoint_access, request, RedshiftCreateEndpointAccessResponse)

    async def create_event_subscription(
        self,
        request: RedshiftCreateEventSubscriptionRequest,
    ) -> RedshiftCreateEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_event_subscription, request, RedshiftCreateEventSubscriptionResponse)

    async def create_hsm_client_certificate(
        self,
        request: RedshiftCreateHsmClientCertificateRequest,
    ) -> RedshiftCreateHsmClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.create_hsm_client_certificate, request, RedshiftCreateHsmClientCertificateResponse)

    async def create_hsm_configuration(
        self,
        request: RedshiftCreateHsmConfigurationRequest,
    ) -> RedshiftCreateHsmConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_hsm_configuration, request, RedshiftCreateHsmConfigurationResponse)

    async def create_integration(
        self,
        request: RedshiftCreateIntegrationRequest,
    ) -> RedshiftCreateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.create_integration, request, RedshiftCreateIntegrationResponse)

    async def create_qev2_idc_application(
        self,
        request: RedshiftCreateQev2IdcApplicationRequest,
    ) -> RedshiftCreateQev2IdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_qev2_idc_application, request, RedshiftCreateQev2IdcApplicationResponse)

    async def create_redshift_idc_application(
        self,
        request: RedshiftCreateRedshiftIdcApplicationRequest,
    ) -> RedshiftCreateRedshiftIdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_redshift_idc_application, request, RedshiftCreateRedshiftIdcApplicationResponse)

    async def create_scheduled_action(
        self,
        request: RedshiftCreateScheduledActionRequest,
    ) -> RedshiftCreateScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.create_scheduled_action, request, RedshiftCreateScheduledActionResponse)

    async def create_snapshot_copy_grant(
        self,
        request: RedshiftCreateSnapshotCopyGrantRequest,
    ) -> RedshiftCreateSnapshotCopyGrantResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot_copy_grant, request, RedshiftCreateSnapshotCopyGrantResponse)

    async def create_snapshot_schedule(
        self,
        request: RedshiftCreateSnapshotScheduleRequest | None = None,
    ) -> RedshiftCreateSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot_schedule, request, RedshiftCreateSnapshotScheduleResponse)

    async def create_tags(
        self,
        request: RedshiftCreateTagsRequest,
    ) -> RedshiftCreateTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_tags, request, RedshiftCreateTagsResponse)

    async def create_usage_limit(
        self,
        request: RedshiftCreateUsageLimitRequest,
    ) -> RedshiftCreateUsageLimitResponse:
        client = self._require_client()
        return await self._execute(client.create_usage_limit, request, RedshiftCreateUsageLimitResponse)

    async def deauthorize_data_share(
        self,
        request: RedshiftDeauthorizeDataShareRequest,
    ) -> RedshiftDeauthorizeDataShareResponse:
        client = self._require_client()
        return await self._execute(client.deauthorize_data_share, request, RedshiftDeauthorizeDataShareResponse)

    async def delete_authentication_profile(
        self,
        request: RedshiftDeleteAuthenticationProfileRequest,
    ) -> RedshiftDeleteAuthenticationProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_authentication_profile, request, RedshiftDeleteAuthenticationProfileResponse)

    async def delete_cluster(
        self,
        request: RedshiftDeleteClusterRequest,
    ) -> RedshiftDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, RedshiftDeleteClusterResponse)

    async def delete_cluster_parameter_group(
        self,
        request: RedshiftDeleteClusterParameterGroupRequest,
    ) -> RedshiftDeleteClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_parameter_group, request, RedshiftDeleteClusterParameterGroupResponse)

    async def delete_cluster_security_group(
        self,
        request: RedshiftDeleteClusterSecurityGroupRequest,
    ) -> RedshiftDeleteClusterSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_security_group, request, RedshiftDeleteClusterSecurityGroupResponse)

    async def delete_cluster_snapshot(
        self,
        request: RedshiftDeleteClusterSnapshotRequest,
    ) -> RedshiftDeleteClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_snapshot, request, RedshiftDeleteClusterSnapshotResponse)

    async def delete_cluster_subnet_group(
        self,
        request: RedshiftDeleteClusterSubnetGroupRequest,
    ) -> RedshiftDeleteClusterSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_subnet_group, request, RedshiftDeleteClusterSubnetGroupResponse)

    async def delete_custom_domain_association(
        self,
        request: RedshiftDeleteCustomDomainAssociationRequest,
    ) -> RedshiftDeleteCustomDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_domain_association, request, RedshiftDeleteCustomDomainAssociationResponse)

    async def delete_endpoint_access(
        self,
        request: RedshiftDeleteEndpointAccessRequest,
    ) -> RedshiftDeleteEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint_access, request, RedshiftDeleteEndpointAccessResponse)

    async def delete_event_subscription(
        self,
        request: RedshiftDeleteEventSubscriptionRequest,
    ) -> RedshiftDeleteEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_subscription, request, RedshiftDeleteEventSubscriptionResponse)

    async def delete_hsm_client_certificate(
        self,
        request: RedshiftDeleteHsmClientCertificateRequest,
    ) -> RedshiftDeleteHsmClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_hsm_client_certificate, request, RedshiftDeleteHsmClientCertificateResponse)

    async def delete_hsm_configuration(
        self,
        request: RedshiftDeleteHsmConfigurationRequest,
    ) -> RedshiftDeleteHsmConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_hsm_configuration, request, RedshiftDeleteHsmConfigurationResponse)

    async def delete_integration(
        self,
        request: RedshiftDeleteIntegrationRequest,
    ) -> RedshiftDeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, RedshiftDeleteIntegrationResponse)

    async def delete_partner(
        self,
        request: RedshiftDeletePartnerRequest,
    ) -> RedshiftDeletePartnerResponse:
        client = self._require_client()
        return await self._execute(client.delete_partner, request, RedshiftDeletePartnerResponse)

    async def delete_qev2_idc_application(
        self,
        request: RedshiftDeleteQev2IdcApplicationRequest,
    ) -> RedshiftDeleteQev2IdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_qev2_idc_application, request, RedshiftDeleteQev2IdcApplicationResponse)

    async def delete_redshift_idc_application(
        self,
        request: RedshiftDeleteRedshiftIdcApplicationRequest,
    ) -> RedshiftDeleteRedshiftIdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_redshift_idc_application, request, RedshiftDeleteRedshiftIdcApplicationResponse)

    async def delete_resource_policy(
        self,
        request: RedshiftDeleteResourcePolicyRequest,
    ) -> RedshiftDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, RedshiftDeleteResourcePolicyResponse)

    async def delete_scheduled_action(
        self,
        request: RedshiftDeleteScheduledActionRequest,
    ) -> RedshiftDeleteScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduled_action, request, RedshiftDeleteScheduledActionResponse)

    async def delete_snapshot_copy_grant(
        self,
        request: RedshiftDeleteSnapshotCopyGrantRequest,
    ) -> RedshiftDeleteSnapshotCopyGrantResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot_copy_grant, request, RedshiftDeleteSnapshotCopyGrantResponse)

    async def delete_snapshot_schedule(
        self,
        request: RedshiftDeleteSnapshotScheduleRequest,
    ) -> RedshiftDeleteSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot_schedule, request, RedshiftDeleteSnapshotScheduleResponse)

    async def delete_tags(
        self,
        request: RedshiftDeleteTagsRequest,
    ) -> RedshiftDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, RedshiftDeleteTagsResponse)

    async def delete_usage_limit(
        self,
        request: RedshiftDeleteUsageLimitRequest,
    ) -> RedshiftDeleteUsageLimitResponse:
        client = self._require_client()
        return await self._execute(client.delete_usage_limit, request, RedshiftDeleteUsageLimitResponse)

    async def deregister_namespace(
        self,
        request: RedshiftDeregisterNamespaceRequest,
    ) -> RedshiftDeregisterNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.deregister_namespace, request, RedshiftDeregisterNamespaceResponse)

    async def describe_account_attributes(
        self,
        request: RedshiftDescribeAccountAttributesRequest | None = None,
    ) -> RedshiftDescribeAccountAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_attributes, request, RedshiftDescribeAccountAttributesResponse)

    async def describe_authentication_profiles(
        self,
        request: RedshiftDescribeAuthenticationProfilesRequest | None = None,
    ) -> RedshiftDescribeAuthenticationProfilesResponse:
        client = self._require_client()
        return await self._execute(client.describe_authentication_profiles, request, RedshiftDescribeAuthenticationProfilesResponse)

    async def describe_cluster_db_revisions(
        self,
        request: RedshiftDescribeClusterDbRevisionsRequest | None = None,
    ) -> RedshiftDescribeClusterDbRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_db_revisions, request, RedshiftDescribeClusterDbRevisionsResponse)

    async def describe_cluster_db_revisions_paginated(
        self,
        request: RedshiftDescribeClusterDbRevisionsRequest | None = None,
    ) -> list[RedshiftDescribeClusterDbRevisionsResponse]:
        return await self._paginate('describe_cluster_db_revisions', request, RedshiftDescribeClusterDbRevisionsResponse)

    async def describe_cluster_parameter_groups(
        self,
        request: RedshiftDescribeClusterParameterGroupsRequest | None = None,
    ) -> RedshiftDescribeClusterParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_parameter_groups, request, RedshiftDescribeClusterParameterGroupsResponse)

    async def describe_cluster_parameter_groups_paginated(
        self,
        request: RedshiftDescribeClusterParameterGroupsRequest | None = None,
    ) -> list[RedshiftDescribeClusterParameterGroupsResponse]:
        return await self._paginate('describe_cluster_parameter_groups', request, RedshiftDescribeClusterParameterGroupsResponse)

    async def describe_cluster_parameters(
        self,
        request: RedshiftDescribeClusterParametersRequest,
    ) -> RedshiftDescribeClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_parameters, request, RedshiftDescribeClusterParametersResponse)

    async def describe_cluster_parameters_paginated(
        self,
        request: RedshiftDescribeClusterParametersRequest,
    ) -> list[RedshiftDescribeClusterParametersResponse]:
        return await self._paginate('describe_cluster_parameters', request, RedshiftDescribeClusterParametersResponse)

    async def describe_cluster_security_groups(
        self,
        request: RedshiftDescribeClusterSecurityGroupsRequest | None = None,
    ) -> RedshiftDescribeClusterSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_security_groups, request, RedshiftDescribeClusterSecurityGroupsResponse)

    async def describe_cluster_security_groups_paginated(
        self,
        request: RedshiftDescribeClusterSecurityGroupsRequest | None = None,
    ) -> list[RedshiftDescribeClusterSecurityGroupsResponse]:
        return await self._paginate('describe_cluster_security_groups', request, RedshiftDescribeClusterSecurityGroupsResponse)

    async def describe_cluster_snapshots(
        self,
        request: RedshiftDescribeClusterSnapshotsRequest | None = None,
    ) -> RedshiftDescribeClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_snapshots, request, RedshiftDescribeClusterSnapshotsResponse)

    async def describe_cluster_snapshots_paginated(
        self,
        request: RedshiftDescribeClusterSnapshotsRequest | None = None,
    ) -> list[RedshiftDescribeClusterSnapshotsResponse]:
        return await self._paginate('describe_cluster_snapshots', request, RedshiftDescribeClusterSnapshotsResponse)

    async def describe_cluster_subnet_groups(
        self,
        request: RedshiftDescribeClusterSubnetGroupsRequest | None = None,
    ) -> RedshiftDescribeClusterSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_subnet_groups, request, RedshiftDescribeClusterSubnetGroupsResponse)

    async def describe_cluster_subnet_groups_paginated(
        self,
        request: RedshiftDescribeClusterSubnetGroupsRequest | None = None,
    ) -> list[RedshiftDescribeClusterSubnetGroupsResponse]:
        return await self._paginate('describe_cluster_subnet_groups', request, RedshiftDescribeClusterSubnetGroupsResponse)

    async def describe_cluster_tracks(
        self,
        request: RedshiftDescribeClusterTracksRequest | None = None,
    ) -> RedshiftDescribeClusterTracksResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_tracks, request, RedshiftDescribeClusterTracksResponse)

    async def describe_cluster_tracks_paginated(
        self,
        request: RedshiftDescribeClusterTracksRequest | None = None,
    ) -> list[RedshiftDescribeClusterTracksResponse]:
        return await self._paginate('describe_cluster_tracks', request, RedshiftDescribeClusterTracksResponse)

    async def describe_cluster_versions(
        self,
        request: RedshiftDescribeClusterVersionsRequest | None = None,
    ) -> RedshiftDescribeClusterVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_versions, request, RedshiftDescribeClusterVersionsResponse)

    async def describe_cluster_versions_paginated(
        self,
        request: RedshiftDescribeClusterVersionsRequest | None = None,
    ) -> list[RedshiftDescribeClusterVersionsResponse]:
        return await self._paginate('describe_cluster_versions', request, RedshiftDescribeClusterVersionsResponse)

    async def describe_clusters(
        self,
        request: RedshiftDescribeClustersRequest | None = None,
    ) -> RedshiftDescribeClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_clusters, request, RedshiftDescribeClustersResponse)

    async def describe_clusters_paginated(
        self,
        request: RedshiftDescribeClustersRequest | None = None,
    ) -> list[RedshiftDescribeClustersResponse]:
        return await self._paginate('describe_clusters', request, RedshiftDescribeClustersResponse)

    async def describe_custom_domain_associations(
        self,
        request: RedshiftDescribeCustomDomainAssociationsRequest | None = None,
    ) -> RedshiftDescribeCustomDomainAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_domain_associations, request, RedshiftDescribeCustomDomainAssociationsResponse)

    async def describe_custom_domain_associations_paginated(
        self,
        request: RedshiftDescribeCustomDomainAssociationsRequest | None = None,
    ) -> list[RedshiftDescribeCustomDomainAssociationsResponse]:
        return await self._paginate('describe_custom_domain_associations', request, RedshiftDescribeCustomDomainAssociationsResponse)

    async def describe_data_shares(
        self,
        request: RedshiftDescribeDataSharesRequest | None = None,
    ) -> RedshiftDescribeDataSharesResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_shares, request, RedshiftDescribeDataSharesResponse)

    async def describe_data_shares_paginated(
        self,
        request: RedshiftDescribeDataSharesRequest | None = None,
    ) -> list[RedshiftDescribeDataSharesResponse]:
        return await self._paginate('describe_data_shares', request, RedshiftDescribeDataSharesResponse)

    async def describe_data_shares_for_consumer(
        self,
        request: RedshiftDescribeDataSharesForConsumerRequest | None = None,
    ) -> RedshiftDescribeDataSharesForConsumerResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_shares_for_consumer, request, RedshiftDescribeDataSharesForConsumerResponse)

    async def describe_data_shares_for_consumer_paginated(
        self,
        request: RedshiftDescribeDataSharesForConsumerRequest | None = None,
    ) -> list[RedshiftDescribeDataSharesForConsumerResponse]:
        return await self._paginate('describe_data_shares_for_consumer', request, RedshiftDescribeDataSharesForConsumerResponse)

    async def describe_data_shares_for_producer(
        self,
        request: RedshiftDescribeDataSharesForProducerRequest | None = None,
    ) -> RedshiftDescribeDataSharesForProducerResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_shares_for_producer, request, RedshiftDescribeDataSharesForProducerResponse)

    async def describe_data_shares_for_producer_paginated(
        self,
        request: RedshiftDescribeDataSharesForProducerRequest | None = None,
    ) -> list[RedshiftDescribeDataSharesForProducerResponse]:
        return await self._paginate('describe_data_shares_for_producer', request, RedshiftDescribeDataSharesForProducerResponse)

    async def describe_default_cluster_parameters(
        self,
        request: RedshiftDescribeDefaultClusterParametersRequest,
    ) -> RedshiftDescribeDefaultClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_default_cluster_parameters, request, RedshiftDescribeDefaultClusterParametersResponse)

    async def describe_default_cluster_parameters_paginated(
        self,
        request: RedshiftDescribeDefaultClusterParametersRequest,
    ) -> list[RedshiftDescribeDefaultClusterParametersResponse]:
        return await self._paginate('describe_default_cluster_parameters', request, RedshiftDescribeDefaultClusterParametersResponse)

    async def describe_endpoint_access(
        self,
        request: RedshiftDescribeEndpointAccessRequest | None = None,
    ) -> RedshiftDescribeEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint_access, request, RedshiftDescribeEndpointAccessResponse)

    async def describe_endpoint_access_paginated(
        self,
        request: RedshiftDescribeEndpointAccessRequest | None = None,
    ) -> list[RedshiftDescribeEndpointAccessResponse]:
        return await self._paginate('describe_endpoint_access', request, RedshiftDescribeEndpointAccessResponse)

    async def describe_endpoint_authorization(
        self,
        request: RedshiftDescribeEndpointAuthorizationRequest | None = None,
    ) -> RedshiftDescribeEndpointAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint_authorization, request, RedshiftDescribeEndpointAuthorizationResponse)

    async def describe_endpoint_authorization_paginated(
        self,
        request: RedshiftDescribeEndpointAuthorizationRequest | None = None,
    ) -> list[RedshiftDescribeEndpointAuthorizationResponse]:
        return await self._paginate('describe_endpoint_authorization', request, RedshiftDescribeEndpointAuthorizationResponse)

    async def describe_event_categories(
        self,
        request: RedshiftDescribeEventCategoriesRequest | None = None,
    ) -> RedshiftDescribeEventCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_categories, request, RedshiftDescribeEventCategoriesResponse)

    async def describe_event_subscriptions(
        self,
        request: RedshiftDescribeEventSubscriptionsRequest | None = None,
    ) -> RedshiftDescribeEventSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_subscriptions, request, RedshiftDescribeEventSubscriptionsResponse)

    async def describe_event_subscriptions_paginated(
        self,
        request: RedshiftDescribeEventSubscriptionsRequest | None = None,
    ) -> list[RedshiftDescribeEventSubscriptionsResponse]:
        return await self._paginate('describe_event_subscriptions', request, RedshiftDescribeEventSubscriptionsResponse)

    async def describe_events(
        self,
        request: RedshiftDescribeEventsRequest | None = None,
    ) -> RedshiftDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, RedshiftDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: RedshiftDescribeEventsRequest | None = None,
    ) -> list[RedshiftDescribeEventsResponse]:
        return await self._paginate('describe_events', request, RedshiftDescribeEventsResponse)

    async def describe_hsm_client_certificates(
        self,
        request: RedshiftDescribeHsmClientCertificatesRequest | None = None,
    ) -> RedshiftDescribeHsmClientCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_hsm_client_certificates, request, RedshiftDescribeHsmClientCertificatesResponse)

    async def describe_hsm_client_certificates_paginated(
        self,
        request: RedshiftDescribeHsmClientCertificatesRequest | None = None,
    ) -> list[RedshiftDescribeHsmClientCertificatesResponse]:
        return await self._paginate('describe_hsm_client_certificates', request, RedshiftDescribeHsmClientCertificatesResponse)

    async def describe_hsm_configurations(
        self,
        request: RedshiftDescribeHsmConfigurationsRequest | None = None,
    ) -> RedshiftDescribeHsmConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_hsm_configurations, request, RedshiftDescribeHsmConfigurationsResponse)

    async def describe_hsm_configurations_paginated(
        self,
        request: RedshiftDescribeHsmConfigurationsRequest | None = None,
    ) -> list[RedshiftDescribeHsmConfigurationsResponse]:
        return await self._paginate('describe_hsm_configurations', request, RedshiftDescribeHsmConfigurationsResponse)

    async def describe_inbound_integrations(
        self,
        request: RedshiftDescribeInboundIntegrationsRequest | None = None,
    ) -> RedshiftDescribeInboundIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_inbound_integrations, request, RedshiftDescribeInboundIntegrationsResponse)

    async def describe_inbound_integrations_paginated(
        self,
        request: RedshiftDescribeInboundIntegrationsRequest | None = None,
    ) -> list[RedshiftDescribeInboundIntegrationsResponse]:
        return await self._paginate('describe_inbound_integrations', request, RedshiftDescribeInboundIntegrationsResponse)

    async def describe_integrations(
        self,
        request: RedshiftDescribeIntegrationsRequest | None = None,
    ) -> RedshiftDescribeIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_integrations, request, RedshiftDescribeIntegrationsResponse)

    async def describe_integrations_paginated(
        self,
        request: RedshiftDescribeIntegrationsRequest | None = None,
    ) -> list[RedshiftDescribeIntegrationsResponse]:
        return await self._paginate('describe_integrations', request, RedshiftDescribeIntegrationsResponse)

    async def describe_logging_status(
        self,
        request: RedshiftDescribeLoggingStatusRequest,
    ) -> RedshiftDescribeLoggingStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_logging_status, request, RedshiftDescribeLoggingStatusResponse)

    async def describe_node_configuration_options(
        self,
        request: RedshiftDescribeNodeConfigurationOptionsRequest,
    ) -> RedshiftDescribeNodeConfigurationOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_node_configuration_options, request, RedshiftDescribeNodeConfigurationOptionsResponse)

    async def describe_node_configuration_options_paginated(
        self,
        request: RedshiftDescribeNodeConfigurationOptionsRequest,
    ) -> list[RedshiftDescribeNodeConfigurationOptionsResponse]:
        return await self._paginate('describe_node_configuration_options', request, RedshiftDescribeNodeConfigurationOptionsResponse)

    async def describe_orderable_cluster_options(
        self,
        request: RedshiftDescribeOrderableClusterOptionsRequest | None = None,
    ) -> RedshiftDescribeOrderableClusterOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_orderable_cluster_options, request, RedshiftDescribeOrderableClusterOptionsResponse)

    async def describe_orderable_cluster_options_paginated(
        self,
        request: RedshiftDescribeOrderableClusterOptionsRequest | None = None,
    ) -> list[RedshiftDescribeOrderableClusterOptionsResponse]:
        return await self._paginate('describe_orderable_cluster_options', request, RedshiftDescribeOrderableClusterOptionsResponse)

    async def describe_partners(
        self,
        request: RedshiftDescribePartnersRequest,
    ) -> RedshiftDescribePartnersResponse:
        client = self._require_client()
        return await self._execute(client.describe_partners, request, RedshiftDescribePartnersResponse)

    async def describe_qev2_idc_applications(
        self,
        request: RedshiftDescribeQev2IdcApplicationsRequest | None = None,
    ) -> RedshiftDescribeQev2IdcApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_qev2_idc_applications, request, RedshiftDescribeQev2IdcApplicationsResponse)

    async def describe_qev2_idc_applications_paginated(
        self,
        request: RedshiftDescribeQev2IdcApplicationsRequest | None = None,
    ) -> list[RedshiftDescribeQev2IdcApplicationsResponse]:
        return await self._paginate('describe_qev2_idc_applications', request, RedshiftDescribeQev2IdcApplicationsResponse)

    async def describe_redshift_idc_applications(
        self,
        request: RedshiftDescribeRedshiftIdcApplicationsRequest | None = None,
    ) -> RedshiftDescribeRedshiftIdcApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_redshift_idc_applications, request, RedshiftDescribeRedshiftIdcApplicationsResponse)

    async def describe_redshift_idc_applications_paginated(
        self,
        request: RedshiftDescribeRedshiftIdcApplicationsRequest | None = None,
    ) -> list[RedshiftDescribeRedshiftIdcApplicationsResponse]:
        return await self._paginate('describe_redshift_idc_applications', request, RedshiftDescribeRedshiftIdcApplicationsResponse)

    async def describe_reserved_node_exchange_status(
        self,
        request: RedshiftDescribeReservedNodeExchangeStatusRequest | None = None,
    ) -> RedshiftDescribeReservedNodeExchangeStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_node_exchange_status, request, RedshiftDescribeReservedNodeExchangeStatusResponse)

    async def describe_reserved_node_exchange_status_paginated(
        self,
        request: RedshiftDescribeReservedNodeExchangeStatusRequest | None = None,
    ) -> list[RedshiftDescribeReservedNodeExchangeStatusResponse]:
        return await self._paginate('describe_reserved_node_exchange_status', request, RedshiftDescribeReservedNodeExchangeStatusResponse)

    async def describe_reserved_node_offerings(
        self,
        request: RedshiftDescribeReservedNodeOfferingsRequest | None = None,
    ) -> RedshiftDescribeReservedNodeOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_node_offerings, request, RedshiftDescribeReservedNodeOfferingsResponse)

    async def describe_reserved_node_offerings_paginated(
        self,
        request: RedshiftDescribeReservedNodeOfferingsRequest | None = None,
    ) -> list[RedshiftDescribeReservedNodeOfferingsResponse]:
        return await self._paginate('describe_reserved_node_offerings', request, RedshiftDescribeReservedNodeOfferingsResponse)

    async def describe_reserved_nodes(
        self,
        request: RedshiftDescribeReservedNodesRequest | None = None,
    ) -> RedshiftDescribeReservedNodesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_nodes, request, RedshiftDescribeReservedNodesResponse)

    async def describe_reserved_nodes_paginated(
        self,
        request: RedshiftDescribeReservedNodesRequest | None = None,
    ) -> list[RedshiftDescribeReservedNodesResponse]:
        return await self._paginate('describe_reserved_nodes', request, RedshiftDescribeReservedNodesResponse)

    async def describe_resize(
        self,
        request: RedshiftDescribeResizeRequest,
    ) -> RedshiftDescribeResizeResponse:
        client = self._require_client()
        return await self._execute(client.describe_resize, request, RedshiftDescribeResizeResponse)

    async def describe_scheduled_actions(
        self,
        request: RedshiftDescribeScheduledActionsRequest | None = None,
    ) -> RedshiftDescribeScheduledActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_actions, request, RedshiftDescribeScheduledActionsResponse)

    async def describe_scheduled_actions_paginated(
        self,
        request: RedshiftDescribeScheduledActionsRequest | None = None,
    ) -> list[RedshiftDescribeScheduledActionsResponse]:
        return await self._paginate('describe_scheduled_actions', request, RedshiftDescribeScheduledActionsResponse)

    async def describe_snapshot_copy_grants(
        self,
        request: RedshiftDescribeSnapshotCopyGrantsRequest | None = None,
    ) -> RedshiftDescribeSnapshotCopyGrantsResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_copy_grants, request, RedshiftDescribeSnapshotCopyGrantsResponse)

    async def describe_snapshot_copy_grants_paginated(
        self,
        request: RedshiftDescribeSnapshotCopyGrantsRequest | None = None,
    ) -> list[RedshiftDescribeSnapshotCopyGrantsResponse]:
        return await self._paginate('describe_snapshot_copy_grants', request, RedshiftDescribeSnapshotCopyGrantsResponse)

    async def describe_snapshot_schedules(
        self,
        request: RedshiftDescribeSnapshotSchedulesRequest | None = None,
    ) -> RedshiftDescribeSnapshotSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_schedules, request, RedshiftDescribeSnapshotSchedulesResponse)

    async def describe_snapshot_schedules_paginated(
        self,
        request: RedshiftDescribeSnapshotSchedulesRequest | None = None,
    ) -> list[RedshiftDescribeSnapshotSchedulesResponse]:
        return await self._paginate('describe_snapshot_schedules', request, RedshiftDescribeSnapshotSchedulesResponse)

    async def describe_storage(
        self,
        request: RedshiftDescribeStorageRequest | None = None,
    ) -> RedshiftDescribeStorageResponse:
        client = self._require_client()
        return await self._execute(client.describe_storage, request, RedshiftDescribeStorageResponse)

    async def describe_table_restore_status(
        self,
        request: RedshiftDescribeTableRestoreStatusRequest | None = None,
    ) -> RedshiftDescribeTableRestoreStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_table_restore_status, request, RedshiftDescribeTableRestoreStatusResponse)

    async def describe_table_restore_status_paginated(
        self,
        request: RedshiftDescribeTableRestoreStatusRequest | None = None,
    ) -> list[RedshiftDescribeTableRestoreStatusResponse]:
        return await self._paginate('describe_table_restore_status', request, RedshiftDescribeTableRestoreStatusResponse)

    async def describe_tags(
        self,
        request: RedshiftDescribeTagsRequest | None = None,
    ) -> RedshiftDescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, RedshiftDescribeTagsResponse)

    async def describe_tags_paginated(
        self,
        request: RedshiftDescribeTagsRequest | None = None,
    ) -> list[RedshiftDescribeTagsResponse]:
        return await self._paginate('describe_tags', request, RedshiftDescribeTagsResponse)

    async def describe_usage_limits(
        self,
        request: RedshiftDescribeUsageLimitsRequest | None = None,
    ) -> RedshiftDescribeUsageLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_usage_limits, request, RedshiftDescribeUsageLimitsResponse)

    async def describe_usage_limits_paginated(
        self,
        request: RedshiftDescribeUsageLimitsRequest | None = None,
    ) -> list[RedshiftDescribeUsageLimitsResponse]:
        return await self._paginate('describe_usage_limits', request, RedshiftDescribeUsageLimitsResponse)

    async def disable_logging(
        self,
        request: RedshiftDisableLoggingRequest,
    ) -> RedshiftDisableLoggingResponse:
        client = self._require_client()
        return await self._execute(client.disable_logging, request, RedshiftDisableLoggingResponse)

    async def disable_snapshot_copy(
        self,
        request: RedshiftDisableSnapshotCopyRequest,
    ) -> RedshiftDisableSnapshotCopyResponse:
        client = self._require_client()
        return await self._execute(client.disable_snapshot_copy, request, RedshiftDisableSnapshotCopyResponse)

    async def disassociate_data_share_consumer(
        self,
        request: RedshiftDisassociateDataShareConsumerRequest,
    ) -> RedshiftDisassociateDataShareConsumerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_data_share_consumer, request, RedshiftDisassociateDataShareConsumerResponse)

    async def enable_logging(
        self,
        request: RedshiftEnableLoggingRequest,
    ) -> RedshiftEnableLoggingResponse:
        client = self._require_client()
        return await self._execute(client.enable_logging, request, RedshiftEnableLoggingResponse)

    async def enable_snapshot_copy(
        self,
        request: RedshiftEnableSnapshotCopyRequest,
    ) -> RedshiftEnableSnapshotCopyResponse:
        client = self._require_client()
        return await self._execute(client.enable_snapshot_copy, request, RedshiftEnableSnapshotCopyResponse)

    async def failover_primary_compute(
        self,
        request: RedshiftFailoverPrimaryComputeRequest,
    ) -> RedshiftFailoverPrimaryComputeResponse:
        client = self._require_client()
        return await self._execute(client.failover_primary_compute, request, RedshiftFailoverPrimaryComputeResponse)

    async def get_cluster_credentials(
        self,
        request: RedshiftGetClusterCredentialsRequest,
    ) -> RedshiftGetClusterCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_cluster_credentials, request, RedshiftGetClusterCredentialsResponse)

    async def get_cluster_credentials_with_iam(
        self,
        request: RedshiftGetClusterCredentialsWithIAMRequest | None = None,
    ) -> RedshiftGetClusterCredentialsWithIAMResponse:
        client = self._require_client()
        return await self._execute(client.get_cluster_credentials_with_iam, request, RedshiftGetClusterCredentialsWithIAMResponse)

    async def get_identity_center_auth_token(
        self,
        request: RedshiftGetIdentityCenterAuthTokenRequest,
    ) -> RedshiftGetIdentityCenterAuthTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_identity_center_auth_token, request, RedshiftGetIdentityCenterAuthTokenResponse)

    async def get_reserved_node_exchange_configuration_options(
        self,
        request: RedshiftGetReservedNodeExchangeConfigurationOptionsRequest,
    ) -> RedshiftGetReservedNodeExchangeConfigurationOptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_reserved_node_exchange_configuration_options, request, RedshiftGetReservedNodeExchangeConfigurationOptionsResponse)

    async def get_reserved_node_exchange_configuration_options_paginated(
        self,
        request: RedshiftGetReservedNodeExchangeConfigurationOptionsRequest,
    ) -> list[RedshiftGetReservedNodeExchangeConfigurationOptionsResponse]:
        return await self._paginate('get_reserved_node_exchange_configuration_options', request, RedshiftGetReservedNodeExchangeConfigurationOptionsResponse)

    async def get_reserved_node_exchange_offerings(
        self,
        request: RedshiftGetReservedNodeExchangeOfferingsRequest,
    ) -> RedshiftGetReservedNodeExchangeOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.get_reserved_node_exchange_offerings, request, RedshiftGetReservedNodeExchangeOfferingsResponse)

    async def get_reserved_node_exchange_offerings_paginated(
        self,
        request: RedshiftGetReservedNodeExchangeOfferingsRequest,
    ) -> list[RedshiftGetReservedNodeExchangeOfferingsResponse]:
        return await self._paginate('get_reserved_node_exchange_offerings', request, RedshiftGetReservedNodeExchangeOfferingsResponse)

    async def get_resource_policy(
        self,
        request: RedshiftGetResourcePolicyRequest,
    ) -> RedshiftGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, RedshiftGetResourcePolicyResponse)

    async def list_recommendations(
        self,
        request: RedshiftListRecommendationsRequest | None = None,
    ) -> RedshiftListRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendations, request, RedshiftListRecommendationsResponse)

    async def list_recommendations_paginated(
        self,
        request: RedshiftListRecommendationsRequest | None = None,
    ) -> list[RedshiftListRecommendationsResponse]:
        return await self._paginate('list_recommendations', request, RedshiftListRecommendationsResponse)

    async def modify_aqua_configuration(
        self,
        request: RedshiftModifyAquaConfigurationRequest,
    ) -> RedshiftModifyAquaConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_aqua_configuration, request, RedshiftModifyAquaConfigurationResponse)

    async def modify_authentication_profile(
        self,
        request: RedshiftModifyAuthenticationProfileRequest,
    ) -> RedshiftModifyAuthenticationProfileResponse:
        client = self._require_client()
        return await self._execute(client.modify_authentication_profile, request, RedshiftModifyAuthenticationProfileResponse)

    async def modify_cluster(
        self,
        request: RedshiftModifyClusterRequest,
    ) -> RedshiftModifyClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster, request, RedshiftModifyClusterResponse)

    async def modify_cluster_db_revision(
        self,
        request: RedshiftModifyClusterDbRevisionRequest,
    ) -> RedshiftModifyClusterDbRevisionResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_db_revision, request, RedshiftModifyClusterDbRevisionResponse)

    async def modify_cluster_iam_roles(
        self,
        request: RedshiftModifyClusterIamRolesRequest,
    ) -> RedshiftModifyClusterIamRolesResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_iam_roles, request, RedshiftModifyClusterIamRolesResponse)

    async def modify_cluster_maintenance(
        self,
        request: RedshiftModifyClusterMaintenanceRequest,
    ) -> RedshiftModifyClusterMaintenanceResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_maintenance, request, RedshiftModifyClusterMaintenanceResponse)

    async def modify_cluster_parameter_group(
        self,
        request: RedshiftModifyClusterParameterGroupRequest,
    ) -> RedshiftModifyClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_parameter_group, request, RedshiftModifyClusterParameterGroupResponse)

    async def modify_cluster_snapshot(
        self,
        request: RedshiftModifyClusterSnapshotRequest,
    ) -> RedshiftModifyClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_snapshot, request, RedshiftModifyClusterSnapshotResponse)

    async def modify_cluster_snapshot_schedule(
        self,
        request: RedshiftModifyClusterSnapshotScheduleRequest,
    ) -> RedshiftModifyClusterSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_snapshot_schedule, request, RedshiftModifyClusterSnapshotScheduleResponse)

    async def modify_cluster_subnet_group(
        self,
        request: RedshiftModifyClusterSubnetGroupRequest,
    ) -> RedshiftModifyClusterSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster_subnet_group, request, RedshiftModifyClusterSubnetGroupResponse)

    async def modify_custom_domain_association(
        self,
        request: RedshiftModifyCustomDomainAssociationRequest,
    ) -> RedshiftModifyCustomDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.modify_custom_domain_association, request, RedshiftModifyCustomDomainAssociationResponse)

    async def modify_endpoint_access(
        self,
        request: RedshiftModifyEndpointAccessRequest,
    ) -> RedshiftModifyEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.modify_endpoint_access, request, RedshiftModifyEndpointAccessResponse)

    async def modify_event_subscription(
        self,
        request: RedshiftModifyEventSubscriptionRequest,
    ) -> RedshiftModifyEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.modify_event_subscription, request, RedshiftModifyEventSubscriptionResponse)

    async def modify_integration(
        self,
        request: RedshiftModifyIntegrationRequest,
    ) -> RedshiftModifyIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.modify_integration, request, RedshiftModifyIntegrationResponse)

    async def modify_lakehouse_configuration(
        self,
        request: RedshiftModifyLakehouseConfigurationRequest,
    ) -> RedshiftModifyLakehouseConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_lakehouse_configuration, request, RedshiftModifyLakehouseConfigurationResponse)

    async def modify_qev2_idc_application(
        self,
        request: RedshiftModifyQev2IdcApplicationRequest,
    ) -> RedshiftModifyQev2IdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.modify_qev2_idc_application, request, RedshiftModifyQev2IdcApplicationResponse)

    async def modify_redshift_idc_application(
        self,
        request: RedshiftModifyRedshiftIdcApplicationRequest,
    ) -> RedshiftModifyRedshiftIdcApplicationResponse:
        client = self._require_client()
        return await self._execute(client.modify_redshift_idc_application, request, RedshiftModifyRedshiftIdcApplicationResponse)

    async def modify_scheduled_action(
        self,
        request: RedshiftModifyScheduledActionRequest,
    ) -> RedshiftModifyScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.modify_scheduled_action, request, RedshiftModifyScheduledActionResponse)

    async def modify_snapshot_copy_retention_period(
        self,
        request: RedshiftModifySnapshotCopyRetentionPeriodRequest,
    ) -> RedshiftModifySnapshotCopyRetentionPeriodResponse:
        client = self._require_client()
        return await self._execute(client.modify_snapshot_copy_retention_period, request, RedshiftModifySnapshotCopyRetentionPeriodResponse)

    async def modify_snapshot_schedule(
        self,
        request: RedshiftModifySnapshotScheduleRequest,
    ) -> RedshiftModifySnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.modify_snapshot_schedule, request, RedshiftModifySnapshotScheduleResponse)

    async def modify_usage_limit(
        self,
        request: RedshiftModifyUsageLimitRequest,
    ) -> RedshiftModifyUsageLimitResponse:
        client = self._require_client()
        return await self._execute(client.modify_usage_limit, request, RedshiftModifyUsageLimitResponse)

    async def pause_cluster(
        self,
        request: RedshiftPauseClusterRequest,
    ) -> RedshiftPauseClusterResponse:
        client = self._require_client()
        return await self._execute(client.pause_cluster, request, RedshiftPauseClusterResponse)

    async def purchase_reserved_node_offering(
        self,
        request: RedshiftPurchaseReservedNodeOfferingRequest,
    ) -> RedshiftPurchaseReservedNodeOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_node_offering, request, RedshiftPurchaseReservedNodeOfferingResponse)

    async def put_resource_policy(
        self,
        request: RedshiftPutResourcePolicyRequest,
    ) -> RedshiftPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, RedshiftPutResourcePolicyResponse)

    async def reboot_cluster(
        self,
        request: RedshiftRebootClusterRequest,
    ) -> RedshiftRebootClusterResponse:
        client = self._require_client()
        return await self._execute(client.reboot_cluster, request, RedshiftRebootClusterResponse)

    async def register_namespace(
        self,
        request: RedshiftRegisterNamespaceRequest,
    ) -> RedshiftRegisterNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.register_namespace, request, RedshiftRegisterNamespaceResponse)

    async def reject_data_share(
        self,
        request: RedshiftRejectDataShareRequest,
    ) -> RedshiftRejectDataShareResponse:
        client = self._require_client()
        return await self._execute(client.reject_data_share, request, RedshiftRejectDataShareResponse)

    async def reset_cluster_parameter_group(
        self,
        request: RedshiftResetClusterParameterGroupRequest,
    ) -> RedshiftResetClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_cluster_parameter_group, request, RedshiftResetClusterParameterGroupResponse)

    async def resize_cluster(
        self,
        request: RedshiftResizeClusterRequest,
    ) -> RedshiftResizeClusterResponse:
        client = self._require_client()
        return await self._execute(client.resize_cluster, request, RedshiftResizeClusterResponse)

    async def restore_from_cluster_snapshot(
        self,
        request: RedshiftRestoreFromClusterSnapshotRequest,
    ) -> RedshiftRestoreFromClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_from_cluster_snapshot, request, RedshiftRestoreFromClusterSnapshotResponse)

    async def restore_table_from_cluster_snapshot(
        self,
        request: RedshiftRestoreTableFromClusterSnapshotRequest,
    ) -> RedshiftRestoreTableFromClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_table_from_cluster_snapshot, request, RedshiftRestoreTableFromClusterSnapshotResponse)

    async def resume_cluster(
        self,
        request: RedshiftResumeClusterRequest,
    ) -> RedshiftResumeClusterResponse:
        client = self._require_client()
        return await self._execute(client.resume_cluster, request, RedshiftResumeClusterResponse)

    async def revoke_cluster_security_group_ingress(
        self,
        request: RedshiftRevokeClusterSecurityGroupIngressRequest,
    ) -> RedshiftRevokeClusterSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_cluster_security_group_ingress, request, RedshiftRevokeClusterSecurityGroupIngressResponse)

    async def revoke_endpoint_access(
        self,
        request: RedshiftRevokeEndpointAccessRequest | None = None,
    ) -> RedshiftRevokeEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.revoke_endpoint_access, request, RedshiftRevokeEndpointAccessResponse)

    async def revoke_snapshot_access(
        self,
        request: RedshiftRevokeSnapshotAccessRequest,
    ) -> RedshiftRevokeSnapshotAccessResponse:
        client = self._require_client()
        return await self._execute(client.revoke_snapshot_access, request, RedshiftRevokeSnapshotAccessResponse)

    async def rotate_encryption_key(
        self,
        request: RedshiftRotateEncryptionKeyRequest,
    ) -> RedshiftRotateEncryptionKeyResponse:
        client = self._require_client()
        return await self._execute(client.rotate_encryption_key, request, RedshiftRotateEncryptionKeyResponse)

    async def update_partner_status(
        self,
        request: RedshiftUpdatePartnerStatusRequest,
    ) -> RedshiftUpdatePartnerStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_partner_status, request, RedshiftUpdatePartnerStatusResponse)

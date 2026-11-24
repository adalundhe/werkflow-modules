from werkflow_aws.models.ec2 import (
    EC2Attachment,
    EC2AttachVolumeRequest,
    EC2CreateSecurityGroupRequest,
    EC2CreateSecurityGroupResponse,
    EC2CreateSnapshotRequest,
    EC2CreateTagsRequest,
    EC2CreateVolumeRequest,
    EC2DeleteSecurityGroupRequest,
    EC2DeleteSecurityGroupResponse,
    EC2DeleteSnapshotRequest,
    EC2DeleteTagsRequest,
    EC2DeleteVolumeRequest,
    EC2DescribeInstancesRequest,
    EC2DescribeInstancesResponse,
    EC2DescribeKeyPairsRequest,
    EC2DescribeKeyPairsResponse,
    EC2DescribeSecurityGroupsRequest,
    EC2DescribeSecurityGroupsResponse,
    EC2DescribeSnapshotsRequest,
    EC2DescribeSnapshotsResponse,
    EC2DescribeSubnetsRequest,
    EC2DescribeSubnetsResponse,
    EC2DescribeVolumesQuery,
    EC2DescribeVolumesResponse,
    EC2DescribeVpcsRequest,
    EC2DescribeVpcsResponse,
    EC2DetachVolumeRequest,
    EC2EmptyResponse,
    EC2RebootInstancesRequest,
    EC2Reservation,
    EC2RunInstancesRequest,
    EC2Snapshot,
    EC2StartInstancesRequest,
    EC2StartInstancesResponse,
    EC2StopInstancesRequest,
    EC2StopInstancesResponse,
    EC2TerminateInstancesRequest,
    EC2TerminateInstancesResponse,
    EC2Volume,
)
from werkflow_aws.types import EC2Client
from .base import AWSBaseService
from werkflow_aws.models.ec2 import (
    EC2AcceptAddressTransferRequest,
    EC2AcceptAddressTransferResponse,
    EC2AcceptCapacityReservationBillingOwnershipRequest,
    EC2AcceptCapacityReservationBillingOwnershipResponse,
    EC2AcceptReservedInstancesExchangeQuoteRequest,
    EC2AcceptReservedInstancesExchangeQuoteResponse,
    EC2AcceptTransitGatewayClientVpnAttachmentRequest,
    EC2AcceptTransitGatewayClientVpnAttachmentResponse,
    EC2AcceptTransitGatewayMulticastDomainAssociationsRequest,
    EC2AcceptTransitGatewayMulticastDomainAssociationsResponse,
    EC2AcceptTransitGatewayPeeringAttachmentRequest,
    EC2AcceptTransitGatewayPeeringAttachmentResponse,
    EC2AcceptTransitGatewayVpcAttachmentRequest,
    EC2AcceptTransitGatewayVpcAttachmentResponse,
    EC2AcceptVpcEndpointConnectionsRequest,
    EC2AcceptVpcEndpointConnectionsResponse,
    EC2AcceptVpcPeeringConnectionRequest,
    EC2AcceptVpcPeeringConnectionResponse,
    EC2AdvertiseByoipCidrRequest,
    EC2AdvertiseByoipCidrResponse,
    EC2AllocateAddressRequest,
    EC2AllocateAddressResponse,
    EC2AllocateHostsRequest,
    EC2AllocateHostsResponse,
    EC2AllocateIpamPoolCidrRequest,
    EC2AllocateIpamPoolCidrResponse,
    EC2ApplySecurityGroupsToClientVpnTargetNetworkRequest,
    EC2ApplySecurityGroupsToClientVpnTargetNetworkResponse,
    EC2AssignIpv6AddressesRequest,
    EC2AssignIpv6AddressesResponse,
    EC2AssignPrivateIpAddressesRequest,
    EC2AssignPrivateIpAddressesResponse,
    EC2AssignPrivateNatGatewayAddressRequest,
    EC2AssignPrivateNatGatewayAddressResponse,
    EC2AssociateAddressRequest,
    EC2AssociateAddressResponse,
    EC2AssociateApplicationStatusCheckRequest,
    EC2AssociateApplicationStatusCheckResponse,
    EC2AssociateCapacityReservationBillingOwnerRequest,
    EC2AssociateCapacityReservationBillingOwnerResponse,
    EC2AssociateClientVpnTargetNetworkRequest,
    EC2AssociateClientVpnTargetNetworkResponse,
    EC2AssociateDhcpOptionsRequest,
    EC2AssociateDhcpOptionsResponse,
    EC2AssociateEnclaveCertificateIamRoleRequest,
    EC2AssociateEnclaveCertificateIamRoleResponse,
    EC2AssociateIamInstanceProfileRequest,
    EC2AssociateIamInstanceProfileResponse,
    EC2AssociateInstanceEventWindowRequest,
    EC2AssociateInstanceEventWindowResponse,
    EC2AssociateIpamByoasnRequest,
    EC2AssociateIpamByoasnResponse,
    EC2AssociateIpamResourceDiscoveryRequest,
    EC2AssociateIpamResourceDiscoveryResponse,
    EC2AssociateKmsKeyIdRequest,
    EC2AssociateKmsKeyIdResponse,
    EC2AssociateNatGatewayAddressRequest,
    EC2AssociateNatGatewayAddressResponse,
    EC2AssociateNetworkingFlexCostAllocationPolicyRequest,
    EC2AssociateNetworkingFlexCostAllocationPolicyResponse,
    EC2AssociateRouteServerRequest,
    EC2AssociateRouteServerResponse,
    EC2AssociateRouteTableRequest,
    EC2AssociateRouteTableResponse,
    EC2AssociateSecurityGroupVpcRequest,
    EC2AssociateSecurityGroupVpcResponse,
    EC2AssociateSubnetCidrBlockRequest,
    EC2AssociateSubnetCidrBlockResponse,
    EC2AssociateTransitGatewayMulticastDomainRequest,
    EC2AssociateTransitGatewayMulticastDomainResponse,
    EC2AssociateTransitGatewayPolicyTableRequest,
    EC2AssociateTransitGatewayPolicyTableResponse,
    EC2AssociateTransitGatewayRouteTableRequest,
    EC2AssociateTransitGatewayRouteTableResponse,
    EC2AssociateTrunkInterfaceRequest,
    EC2AssociateTrunkInterfaceResponse,
    EC2AssociateVpcCidrBlockRequest,
    EC2AssociateVpcCidrBlockResponse,
    EC2AttachClassicLinkVpcRequest,
    EC2AttachClassicLinkVpcResponse,
    EC2AttachImageWatermarkRequest,
    EC2AttachImageWatermarkResponse,
    EC2AttachInternetGatewayRequest,
    EC2AttachInternetGatewayResponse,
    EC2AttachNetworkInterfaceRequest,
    EC2AttachNetworkInterfaceResponse,
    EC2AttachVerifiedAccessTrustProviderRequest,
    EC2AttachVerifiedAccessTrustProviderResponse,
    EC2AttachVpnGatewayRequest,
    EC2AttachVpnGatewayResponse,
    EC2AuthorizeClientVpnIngressRequest,
    EC2AuthorizeClientVpnIngressResponse,
    EC2AuthorizeSecurityGroupEgressRequest,
    EC2AuthorizeSecurityGroupEgressResponse,
    EC2AuthorizeSecurityGroupIngressRequest,
    EC2AuthorizeSecurityGroupIngressResponse,
    EC2BatchModifyIpamRoutingPolicyRegistrationsRequest,
    EC2BatchModifyIpamRoutingPolicyRegistrationsResponse,
    EC2BundleInstanceRequest,
    EC2BundleInstanceResponse,
    EC2CancelBundleTaskRequest,
    EC2CancelBundleTaskResponse,
    EC2CancelCapacityReservationFleetsRequest,
    EC2CancelCapacityReservationFleetsResponse,
    EC2CancelCapacityReservationRequest,
    EC2CancelCapacityReservationResponse,
    EC2CancelConversionTaskRequest,
    EC2CancelConversionTaskResponse,
    EC2CancelDeclarativePoliciesReportRequest,
    EC2CancelDeclarativePoliciesReportResponse,
    EC2CancelExportTaskRequest,
    EC2CancelExportTaskResponse,
    EC2CancelImageLaunchPermissionRequest,
    EC2CancelImageLaunchPermissionResponse,
    EC2CancelImportTaskRequest,
    EC2CancelImportTaskResponse,
    EC2CancelReservedInstancesListingRequest,
    EC2CancelReservedInstancesListingResponse,
    EC2CancelSpotFleetRequestsRequest,
    EC2CancelSpotFleetRequestsResponse,
    EC2CancelSpotInstanceRequestsRequest,
    EC2CancelSpotInstanceRequestsResponse,
    EC2ConfirmProductInstanceRequest,
    EC2ConfirmProductInstanceResponse,
    EC2CopyFpgaImageRequest,
    EC2CopyFpgaImageResponse,
    EC2CopyImageRequest,
    EC2CopyImageResponse,
    EC2CopySnapshotRequest,
    EC2CopySnapshotResponse,
    EC2CopyVolumesRequest,
    EC2CopyVolumesResponse,
    EC2CreateApplicationStatusCheckRequest,
    EC2CreateApplicationStatusCheckResponse,
    EC2CreateCapacityManagerDataExportRequest,
    EC2CreateCapacityManagerDataExportResponse,
    EC2CreateCapacityReservationBySplittingRequest,
    EC2CreateCapacityReservationBySplittingResponse,
    EC2CreateCapacityReservationCancellationQuoteRequest,
    EC2CreateCapacityReservationCancellationQuoteResponse,
    EC2CreateCapacityReservationDateChangeQuoteRequest,
    EC2CreateCapacityReservationDateChangeQuoteResponse,
    EC2CreateCapacityReservationFleetRequest,
    EC2CreateCapacityReservationFleetResponse,
    EC2CreateCapacityReservationRequest,
    EC2CreateCapacityReservationResponse,
    EC2CreateCarrierGatewayRequest,
    EC2CreateCarrierGatewayResponse,
    EC2CreateClientVpnEndpointRequest,
    EC2CreateClientVpnEndpointResponse,
    EC2CreateClientVpnRouteRequest,
    EC2CreateClientVpnRouteResponse,
    EC2CreateCoipCidrRequest,
    EC2CreateCoipCidrResponse,
    EC2CreateCoipPoolRequest,
    EC2CreateCoipPoolResponse,
    EC2CreateCustomerGatewayRequest,
    EC2CreateCustomerGatewayResponse,
    EC2CreateDefaultSubnetRequest,
    EC2CreateDefaultSubnetResponse,
    EC2CreateDefaultVpcRequest,
    EC2CreateDefaultVpcResponse,
    EC2CreateDelegateMacVolumeOwnershipTaskRequest,
    EC2CreateDelegateMacVolumeOwnershipTaskResponse,
    EC2CreateDhcpOptionsRequest,
    EC2CreateDhcpOptionsResponse,
    EC2CreateEgressOnlyInternetGatewayRequest,
    EC2CreateEgressOnlyInternetGatewayResponse,
    EC2CreateFleetRequest,
    EC2CreateFleetResponse,
    EC2CreateFlowLogsRequest,
    EC2CreateFlowLogsResponse,
    EC2CreateFpgaImageRequest,
    EC2CreateFpgaImageResponse,
    EC2CreateImageRequest,
    EC2CreateImageResponse,
    EC2CreateImageUsageReportRequest,
    EC2CreateImageUsageReportResponse,
    EC2CreateInstanceConnectEndpointRequest,
    EC2CreateInstanceConnectEndpointResponse,
    EC2CreateInstanceEventWindowRequest,
    EC2CreateInstanceEventWindowResponse,
    EC2CreateInstanceExportTaskRequest,
    EC2CreateInstanceExportTaskResponse,
    EC2CreateInternetGatewayRequest,
    EC2CreateInternetGatewayResponse,
    EC2CreateInterruptibleCapacityReservationAllocationRequest,
    EC2CreateInterruptibleCapacityReservationAllocationResponse,
    EC2CreateIpamExternalResourceVerificationTokenRequest,
    EC2CreateIpamExternalResourceVerificationTokenResponse,
    EC2CreateIpamInternetRegistryAssociationRequest,
    EC2CreateIpamInternetRegistryAssociationResponse,
    EC2CreateIpamPolicyRequest,
    EC2CreateIpamPolicyResponse,
    EC2CreateIpamPoolRequest,
    EC2CreateIpamPoolResponse,
    EC2CreateIpamPrefixListResolverRequest,
    EC2CreateIpamPrefixListResolverResponse,
    EC2CreateIpamPrefixListResolverTargetRequest,
    EC2CreateIpamPrefixListResolverTargetResponse,
    EC2CreateIpamRequest,
    EC2CreateIpamResourceDiscoveryRequest,
    EC2CreateIpamResourceDiscoveryResponse,
    EC2CreateIpamResponse,
    EC2CreateIpamRoutingPolicyRegistrationRequest,
    EC2CreateIpamRoutingPolicyRegistrationResponse,
    EC2CreateIpamScopeRequest,
    EC2CreateIpamScopeResponse,
    EC2CreateKeyPairRequest,
    EC2CreateKeyPairResponse,
    EC2CreateLaunchTemplateRequest,
    EC2CreateLaunchTemplateResponse,
    EC2CreateLaunchTemplateVersionRequest,
    EC2CreateLaunchTemplateVersionResponse,
    EC2CreateLocalGatewayRouteRequest,
    EC2CreateLocalGatewayRouteResponse,
    EC2CreateLocalGatewayRouteTableRequest,
    EC2CreateLocalGatewayRouteTableResponse,
    EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
    EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse,
    EC2CreateLocalGatewayRouteTableVpcAssociationRequest,
    EC2CreateLocalGatewayRouteTableVpcAssociationResponse,
    EC2CreateLocalGatewayVirtualInterfaceGroupRequest,
    EC2CreateLocalGatewayVirtualInterfaceGroupResponse,
    EC2CreateLocalGatewayVirtualInterfaceRequest,
    EC2CreateLocalGatewayVirtualInterfaceResponse,
    EC2CreateMacSystemIntegrityProtectionModificationTaskRequest,
    EC2CreateMacSystemIntegrityProtectionModificationTaskResponse,
    EC2CreateManagedPrefixListRequest,
    EC2CreateManagedPrefixListResponse,
    EC2CreateMetricCategoryRequest,
    EC2CreateMetricCategoryResponse,
    EC2CreateNatGatewayRequest,
    EC2CreateNatGatewayResponse,
    EC2CreateNetworkAclEntryRequest,
    EC2CreateNetworkAclEntryResponse,
    EC2CreateNetworkAclRequest,
    EC2CreateNetworkAclResponse,
    EC2CreateNetworkInsightsAccessScopeRequest,
    EC2CreateNetworkInsightsAccessScopeResponse,
    EC2CreateNetworkInsightsPathRequest,
    EC2CreateNetworkInsightsPathResponse,
    EC2CreateNetworkInterfacePermissionRequest,
    EC2CreateNetworkInterfacePermissionResponse,
    EC2CreateNetworkInterfaceRequest,
    EC2CreateNetworkInterfaceResponse,
    EC2CreateNetworkingFlexCostAllocationPolicyRequest,
    EC2CreateNetworkingFlexCostAllocationPolicyResponse,
    EC2CreatePlacementGroupRequest,
    EC2CreatePlacementGroupResponse,
    EC2CreatePublicIpv4PoolRequest,
    EC2CreatePublicIpv4PoolResponse,
    EC2CreateReplaceRootVolumeTaskRequest,
    EC2CreateReplaceRootVolumeTaskResponse,
    EC2CreateReservedInstancesListingRequest,
    EC2CreateReservedInstancesListingResponse,
    EC2CreateRestoreImageTaskRequest,
    EC2CreateRestoreImageTaskResponse,
    EC2CreateRouteRequest,
    EC2CreateRouteResponse,
    EC2CreateRouteServerEndpointRequest,
    EC2CreateRouteServerEndpointResponse,
    EC2CreateRouteServerPeerRequest,
    EC2CreateRouteServerPeerResponse,
    EC2CreateRouteServerRequest,
    EC2CreateRouteServerResponse,
    EC2CreateRouteTableRequest,
    EC2CreateRouteTableResponse,
    EC2CreateSecondaryNetworkRequest,
    EC2CreateSecondaryNetworkResponse,
    EC2CreateSecondarySubnetRequest,
    EC2CreateSecondarySubnetResponse,
    EC2CreateSnapshotsRequest,
    EC2CreateSnapshotsResponse,
    EC2CreateSpotDatafeedSubscriptionRequest,
    EC2CreateSpotDatafeedSubscriptionResponse,
    EC2CreateStoreImageTaskRequest,
    EC2CreateStoreImageTaskResponse,
    EC2CreateSubnetCidrReservationRequest,
    EC2CreateSubnetCidrReservationResponse,
    EC2CreateSubnetRequest,
    EC2CreateSubnetResponse,
    EC2CreateTrafficMirrorFilterRequest,
    EC2CreateTrafficMirrorFilterResponse,
    EC2CreateTrafficMirrorFilterRuleRequest,
    EC2CreateTrafficMirrorFilterRuleResponse,
    EC2CreateTrafficMirrorSessionRequest,
    EC2CreateTrafficMirrorSessionResponse,
    EC2CreateTrafficMirrorTargetRequest,
    EC2CreateTrafficMirrorTargetResponse,
    EC2CreateTransitGatewayConnectPeerRequest,
    EC2CreateTransitGatewayConnectPeerResponse,
    EC2CreateTransitGatewayConnectRequest,
    EC2CreateTransitGatewayConnectResponse,
    EC2CreateTransitGatewayMeteringPolicyEntryRequest,
    EC2CreateTransitGatewayMeteringPolicyEntryResponse,
    EC2CreateTransitGatewayMeteringPolicyRequest,
    EC2CreateTransitGatewayMeteringPolicyResponse,
    EC2CreateTransitGatewayMulticastDomainRequest,
    EC2CreateTransitGatewayMulticastDomainResponse,
    EC2CreateTransitGatewayNetworkFunctionAttachmentRequest,
    EC2CreateTransitGatewayNetworkFunctionAttachmentResponse,
    EC2CreateTransitGatewayPeeringAttachmentRequest,
    EC2CreateTransitGatewayPeeringAttachmentResponse,
    EC2CreateTransitGatewayPolicyTableEntryRequest,
    EC2CreateTransitGatewayPolicyTableEntryResponse,
    EC2CreateTransitGatewayPolicyTableRequest,
    EC2CreateTransitGatewayPolicyTableResponse,
    EC2CreateTransitGatewayPrefixListReferenceRequest,
    EC2CreateTransitGatewayPrefixListReferenceResponse,
    EC2CreateTransitGatewayRequest,
    EC2CreateTransitGatewayResponse,
    EC2CreateTransitGatewayRouteRequest,
    EC2CreateTransitGatewayRouteResponse,
    EC2CreateTransitGatewayRouteTableAnnouncementRequest,
    EC2CreateTransitGatewayRouteTableAnnouncementResponse,
    EC2CreateTransitGatewayRouteTableRequest,
    EC2CreateTransitGatewayRouteTableResponse,
    EC2CreateTransitGatewayVpcAttachmentRequest,
    EC2CreateTransitGatewayVpcAttachmentResponse,
    EC2CreateVerifiedAccessEndpointRequest,
    EC2CreateVerifiedAccessEndpointResponse,
    EC2CreateVerifiedAccessGroupRequest,
    EC2CreateVerifiedAccessGroupResponse,
    EC2CreateVerifiedAccessInstanceRequest,
    EC2CreateVerifiedAccessInstanceResponse,
    EC2CreateVerifiedAccessTrustProviderRequest,
    EC2CreateVerifiedAccessTrustProviderResponse,
    EC2CreateVpcBlockPublicAccessExclusionRequest,
    EC2CreateVpcBlockPublicAccessExclusionResponse,
    EC2CreateVpcEncryptionControlRequest,
    EC2CreateVpcEncryptionControlResponse,
    EC2CreateVpcEndpointConnectionNotificationRequest,
    EC2CreateVpcEndpointConnectionNotificationResponse,
    EC2CreateVpcEndpointRequest,
    EC2CreateVpcEndpointResponse,
    EC2CreateVpcEndpointServiceConfigurationRequest,
    EC2CreateVpcEndpointServiceConfigurationResponse,
    EC2CreateVpcPeeringConnectionRequest,
    EC2CreateVpcPeeringConnectionResponse,
    EC2CreateVpcRequest,
    EC2CreateVpcResponse,
    EC2CreateVpnConcentratorRequest,
    EC2CreateVpnConcentratorResponse,
    EC2CreateVpnConnectionRequest,
    EC2CreateVpnConnectionResponse,
    EC2CreateVpnConnectionRouteRequest,
    EC2CreateVpnConnectionRouteResponse,
    EC2CreateVpnGatewayRequest,
    EC2CreateVpnGatewayResponse,
    EC2DeleteApplicationStatusCheckRequest,
    EC2DeleteApplicationStatusCheckResponse,
    EC2DeleteCapacityManagerDataExportRequest,
    EC2DeleteCapacityManagerDataExportResponse,
    EC2DeleteCarrierGatewayRequest,
    EC2DeleteCarrierGatewayResponse,
    EC2DeleteClientVpnEndpointAuthorizationPolicyRequest,
    EC2DeleteClientVpnEndpointAuthorizationPolicyResponse,
    EC2DeleteClientVpnEndpointRequest,
    EC2DeleteClientVpnEndpointResponse,
    EC2DeleteClientVpnRouteRequest,
    EC2DeleteClientVpnRouteResponse,
    EC2DeleteCoipCidrRequest,
    EC2DeleteCoipCidrResponse,
    EC2DeleteCoipPoolRequest,
    EC2DeleteCoipPoolResponse,
    EC2DeleteCustomerGatewayRequest,
    EC2DeleteCustomerGatewayResponse,
    EC2DeleteDhcpOptionsRequest,
    EC2DeleteDhcpOptionsResponse,
    EC2DeleteEgressOnlyInternetGatewayRequest,
    EC2DeleteEgressOnlyInternetGatewayResponse,
    EC2DeleteFleetsRequest,
    EC2DeleteFleetsResponse,
    EC2DeleteFlowLogsRequest,
    EC2DeleteFlowLogsResponse,
    EC2DeleteFpgaImageRequest,
    EC2DeleteFpgaImageResponse,
    EC2DeleteImageUsageReportRequest,
    EC2DeleteImageUsageReportResponse,
    EC2DeleteInstanceConnectEndpointRequest,
    EC2DeleteInstanceConnectEndpointResponse,
    EC2DeleteInstanceEventWindowRequest,
    EC2DeleteInstanceEventWindowResponse,
    EC2DeleteInternetGatewayRequest,
    EC2DeleteInternetGatewayResponse,
    EC2DeleteIpamExternalResourceVerificationTokenRequest,
    EC2DeleteIpamExternalResourceVerificationTokenResponse,
    EC2DeleteIpamInternetRegistryAssociationRequest,
    EC2DeleteIpamInternetRegistryAssociationResponse,
    EC2DeleteIpamPolicyRequest,
    EC2DeleteIpamPolicyResponse,
    EC2DeleteIpamPoolRequest,
    EC2DeleteIpamPoolResponse,
    EC2DeleteIpamPrefixListResolverRequest,
    EC2DeleteIpamPrefixListResolverResponse,
    EC2DeleteIpamPrefixListResolverTargetRequest,
    EC2DeleteIpamPrefixListResolverTargetResponse,
    EC2DeleteIpamRequest,
    EC2DeleteIpamResourceDiscoveryRequest,
    EC2DeleteIpamResourceDiscoveryResponse,
    EC2DeleteIpamResponse,
    EC2DeleteIpamRoutingPolicyRegistrationRequest,
    EC2DeleteIpamRoutingPolicyRegistrationResponse,
    EC2DeleteIpamScopeRequest,
    EC2DeleteIpamScopeResponse,
    EC2DeleteKeyPairRequest,
    EC2DeleteKeyPairResponse,
    EC2DeleteLaunchTemplateRequest,
    EC2DeleteLaunchTemplateResponse,
    EC2DeleteLaunchTemplateVersionsRequest,
    EC2DeleteLaunchTemplateVersionsResponse,
    EC2DeleteLocalGatewayRouteRequest,
    EC2DeleteLocalGatewayRouteResponse,
    EC2DeleteLocalGatewayRouteTableRequest,
    EC2DeleteLocalGatewayRouteTableResponse,
    EC2DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
    EC2DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse,
    EC2DeleteLocalGatewayRouteTableVpcAssociationRequest,
    EC2DeleteLocalGatewayRouteTableVpcAssociationResponse,
    EC2DeleteLocalGatewayVirtualInterfaceGroupRequest,
    EC2DeleteLocalGatewayVirtualInterfaceGroupResponse,
    EC2DeleteLocalGatewayVirtualInterfaceRequest,
    EC2DeleteLocalGatewayVirtualInterfaceResponse,
    EC2DeleteManagedPrefixListRequest,
    EC2DeleteManagedPrefixListResponse,
    EC2DeleteMetricCategoryRequest,
    EC2DeleteMetricCategoryResponse,
    EC2DeleteNatGatewayRequest,
    EC2DeleteNatGatewayResponse,
    EC2DeleteNetworkAclEntryRequest,
    EC2DeleteNetworkAclEntryResponse,
    EC2DeleteNetworkAclRequest,
    EC2DeleteNetworkAclResponse,
    EC2DeleteNetworkInsightsAccessScopeAnalysisRequest,
    EC2DeleteNetworkInsightsAccessScopeAnalysisResponse,
    EC2DeleteNetworkInsightsAccessScopeRequest,
    EC2DeleteNetworkInsightsAccessScopeResponse,
    EC2DeleteNetworkInsightsAnalysisRequest,
    EC2DeleteNetworkInsightsAnalysisResponse,
    EC2DeleteNetworkInsightsPathRequest,
    EC2DeleteNetworkInsightsPathResponse,
    EC2DeleteNetworkInterfacePermissionRequest,
    EC2DeleteNetworkInterfacePermissionResponse,
    EC2DeleteNetworkInterfaceRequest,
    EC2DeleteNetworkInterfaceResponse,
    EC2DeleteNetworkingFlexCostAllocationPoliciesRequest,
    EC2DeleteNetworkingFlexCostAllocationPoliciesResponse,
    EC2DeletePlacementGroupRequest,
    EC2DeletePlacementGroupResponse,
    EC2DeletePublicIpv4PoolRequest,
    EC2DeletePublicIpv4PoolResponse,
    EC2DeleteQueuedReservedInstancesRequest,
    EC2DeleteQueuedReservedInstancesResponse,
    EC2DeleteRouteRequest,
    EC2DeleteRouteResponse,
    EC2DeleteRouteServerEndpointRequest,
    EC2DeleteRouteServerEndpointResponse,
    EC2DeleteRouteServerPeerRequest,
    EC2DeleteRouteServerPeerResponse,
    EC2DeleteRouteServerRequest,
    EC2DeleteRouteServerResponse,
    EC2DeleteRouteTableRequest,
    EC2DeleteRouteTableResponse,
    EC2DeleteSecondaryNetworkRequest,
    EC2DeleteSecondaryNetworkResponse,
    EC2DeleteSecondarySubnetRequest,
    EC2DeleteSecondarySubnetResponse,
    EC2DeleteSpotDatafeedSubscriptionRequest,
    EC2DeleteSpotDatafeedSubscriptionResponse,
    EC2DeleteSubnetCidrReservationRequest,
    EC2DeleteSubnetCidrReservationResponse,
    EC2DeleteSubnetRequest,
    EC2DeleteSubnetResponse,
    EC2DeleteTrafficMirrorFilterRequest,
    EC2DeleteTrafficMirrorFilterResponse,
    EC2DeleteTrafficMirrorFilterRuleRequest,
    EC2DeleteTrafficMirrorFilterRuleResponse,
    EC2DeleteTrafficMirrorSessionRequest,
    EC2DeleteTrafficMirrorSessionResponse,
    EC2DeleteTrafficMirrorTargetRequest,
    EC2DeleteTrafficMirrorTargetResponse,
    EC2DeleteTransitGatewayClientVpnAttachmentRequest,
    EC2DeleteTransitGatewayClientVpnAttachmentResponse,
    EC2DeleteTransitGatewayConnectPeerRequest,
    EC2DeleteTransitGatewayConnectPeerResponse,
    EC2DeleteTransitGatewayConnectRequest,
    EC2DeleteTransitGatewayConnectResponse,
    EC2DeleteTransitGatewayMeteringPolicyEntryRequest,
    EC2DeleteTransitGatewayMeteringPolicyEntryResponse,
    EC2DeleteTransitGatewayMeteringPolicyRequest,
    EC2DeleteTransitGatewayMeteringPolicyResponse,
    EC2DeleteTransitGatewayMulticastDomainRequest,
    EC2DeleteTransitGatewayMulticastDomainResponse,
    EC2DeleteTransitGatewayNetworkFunctionAttachmentRequest,
    EC2DeleteTransitGatewayNetworkFunctionAttachmentResponse,
    EC2DeleteTransitGatewayPeeringAttachmentRequest,
    EC2DeleteTransitGatewayPeeringAttachmentResponse,
    EC2DeleteTransitGatewayPolicyTableEntryRequest,
    EC2DeleteTransitGatewayPolicyTableEntryResponse,
    EC2DeleteTransitGatewayPolicyTableRequest,
    EC2DeleteTransitGatewayPolicyTableResponse,
    EC2DeleteTransitGatewayPrefixListReferenceRequest,
    EC2DeleteTransitGatewayPrefixListReferenceResponse,
    EC2DeleteTransitGatewayRequest,
    EC2DeleteTransitGatewayResponse,
    EC2DeleteTransitGatewayRouteRequest,
    EC2DeleteTransitGatewayRouteResponse,
    EC2DeleteTransitGatewayRouteTableAnnouncementRequest,
    EC2DeleteTransitGatewayRouteTableAnnouncementResponse,
    EC2DeleteTransitGatewayRouteTableRequest,
    EC2DeleteTransitGatewayRouteTableResponse,
    EC2DeleteTransitGatewayVpcAttachmentRequest,
    EC2DeleteTransitGatewayVpcAttachmentResponse,
    EC2DeleteVerifiedAccessEndpointRequest,
    EC2DeleteVerifiedAccessEndpointResponse,
    EC2DeleteVerifiedAccessGroupRequest,
    EC2DeleteVerifiedAccessGroupResponse,
    EC2DeleteVerifiedAccessInstanceRequest,
    EC2DeleteVerifiedAccessInstanceResponse,
    EC2DeleteVerifiedAccessTrustProviderRequest,
    EC2DeleteVerifiedAccessTrustProviderResponse,
    EC2DeleteVpcBlockPublicAccessExclusionRequest,
    EC2DeleteVpcBlockPublicAccessExclusionResponse,
    EC2DeleteVpcEncryptionControlRequest,
    EC2DeleteVpcEncryptionControlResponse,
    EC2DeleteVpcEndpointConnectionNotificationsRequest,
    EC2DeleteVpcEndpointConnectionNotificationsResponse,
    EC2DeleteVpcEndpointServiceConfigurationsRequest,
    EC2DeleteVpcEndpointServiceConfigurationsResponse,
    EC2DeleteVpcEndpointsRequest,
    EC2DeleteVpcEndpointsResponse,
    EC2DeleteVpcPeeringConnectionRequest,
    EC2DeleteVpcPeeringConnectionResponse,
    EC2DeleteVpcRequest,
    EC2DeleteVpcResponse,
    EC2DeleteVpnConcentratorRequest,
    EC2DeleteVpnConcentratorResponse,
    EC2DeleteVpnConnectionRequest,
    EC2DeleteVpnConnectionResponse,
    EC2DeleteVpnConnectionRouteRequest,
    EC2DeleteVpnConnectionRouteResponse,
    EC2DeleteVpnGatewayRequest,
    EC2DeleteVpnGatewayResponse,
    EC2DeprovisionByoipCidrRequest,
    EC2DeprovisionByoipCidrResponse,
    EC2DeprovisionIpamByoasnRequest,
    EC2DeprovisionIpamByoasnResponse,
    EC2DeprovisionIpamPoolCidrRequest,
    EC2DeprovisionIpamPoolCidrResponse,
    EC2DeprovisionPublicIpv4PoolCidrRequest,
    EC2DeprovisionPublicIpv4PoolCidrResponse,
    EC2DeregisterImageRequest,
    EC2DeregisterImageResponse,
    EC2DeregisterInstanceEventNotificationAttributesRequest,
    EC2DeregisterInstanceEventNotificationAttributesResponse,
    EC2DeregisterTransitGatewayMulticastGroupMembersRequest,
    EC2DeregisterTransitGatewayMulticastGroupMembersResponse,
    EC2DeregisterTransitGatewayMulticastGroupSourcesRequest,
    EC2DeregisterTransitGatewayMulticastGroupSourcesResponse,
    EC2DescribeAccountAttributesRequest,
    EC2DescribeAccountAttributesResponse,
    EC2DescribeAccountVpcEncryptionControlRequest,
    EC2DescribeAccountVpcEncryptionControlResponse,
    EC2DescribeAddressTransfersRequest,
    EC2DescribeAddressTransfersResponse,
    EC2DescribeAddressesAttributeRequest,
    EC2DescribeAddressesAttributeResponse,
    EC2DescribeAddressesRequest,
    EC2DescribeAddressesResponse,
    EC2DescribeAggregateIdFormatRequest,
    EC2DescribeAggregateIdFormatResponse,
    EC2DescribeApplicationStatusCheckAssociationsRequest,
    EC2DescribeApplicationStatusCheckAssociationsResponse,
    EC2DescribeApplicationStatusChecksRequest,
    EC2DescribeApplicationStatusChecksResponse,
    EC2DescribeApplicationStatusRequest,
    EC2DescribeApplicationStatusResponse,
    EC2DescribeAvailabilityZonesRequest,
    EC2DescribeAvailabilityZonesResponse,
    EC2DescribeAwsNetworkPerformanceMetricSubscriptionsRequest,
    EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse,
    EC2DescribeBundleTasksRequest,
    EC2DescribeBundleTasksResponse,
    EC2DescribeByoipCidrsRequest,
    EC2DescribeByoipCidrsResponse,
    EC2DescribeCapacityBlockExtensionHistoryRequest,
    EC2DescribeCapacityBlockExtensionHistoryResponse,
    EC2DescribeCapacityBlockExtensionOfferingsRequest,
    EC2DescribeCapacityBlockExtensionOfferingsResponse,
    EC2DescribeCapacityBlockOfferingsRequest,
    EC2DescribeCapacityBlockOfferingsResponse,
    EC2DescribeCapacityBlockStatusRequest,
    EC2DescribeCapacityBlockStatusResponse,
    EC2DescribeCapacityBlocksRequest,
    EC2DescribeCapacityBlocksResponse,
    EC2DescribeCapacityManagerDataExportsRequest,
    EC2DescribeCapacityManagerDataExportsResponse,
    EC2DescribeCapacityReservationBillingRequestsRequest,
    EC2DescribeCapacityReservationBillingRequestsResponse,
    EC2DescribeCapacityReservationCancellationQuotesRequest,
    EC2DescribeCapacityReservationCancellationQuotesResponse,
    EC2DescribeCapacityReservationDateChangeQuotesRequest,
    EC2DescribeCapacityReservationDateChangeQuotesResponse,
    EC2DescribeCapacityReservationFleetsRequest,
    EC2DescribeCapacityReservationFleetsResponse,
    EC2DescribeCapacityReservationTopologyRequest,
    EC2DescribeCapacityReservationTopologyResponse,
    EC2DescribeCapacityReservationsRequest,
    EC2DescribeCapacityReservationsResponse,
    EC2DescribeCarrierGatewaysRequest,
    EC2DescribeCarrierGatewaysResponse,
    EC2DescribeClassicLinkInstancesRequest,
    EC2DescribeClassicLinkInstancesResponse,
    EC2DescribeClientVpnAuthorizationRulesRequest,
    EC2DescribeClientVpnAuthorizationRulesResponse,
    EC2DescribeClientVpnConnectionsRequest,
    EC2DescribeClientVpnConnectionsResponse,
    EC2DescribeClientVpnEndpointsRequest,
    EC2DescribeClientVpnEndpointsResponse,
    EC2DescribeClientVpnRoutesRequest,
    EC2DescribeClientVpnRoutesResponse,
    EC2DescribeClientVpnTargetNetworksRequest,
    EC2DescribeClientVpnTargetNetworksResponse,
    EC2DescribeCoipPoolsRequest,
    EC2DescribeCoipPoolsResponse,
    EC2DescribeConversionTasksRequest,
    EC2DescribeConversionTasksResponse,
    EC2DescribeCustomerGatewaysRequest,
    EC2DescribeCustomerGatewaysResponse,
    EC2DescribeDeclarativePoliciesReportsRequest,
    EC2DescribeDeclarativePoliciesReportsResponse,
    EC2DescribeDhcpOptionsRequest,
    EC2DescribeDhcpOptionsResponse,
    EC2DescribeEgressOnlyInternetGatewaysRequest,
    EC2DescribeEgressOnlyInternetGatewaysResponse,
    EC2DescribeElasticGpusRequest,
    EC2DescribeElasticGpusResponse,
    EC2DescribeExportImageTasksRequest,
    EC2DescribeExportImageTasksResponse,
    EC2DescribeExportTasksRequest,
    EC2DescribeExportTasksResponse,
    EC2DescribeFastLaunchImagesRequest,
    EC2DescribeFastLaunchImagesResponse,
    EC2DescribeFastSnapshotRestoresRequest,
    EC2DescribeFastSnapshotRestoresResponse,
    EC2DescribeFleetHistoryRequest,
    EC2DescribeFleetHistoryResponse,
    EC2DescribeFleetInstancesRequest,
    EC2DescribeFleetInstancesResponse,
    EC2DescribeFleetsRequest,
    EC2DescribeFleetsResponse,
    EC2DescribeFlowLogsRequest,
    EC2DescribeFlowLogsResponse,
    EC2DescribeFpgaImageAttributeRequest,
    EC2DescribeFpgaImageAttributeResponse,
    EC2DescribeFpgaImagesRequest,
    EC2DescribeFpgaImagesResponse,
    EC2DescribeHostReservationOfferingsRequest,
    EC2DescribeHostReservationOfferingsResponse,
    EC2DescribeHostReservationsRequest,
    EC2DescribeHostReservationsResponse,
    EC2DescribeHostsRequest,
    EC2DescribeHostsResponse,
    EC2DescribeIamInstanceProfileAssociationsRequest,
    EC2DescribeIamInstanceProfileAssociationsResponse,
    EC2DescribeIdFormatRequest,
    EC2DescribeIdFormatResponse,
    EC2DescribeIdentityIdFormatRequest,
    EC2DescribeIdentityIdFormatResponse,
    EC2DescribeImageAttributeRequest,
    EC2DescribeImageAttributeResponse,
    EC2DescribeImageReferencesRequest,
    EC2DescribeImageReferencesResponse,
    EC2DescribeImageUsageReportEntriesRequest,
    EC2DescribeImageUsageReportEntriesResponse,
    EC2DescribeImageUsageReportsRequest,
    EC2DescribeImageUsageReportsResponse,
    EC2DescribeImagesRequest,
    EC2DescribeImagesResponse,
    EC2DescribeImportImageTasksRequest,
    EC2DescribeImportImageTasksResponse,
    EC2DescribeImportSnapshotTasksRequest,
    EC2DescribeImportSnapshotTasksResponse,
    EC2DescribeInstanceAttributeRequest,
    EC2DescribeInstanceAttributeResponse,
    EC2DescribeInstanceConnectEndpointsRequest,
    EC2DescribeInstanceConnectEndpointsResponse,
    EC2DescribeInstanceCreditSpecificationsRequest,
    EC2DescribeInstanceCreditSpecificationsResponse,
    EC2DescribeInstanceEventNotificationAttributesRequest,
    EC2DescribeInstanceEventNotificationAttributesResponse,
    EC2DescribeInstanceEventWindowsRequest,
    EC2DescribeInstanceEventWindowsResponse,
    EC2DescribeInstanceImageMetadataRequest,
    EC2DescribeInstanceImageMetadataResponse,
    EC2DescribeInstanceSqlHaHistoryStatesRequest,
    EC2DescribeInstanceSqlHaHistoryStatesResponse,
    EC2DescribeInstanceSqlHaStatesRequest,
    EC2DescribeInstanceSqlHaStatesResponse,
    EC2DescribeInstanceStatusRequest,
    EC2DescribeInstanceStatusResponse,
    EC2DescribeInstanceTopologyRequest,
    EC2DescribeInstanceTopologyResponse,
    EC2DescribeInstanceTypeOfferingsRequest,
    EC2DescribeInstanceTypeOfferingsResponse,
    EC2DescribeInstanceTypesRequest,
    EC2DescribeInstanceTypesResponse,
    EC2DescribeInternetGatewaysRequest,
    EC2DescribeInternetGatewaysResponse,
    EC2DescribeIpamByoasnRequest,
    EC2DescribeIpamByoasnResponse,
    EC2DescribeIpamExternalResourceVerificationTokensRequest,
    EC2DescribeIpamExternalResourceVerificationTokensResponse,
    EC2DescribeIpamInternetRegistryAssociationsRequest,
    EC2DescribeIpamInternetRegistryAssociationsResponse,
    EC2DescribeIpamPoliciesRequest,
    EC2DescribeIpamPoliciesResponse,
    EC2DescribeIpamPoolAllocationsRequest,
    EC2DescribeIpamPoolAllocationsResponse,
    EC2DescribeIpamPoolsRequest,
    EC2DescribeIpamPoolsResponse,
    EC2DescribeIpamPrefixListResolverTargetsRequest,
    EC2DescribeIpamPrefixListResolverTargetsResponse,
    EC2DescribeIpamPrefixListResolversRequest,
    EC2DescribeIpamPrefixListResolversResponse,
    EC2DescribeIpamResourceDiscoveriesRequest,
    EC2DescribeIpamResourceDiscoveriesResponse,
    EC2DescribeIpamResourceDiscoveryAssociationsRequest,
    EC2DescribeIpamResourceDiscoveryAssociationsResponse,
    EC2DescribeIpamScopesRequest,
    EC2DescribeIpamScopesResponse,
    EC2DescribeIpamsRequest,
    EC2DescribeIpamsResponse,
    EC2DescribeIpv6PoolsRequest,
    EC2DescribeIpv6PoolsResponse,
    EC2DescribeLaunchTemplateVersionsRequest,
    EC2DescribeLaunchTemplateVersionsResponse,
    EC2DescribeLaunchTemplatesRequest,
    EC2DescribeLaunchTemplatesResponse,
    EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest,
    EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponse,
    EC2DescribeLocalGatewayRouteTableVpcAssociationsRequest,
    EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse,
    EC2DescribeLocalGatewayRouteTablesRequest,
    EC2DescribeLocalGatewayRouteTablesResponse,
    EC2DescribeLocalGatewayVirtualInterfaceGroupsRequest,
    EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse,
    EC2DescribeLocalGatewayVirtualInterfacesRequest,
    EC2DescribeLocalGatewayVirtualInterfacesResponse,
    EC2DescribeLocalGatewaysRequest,
    EC2DescribeLocalGatewaysResponse,
    EC2DescribeLockedSnapshotsRequest,
    EC2DescribeLockedSnapshotsResponse,
    EC2DescribeMacHostsRequest,
    EC2DescribeMacHostsResponse,
    EC2DescribeMacModificationTasksRequest,
    EC2DescribeMacModificationTasksResponse,
    EC2DescribeManagedPrefixListsRequest,
    EC2DescribeManagedPrefixListsResponse,
    EC2DescribeMetricCategoriesRequest,
    EC2DescribeMetricCategoriesResponse,
    EC2DescribeMovingAddressesRequest,
    EC2DescribeMovingAddressesResponse,
    EC2DescribeNatGatewaysRequest,
    EC2DescribeNatGatewaysResponse,
    EC2DescribeNetworkAclsRequest,
    EC2DescribeNetworkAclsResponse,
    EC2DescribeNetworkInsightsAccessScopeAnalysesRequest,
    EC2DescribeNetworkInsightsAccessScopeAnalysesResponse,
    EC2DescribeNetworkInsightsAccessScopesRequest,
    EC2DescribeNetworkInsightsAccessScopesResponse,
    EC2DescribeNetworkInsightsAnalysesRequest,
    EC2DescribeNetworkInsightsAnalysesResponse,
    EC2DescribeNetworkInsightsPathsRequest,
    EC2DescribeNetworkInsightsPathsResponse,
    EC2DescribeNetworkInterfaceAttributeRequest,
    EC2DescribeNetworkInterfaceAttributeResponse,
    EC2DescribeNetworkInterfacePermissionsRequest,
    EC2DescribeNetworkInterfacePermissionsResponse,
    EC2DescribeNetworkInterfacesRequest,
    EC2DescribeNetworkInterfacesResponse,
    EC2DescribeNetworkingFlexCostAllocationPoliciesRequest,
    EC2DescribeNetworkingFlexCostAllocationPoliciesResponse,
    EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsRequest,
    EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse,
    EC2DescribeOutpostLagsRequest,
    EC2DescribeOutpostLagsResponse,
    EC2DescribePlacementGroupsRequest,
    EC2DescribePlacementGroupsResponse,
    EC2DescribePrefixListsRequest,
    EC2DescribePrefixListsResponse,
    EC2DescribePrincipalIdFormatRequest,
    EC2DescribePrincipalIdFormatResponse,
    EC2DescribePublicIpv4PoolsRequest,
    EC2DescribePublicIpv4PoolsResponse,
    EC2DescribeRegionsRequest,
    EC2DescribeRegionsResponse,
    EC2DescribeReplaceRootVolumeTasksRequest,
    EC2DescribeReplaceRootVolumeTasksResponse,
    EC2DescribeReservedInstancesListingsRequest,
    EC2DescribeReservedInstancesListingsResponse,
    EC2DescribeReservedInstancesModificationsRequest,
    EC2DescribeReservedInstancesModificationsResponse,
    EC2DescribeReservedInstancesOfferingsRequest,
    EC2DescribeReservedInstancesOfferingsResponse,
    EC2DescribeReservedInstancesRequest,
    EC2DescribeReservedInstancesResponse,
    EC2DescribeRouteServerEndpointsRequest,
    EC2DescribeRouteServerEndpointsResponse,
    EC2DescribeRouteServerPeersRequest,
    EC2DescribeRouteServerPeersResponse,
    EC2DescribeRouteServersRequest,
    EC2DescribeRouteServersResponse,
    EC2DescribeRouteTablesRequest,
    EC2DescribeRouteTablesResponse,
    EC2DescribeScheduledInstanceAvailabilityRequest,
    EC2DescribeScheduledInstanceAvailabilityResponse,
    EC2DescribeScheduledInstancesRequest,
    EC2DescribeScheduledInstancesResponse,
    EC2DescribeSecondaryInterfacesRequest,
    EC2DescribeSecondaryInterfacesResponse,
    EC2DescribeSecondaryNetworksRequest,
    EC2DescribeSecondaryNetworksResponse,
    EC2DescribeSecondarySubnetsRequest,
    EC2DescribeSecondarySubnetsResponse,
    EC2DescribeSecurityGroupReferencesRequest,
    EC2DescribeSecurityGroupReferencesResponse,
    EC2DescribeSecurityGroupRulesRequest,
    EC2DescribeSecurityGroupRulesResponse,
    EC2DescribeSecurityGroupVpcAssociationsRequest,
    EC2DescribeSecurityGroupVpcAssociationsResponse,
    EC2DescribeServiceLinkVirtualInterfacesRequest,
    EC2DescribeServiceLinkVirtualInterfacesResponse,
    EC2DescribeSnapshotAttributeRequest,
    EC2DescribeSnapshotAttributeResponse,
    EC2DescribeSnapshotTierStatusRequest,
    EC2DescribeSnapshotTierStatusResponse,
    EC2DescribeSpotDatafeedSubscriptionRequest,
    EC2DescribeSpotDatafeedSubscriptionResponse,
    EC2DescribeSpotFleetInstancesRequest,
    EC2DescribeSpotFleetInstancesResponse,
    EC2DescribeSpotFleetRequestHistoryRequest,
    EC2DescribeSpotFleetRequestHistoryResponse,
    EC2DescribeSpotFleetRequestsRequest,
    EC2DescribeSpotFleetRequestsResponse,
    EC2DescribeSpotInstanceRequestsRequest,
    EC2DescribeSpotInstanceRequestsResponse,
    EC2DescribeSpotPriceHistoryRequest,
    EC2DescribeSpotPriceHistoryResponse,
    EC2DescribeStaleSecurityGroupsRequest,
    EC2DescribeStaleSecurityGroupsResponse,
    EC2DescribeStoreImageTasksRequest,
    EC2DescribeStoreImageTasksResponse,
    EC2DescribeTagsRequest,
    EC2DescribeTagsResponse,
    EC2DescribeTrafficMirrorFilterRulesRequest,
    EC2DescribeTrafficMirrorFilterRulesResponse,
    EC2DescribeTrafficMirrorFiltersRequest,
    EC2DescribeTrafficMirrorFiltersResponse,
    EC2DescribeTrafficMirrorSessionsRequest,
    EC2DescribeTrafficMirrorSessionsResponse,
    EC2DescribeTrafficMirrorTargetsRequest,
    EC2DescribeTrafficMirrorTargetsResponse,
    EC2DescribeTransitGatewayAttachmentsRequest,
    EC2DescribeTransitGatewayAttachmentsResponse,
    EC2DescribeTransitGatewayConnectPeersRequest,
    EC2DescribeTransitGatewayConnectPeersResponse,
    EC2DescribeTransitGatewayConnectsRequest,
    EC2DescribeTransitGatewayConnectsResponse,
    EC2DescribeTransitGatewayMeteringPoliciesRequest,
    EC2DescribeTransitGatewayMeteringPoliciesResponse,
    EC2DescribeTransitGatewayMulticastDomainsRequest,
    EC2DescribeTransitGatewayMulticastDomainsResponse,
    EC2DescribeTransitGatewayNetworkFunctionAttachmentsRequest,
    EC2DescribeTransitGatewayNetworkFunctionAttachmentsResponse,
    EC2DescribeTransitGatewayPeeringAttachmentsRequest,
    EC2DescribeTransitGatewayPeeringAttachmentsResponse,
    EC2DescribeTransitGatewayPolicyTablesRequest,
    EC2DescribeTransitGatewayPolicyTablesResponse,
    EC2DescribeTransitGatewayRouteTableAnnouncementsRequest,
    EC2DescribeTransitGatewayRouteTableAnnouncementsResponse,
    EC2DescribeTransitGatewayRouteTablesRequest,
    EC2DescribeTransitGatewayRouteTablesResponse,
    EC2DescribeTransitGatewayVpcAttachmentsRequest,
    EC2DescribeTransitGatewayVpcAttachmentsResponse,
    EC2DescribeTransitGatewaysRequest,
    EC2DescribeTransitGatewaysResponse,
    EC2DescribeTrunkInterfaceAssociationsRequest,
    EC2DescribeTrunkInterfaceAssociationsResponse,
    EC2DescribeVerifiedAccessEndpointsRequest,
    EC2DescribeVerifiedAccessEndpointsResponse,
    EC2DescribeVerifiedAccessGroupsRequest,
    EC2DescribeVerifiedAccessGroupsResponse,
    EC2DescribeVerifiedAccessInstanceLoggingConfigurationsRequest,
    EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse,
    EC2DescribeVerifiedAccessInstancesRequest,
    EC2DescribeVerifiedAccessInstancesResponse,
    EC2DescribeVerifiedAccessTrustProvidersRequest,
    EC2DescribeVerifiedAccessTrustProvidersResponse,
    EC2DescribeVolumeAttributeRequest,
    EC2DescribeVolumeAttributeResponse,
    EC2DescribeVolumeStatusRequest,
    EC2DescribeVolumeStatusResponse,
    EC2DescribeVolumesModificationsRequest,
    EC2DescribeVolumesModificationsResponse,
    EC2DescribeVpcAttributeRequest,
    EC2DescribeVpcAttributeResponse,
    EC2DescribeVpcBlockPublicAccessExclusionsRequest,
    EC2DescribeVpcBlockPublicAccessExclusionsResponse,
    EC2DescribeVpcBlockPublicAccessOptionsRequest,
    EC2DescribeVpcBlockPublicAccessOptionsResponse,
    EC2DescribeVpcClassicLinkDnsSupportRequest,
    EC2DescribeVpcClassicLinkDnsSupportResponse,
    EC2DescribeVpcClassicLinkRequest,
    EC2DescribeVpcClassicLinkResponse,
    EC2DescribeVpcEncryptionControlsRequest,
    EC2DescribeVpcEncryptionControlsResponse,
    EC2DescribeVpcEndpointAssociationsRequest,
    EC2DescribeVpcEndpointAssociationsResponse,
    EC2DescribeVpcEndpointConnectionNotificationsRequest,
    EC2DescribeVpcEndpointConnectionNotificationsResponse,
    EC2DescribeVpcEndpointConnectionsRequest,
    EC2DescribeVpcEndpointConnectionsResponse,
    EC2DescribeVpcEndpointServiceConfigurationsRequest,
    EC2DescribeVpcEndpointServiceConfigurationsResponse,
    EC2DescribeVpcEndpointServicePermissionsRequest,
    EC2DescribeVpcEndpointServicePermissionsResponse,
    EC2DescribeVpcEndpointServicesRequest,
    EC2DescribeVpcEndpointServicesResponse,
    EC2DescribeVpcEndpointsRequest,
    EC2DescribeVpcEndpointsResponse,
    EC2DescribeVpcPeeringConnectionsRequest,
    EC2DescribeVpcPeeringConnectionsResponse,
    EC2DescribeVpnConcentratorsRequest,
    EC2DescribeVpnConcentratorsResponse,
    EC2DescribeVpnConnectionsRequest,
    EC2DescribeVpnConnectionsResponse,
    EC2DescribeVpnGatewaysRequest,
    EC2DescribeVpnGatewaysResponse,
    EC2DetachClassicLinkVpcRequest,
    EC2DetachClassicLinkVpcResponse,
    EC2DetachImageWatermarkRequest,
    EC2DetachImageWatermarkResponse,
    EC2DetachInternetGatewayRequest,
    EC2DetachInternetGatewayResponse,
    EC2DetachNetworkInterfaceRequest,
    EC2DetachNetworkInterfaceResponse,
    EC2DetachVerifiedAccessTrustProviderRequest,
    EC2DetachVerifiedAccessTrustProviderResponse,
    EC2DetachVpnGatewayRequest,
    EC2DetachVpnGatewayResponse,
    EC2DisableAddressTransferRequest,
    EC2DisableAddressTransferResponse,
    EC2DisableAllowedImagesSettingsRequest,
    EC2DisableAllowedImagesSettingsResponse,
    EC2DisableApplicationStatusCheckSuppressionRequest,
    EC2DisableApplicationStatusCheckSuppressionResponse,
    EC2DisableAwsNetworkPerformanceMetricSubscriptionRequest,
    EC2DisableAwsNetworkPerformanceMetricSubscriptionResponse,
    EC2DisableCapacityManagerRequest,
    EC2DisableCapacityManagerResponse,
    EC2DisableEbsEncryptionByDefaultRequest,
    EC2DisableEbsEncryptionByDefaultResponse,
    EC2DisableFastLaunchRequest,
    EC2DisableFastLaunchResponse,
    EC2DisableFastSnapshotRestoresRequest,
    EC2DisableFastSnapshotRestoresResponse,
    EC2DisableImageBlockPublicAccessRequest,
    EC2DisableImageBlockPublicAccessResponse,
    EC2DisableImageDeprecationRequest,
    EC2DisableImageDeprecationResponse,
    EC2DisableImageDeregistrationProtectionRequest,
    EC2DisableImageDeregistrationProtectionResponse,
    EC2DisableImageRequest,
    EC2DisableImageResponse,
    EC2DisableInstanceSqlHaStandbyDetectionsRequest,
    EC2DisableInstanceSqlHaStandbyDetectionsResponse,
    EC2DisableIpamOrganizationAdminAccountRequest,
    EC2DisableIpamOrganizationAdminAccountResponse,
    EC2DisableIpamPolicyRequest,
    EC2DisableIpamPolicyResponse,
    EC2DisableRouteServerPropagationRequest,
    EC2DisableRouteServerPropagationResponse,
    EC2DisableSerialConsoleAccessRequest,
    EC2DisableSerialConsoleAccessResponse,
    EC2DisableSnapshotBlockPublicAccessRequest,
    EC2DisableSnapshotBlockPublicAccessResponse,
    EC2DisableTransitGatewayRouteTablePropagationRequest,
    EC2DisableTransitGatewayRouteTablePropagationResponse,
    EC2DisableVgwRoutePropagationRequest,
    EC2DisableVgwRoutePropagationResponse,
    EC2DisableVpcClassicLinkDnsSupportRequest,
    EC2DisableVpcClassicLinkDnsSupportResponse,
    EC2DisableVpcClassicLinkRequest,
    EC2DisableVpcClassicLinkResponse,
    EC2DisassociateAddressRequest,
    EC2DisassociateAddressResponse,
    EC2DisassociateApplicationStatusCheckRequest,
    EC2DisassociateApplicationStatusCheckResponse,
    EC2DisassociateCapacityReservationBillingOwnerRequest,
    EC2DisassociateCapacityReservationBillingOwnerResponse,
    EC2DisassociateClientVpnTargetNetworkRequest,
    EC2DisassociateClientVpnTargetNetworkResponse,
    EC2DisassociateEnclaveCertificateIamRoleRequest,
    EC2DisassociateEnclaveCertificateIamRoleResponse,
    EC2DisassociateIamInstanceProfileRequest,
    EC2DisassociateIamInstanceProfileResponse,
    EC2DisassociateInstanceEventWindowRequest,
    EC2DisassociateInstanceEventWindowResponse,
    EC2DisassociateIpamByoasnRequest,
    EC2DisassociateIpamByoasnResponse,
    EC2DisassociateIpamResourceDiscoveryRequest,
    EC2DisassociateIpamResourceDiscoveryResponse,
    EC2DisassociateKmsKeyIdRequest,
    EC2DisassociateKmsKeyIdResponse,
    EC2DisassociateNatGatewayAddressRequest,
    EC2DisassociateNatGatewayAddressResponse,
    EC2DisassociateNetworkingFlexCostAllocationPolicyRequest,
    EC2DisassociateNetworkingFlexCostAllocationPolicyResponse,
    EC2DisassociateRouteServerRequest,
    EC2DisassociateRouteServerResponse,
    EC2DisassociateRouteTableRequest,
    EC2DisassociateRouteTableResponse,
    EC2DisassociateSecurityGroupVpcRequest,
    EC2DisassociateSecurityGroupVpcResponse,
    EC2DisassociateSubnetCidrBlockRequest,
    EC2DisassociateSubnetCidrBlockResponse,
    EC2DisassociateTransitGatewayMulticastDomainRequest,
    EC2DisassociateTransitGatewayMulticastDomainResponse,
    EC2DisassociateTransitGatewayPolicyTableRequest,
    EC2DisassociateTransitGatewayPolicyTableResponse,
    EC2DisassociateTransitGatewayRouteTableRequest,
    EC2DisassociateTransitGatewayRouteTableResponse,
    EC2DisassociateTrunkInterfaceRequest,
    EC2DisassociateTrunkInterfaceResponse,
    EC2DisassociateVpcCidrBlockRequest,
    EC2DisassociateVpcCidrBlockResponse,
    EC2EnableAddressTransferRequest,
    EC2EnableAddressTransferResponse,
    EC2EnableAllowedImagesSettingsRequest,
    EC2EnableAllowedImagesSettingsResponse,
    EC2EnableApplicationStatusCheckSuppressionRequest,
    EC2EnableApplicationStatusCheckSuppressionResponse,
    EC2EnableAwsNetworkPerformanceMetricSubscriptionRequest,
    EC2EnableAwsNetworkPerformanceMetricSubscriptionResponse,
    EC2EnableCapacityManagerRequest,
    EC2EnableCapacityManagerResponse,
    EC2EnableEbsEncryptionByDefaultRequest,
    EC2EnableEbsEncryptionByDefaultResponse,
    EC2EnableFastLaunchRequest,
    EC2EnableFastLaunchResponse,
    EC2EnableFastSnapshotRestoresRequest,
    EC2EnableFastSnapshotRestoresResponse,
    EC2EnableImageBlockPublicAccessRequest,
    EC2EnableImageBlockPublicAccessResponse,
    EC2EnableImageDeprecationRequest,
    EC2EnableImageDeprecationResponse,
    EC2EnableImageDeregistrationProtectionRequest,
    EC2EnableImageDeregistrationProtectionResponse,
    EC2EnableImageRequest,
    EC2EnableImageResponse,
    EC2EnableInstanceSqlHaStandbyDetectionsRequest,
    EC2EnableInstanceSqlHaStandbyDetectionsResponse,
    EC2EnableIpamInternetRegistryAssociationRequest,
    EC2EnableIpamInternetRegistryAssociationResponse,
    EC2EnableIpamOrganizationAdminAccountRequest,
    EC2EnableIpamOrganizationAdminAccountResponse,
    EC2EnableIpamPolicyRequest,
    EC2EnableIpamPolicyResponse,
    EC2EnableReachabilityAnalyzerOrganizationSharingRequest,
    EC2EnableReachabilityAnalyzerOrganizationSharingResponse,
    EC2EnableRouteServerPropagationRequest,
    EC2EnableRouteServerPropagationResponse,
    EC2EnableSerialConsoleAccessRequest,
    EC2EnableSerialConsoleAccessResponse,
    EC2EnableSnapshotBlockPublicAccessRequest,
    EC2EnableSnapshotBlockPublicAccessResponse,
    EC2EnableTransitGatewayRouteTablePropagationRequest,
    EC2EnableTransitGatewayRouteTablePropagationResponse,
    EC2EnableVgwRoutePropagationRequest,
    EC2EnableVgwRoutePropagationResponse,
    EC2EnableVolumeIORequest,
    EC2EnableVolumeIOResponse,
    EC2EnableVpcClassicLinkDnsSupportRequest,
    EC2EnableVpcClassicLinkDnsSupportResponse,
    EC2EnableVpcClassicLinkRequest,
    EC2EnableVpcClassicLinkResponse,
    EC2ExportClientVpnClientCertificateRevocationListRequest,
    EC2ExportClientVpnClientCertificateRevocationListResponse,
    EC2ExportClientVpnClientConfigurationRequest,
    EC2ExportClientVpnClientConfigurationResponse,
    EC2ExportImageRequest,
    EC2ExportImageResponse,
    EC2ExportTransitGatewayRoutesRequest,
    EC2ExportTransitGatewayRoutesResponse,
    EC2ExportVerifiedAccessInstanceClientConfigurationRequest,
    EC2ExportVerifiedAccessInstanceClientConfigurationResponse,
    EC2GetActiveVpnTunnelStatusRequest,
    EC2GetActiveVpnTunnelStatusResponse,
    EC2GetAllowedImagesSettingsRequest,
    EC2GetAllowedImagesSettingsResponse,
    EC2GetAssociatedEnclaveCertificateIamRolesRequest,
    EC2GetAssociatedEnclaveCertificateIamRolesResponse,
    EC2GetAssociatedIpv6PoolCidrsRequest,
    EC2GetAssociatedIpv6PoolCidrsResponse,
    EC2GetAwsNetworkPerformanceDataRequest,
    EC2GetAwsNetworkPerformanceDataResponse,
    EC2GetCapacityManagerAttributesRequest,
    EC2GetCapacityManagerAttributesResponse,
    EC2GetCapacityManagerMetricDataRequest,
    EC2GetCapacityManagerMetricDataResponse,
    EC2GetCapacityManagerMetricDimensionsRequest,
    EC2GetCapacityManagerMetricDimensionsResponse,
    EC2GetCapacityManagerMonitoredTagKeysRequest,
    EC2GetCapacityManagerMonitoredTagKeysResponse,
    EC2GetCapacityManagerSupportabilityScoresRequest,
    EC2GetCapacityManagerSupportabilityScoresResponse,
    EC2GetCapacityReservationUsageRequest,
    EC2GetCapacityReservationUsageResponse,
    EC2GetClientVpnEndpointAuthorizationPolicyRequest,
    EC2GetClientVpnEndpointAuthorizationPolicyResponse,
    EC2GetCoipPoolUsageRequest,
    EC2GetCoipPoolUsageResponse,
    EC2GetConsoleOutputRequest,
    EC2GetConsoleOutputResponse,
    EC2GetConsoleScreenshotRequest,
    EC2GetConsoleScreenshotResponse,
    EC2GetDeclarativePoliciesReportSummaryRequest,
    EC2GetDeclarativePoliciesReportSummaryResponse,
    EC2GetDefaultCreditSpecificationRequest,
    EC2GetDefaultCreditSpecificationResponse,
    EC2GetEbsDefaultKmsKeyIdRequest,
    EC2GetEbsDefaultKmsKeyIdResponse,
    EC2GetEbsEncryptionByDefaultRequest,
    EC2GetEbsEncryptionByDefaultResponse,
    EC2GetEnabledIpamPolicyRequest,
    EC2GetEnabledIpamPolicyResponse,
    EC2GetFlowLogsIntegrationTemplateRequest,
    EC2GetFlowLogsIntegrationTemplateResponse,
    EC2GetGroupsForCapacityReservationRequest,
    EC2GetGroupsForCapacityReservationResponse,
    EC2GetHostReservationPurchasePreviewRequest,
    EC2GetHostReservationPurchasePreviewResponse,
    EC2GetImageAncestryRequest,
    EC2GetImageAncestryResponse,
    EC2GetImageBlockPublicAccessStateRequest,
    EC2GetImageBlockPublicAccessStateResponse,
    EC2GetImageFindingsRequest,
    EC2GetImageFindingsResponse,
    EC2GetInstanceMetadataDefaultsRequest,
    EC2GetInstanceMetadataDefaultsResponse,
    EC2GetInstanceTpmEkPubRequest,
    EC2GetInstanceTpmEkPubResponse,
    EC2GetInstanceTypesFromInstanceRequirementsRequest,
    EC2GetInstanceTypesFromInstanceRequirementsResponse,
    EC2GetInstanceUefiDataRequest,
    EC2GetInstanceUefiDataResponse,
    EC2GetIpamAddressHistoryRequest,
    EC2GetIpamAddressHistoryResponse,
    EC2GetIpamDiscoveredAccountsRequest,
    EC2GetIpamDiscoveredAccountsResponse,
    EC2GetIpamDiscoveredPublicAddressesRequest,
    EC2GetIpamDiscoveredPublicAddressesResponse,
    EC2GetIpamDiscoveredResourceCidrsRequest,
    EC2GetIpamDiscoveredResourceCidrsResponse,
    EC2GetIpamDiscoveredRoutesRequest,
    EC2GetIpamDiscoveredRoutesResponse,
    EC2GetIpamInternetRegistryAssociationAsnsRequest,
    EC2GetIpamInternetRegistryAssociationAsnsResponse,
    EC2GetIpamInternetRegistryAssociationCidrsRequest,
    EC2GetIpamInternetRegistryAssociationCidrsResponse,
    EC2GetIpamPolicyAllocationRulesRequest,
    EC2GetIpamPolicyAllocationRulesResponse,
    EC2GetIpamPolicyOrganizationTargetsRequest,
    EC2GetIpamPolicyOrganizationTargetsResponse,
    EC2GetIpamPoolAllocationsRequest,
    EC2GetIpamPoolAllocationsResponse,
    EC2GetIpamPoolCidrsRequest,
    EC2GetIpamPoolCidrsResponse,
    EC2GetIpamPrefixListResolverRulesRequest,
    EC2GetIpamPrefixListResolverRulesResponse,
    EC2GetIpamPrefixListResolverVersionEntriesRequest,
    EC2GetIpamPrefixListResolverVersionEntriesResponse,
    EC2GetIpamPrefixListResolverVersionsRequest,
    EC2GetIpamPrefixListResolverVersionsResponse,
    EC2GetIpamResourceCidrsRequest,
    EC2GetIpamResourceCidrsResponse,
    EC2GetIpamRouteOriginAuthorizationsRequest,
    EC2GetIpamRouteOriginAuthorizationsResponse,
    EC2GetIpamRouteProtectionFindingsRequest,
    EC2GetIpamRouteProtectionFindingsResponse,
    EC2GetIpamRoutingPolicyRegistrationDeltasRequest,
    EC2GetIpamRoutingPolicyRegistrationDeltasResponse,
    EC2GetIpamRoutingPolicyRegistrationsRequest,
    EC2GetIpamRoutingPolicyRegistrationsResponse,
    EC2GetLaunchTemplateDataRequest,
    EC2GetLaunchTemplateDataResponse,
    EC2GetManagedPrefixListAssociationsRequest,
    EC2GetManagedPrefixListAssociationsResponse,
    EC2GetManagedPrefixListEntriesRequest,
    EC2GetManagedPrefixListEntriesResponse,
    EC2GetManagedResourceVisibilityRequest,
    EC2GetManagedResourceVisibilityResponse,
    EC2GetNetworkInsightsAccessScopeAnalysisFindingsRequest,
    EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse,
    EC2GetNetworkInsightsAccessScopeContentRequest,
    EC2GetNetworkInsightsAccessScopeContentResponse,
    EC2GetNetworkingFlexCostAllocationPolicyVersionsRequest,
    EC2GetNetworkingFlexCostAllocationPolicyVersionsResponse,
    EC2GetPasswordDataRequest,
    EC2GetPasswordDataResponse,
    EC2GetReservedInstancesExchangeQuoteRequest,
    EC2GetReservedInstancesExchangeQuoteResponse,
    EC2GetRouteServerAssociationsRequest,
    EC2GetRouteServerAssociationsResponse,
    EC2GetRouteServerPropagationsRequest,
    EC2GetRouteServerPropagationsResponse,
    EC2GetRouteServerRoutingDatabaseRequest,
    EC2GetRouteServerRoutingDatabaseResponse,
    EC2GetSecurityGroupsForVpcRequest,
    EC2GetSecurityGroupsForVpcResponse,
    EC2GetSerialConsoleAccessStatusRequest,
    EC2GetSerialConsoleAccessStatusResponse,
    EC2GetSnapshotBlockPublicAccessStateRequest,
    EC2GetSnapshotBlockPublicAccessStateResponse,
    EC2GetSpotPlacementScoresRequest,
    EC2GetSpotPlacementScoresResponse,
    EC2GetSubnetCidrReservationsRequest,
    EC2GetSubnetCidrReservationsResponse,
    EC2GetTransitGatewayAttachmentNatConfigurationRequest,
    EC2GetTransitGatewayAttachmentNatConfigurationResponse,
    EC2GetTransitGatewayAttachmentPropagationsRequest,
    EC2GetTransitGatewayAttachmentPropagationsResponse,
    EC2GetTransitGatewayMeteringPolicyEntriesRequest,
    EC2GetTransitGatewayMeteringPolicyEntriesResponse,
    EC2GetTransitGatewayMulticastDomainAssociationsRequest,
    EC2GetTransitGatewayMulticastDomainAssociationsResponse,
    EC2GetTransitGatewayPolicyTableAssociationsRequest,
    EC2GetTransitGatewayPolicyTableAssociationsResponse,
    EC2GetTransitGatewayPolicyTableEntriesRequest,
    EC2GetTransitGatewayPolicyTableEntriesResponse,
    EC2GetTransitGatewayPrefixListReferencesRequest,
    EC2GetTransitGatewayPrefixListReferencesResponse,
    EC2GetTransitGatewayRouteTableAssociationsRequest,
    EC2GetTransitGatewayRouteTableAssociationsResponse,
    EC2GetTransitGatewayRouteTablePropagationsRequest,
    EC2GetTransitGatewayRouteTablePropagationsResponse,
    EC2GetVerifiedAccessEndpointPolicyRequest,
    EC2GetVerifiedAccessEndpointPolicyResponse,
    EC2GetVerifiedAccessEndpointTargetsRequest,
    EC2GetVerifiedAccessEndpointTargetsResponse,
    EC2GetVerifiedAccessGroupPolicyRequest,
    EC2GetVerifiedAccessGroupPolicyResponse,
    EC2GetVpcResourcesBlockingEncryptionEnforcementRequest,
    EC2GetVpcResourcesBlockingEncryptionEnforcementResponse,
    EC2GetVpnConnectionDeviceSampleConfigurationRequest,
    EC2GetVpnConnectionDeviceSampleConfigurationResponse,
    EC2GetVpnConnectionDeviceTypesRequest,
    EC2GetVpnConnectionDeviceTypesResponse,
    EC2GetVpnTunnelReplacementStatusRequest,
    EC2GetVpnTunnelReplacementStatusResponse,
    EC2ImportClientVpnClientCertificateRevocationListRequest,
    EC2ImportClientVpnClientCertificateRevocationListResponse,
    EC2ImportImageRequest,
    EC2ImportImageResponse,
    EC2ImportInstanceRequest,
    EC2ImportInstanceResponse,
    EC2ImportKeyPairRequest,
    EC2ImportKeyPairResponse,
    EC2ImportSnapshotRequest,
    EC2ImportSnapshotResponse,
    EC2ImportVolumeRequest,
    EC2ImportVolumeResponse,
    EC2ListImagesInRecycleBinRequest,
    EC2ListImagesInRecycleBinResponse,
    EC2ListSnapshotsInRecycleBinRequest,
    EC2ListSnapshotsInRecycleBinResponse,
    EC2ListVolumesInRecycleBinRequest,
    EC2ListVolumesInRecycleBinResponse,
    EC2LockSnapshotRequest,
    EC2LockSnapshotResponse,
    EC2ModifyAccountVpcEncryptionControlRequest,
    EC2ModifyAccountVpcEncryptionControlResponse,
    EC2ModifyAddressAttributeRequest,
    EC2ModifyAddressAttributeResponse,
    EC2ModifyApplicationStatusCheckRequest,
    EC2ModifyApplicationStatusCheckResponse,
    EC2ModifyAvailabilityZoneGroupRequest,
    EC2ModifyAvailabilityZoneGroupResponse,
    EC2ModifyCapacityReservationFleetRequest,
    EC2ModifyCapacityReservationFleetResponse,
    EC2ModifyCapacityReservationRequest,
    EC2ModifyCapacityReservationResponse,
    EC2ModifyClientVpnEndpointAuthorizationPolicyRequest,
    EC2ModifyClientVpnEndpointAuthorizationPolicyResponse,
    EC2ModifyClientVpnEndpointRequest,
    EC2ModifyClientVpnEndpointResponse,
    EC2ModifyDefaultCreditSpecificationRequest,
    EC2ModifyDefaultCreditSpecificationResponse,
    EC2ModifyEbsDefaultKmsKeyIdRequest,
    EC2ModifyEbsDefaultKmsKeyIdResponse,
    EC2ModifyFleetRequest,
    EC2ModifyFleetResponse,
    EC2ModifyFpgaImageAttributeRequest,
    EC2ModifyFpgaImageAttributeResponse,
    EC2ModifyHostsRequest,
    EC2ModifyHostsResponse,
    EC2ModifyIdFormatRequest,
    EC2ModifyIdFormatResponse,
    EC2ModifyIdentityIdFormatRequest,
    EC2ModifyIdentityIdFormatResponse,
    EC2ModifyImageAttributeRequest,
    EC2ModifyImageAttributeResponse,
    EC2ModifyInstanceAttributeRequest,
    EC2ModifyInstanceAttributeResponse,
    EC2ModifyInstanceCapacityReservationAttributesRequest,
    EC2ModifyInstanceCapacityReservationAttributesResponse,
    EC2ModifyInstanceConnectEndpointRequest,
    EC2ModifyInstanceConnectEndpointResponse,
    EC2ModifyInstanceCpuOptionsRequest,
    EC2ModifyInstanceCpuOptionsResponse,
    EC2ModifyInstanceCreditSpecificationRequest,
    EC2ModifyInstanceCreditSpecificationResponse,
    EC2ModifyInstanceEventStartTimeRequest,
    EC2ModifyInstanceEventStartTimeResponse,
    EC2ModifyInstanceEventWindowRequest,
    EC2ModifyInstanceEventWindowResponse,
    EC2ModifyInstanceMaintenanceOptionsRequest,
    EC2ModifyInstanceMaintenanceOptionsResponse,
    EC2ModifyInstanceMetadataDefaultsRequest,
    EC2ModifyInstanceMetadataDefaultsResponse,
    EC2ModifyInstanceMetadataOptionsRequest,
    EC2ModifyInstanceMetadataOptionsResponse,
    EC2ModifyInstanceNetworkPerformanceOptionsRequest,
    EC2ModifyInstanceNetworkPerformanceOptionsResponse,
    EC2ModifyInstancePlacementRequest,
    EC2ModifyInstancePlacementResponse,
    EC2ModifyIpamPolicyAllocationRulesRequest,
    EC2ModifyIpamPolicyAllocationRulesResponse,
    EC2ModifyIpamPoolAllocationRequest,
    EC2ModifyIpamPoolAllocationResponse,
    EC2ModifyIpamPoolRequest,
    EC2ModifyIpamPoolResponse,
    EC2ModifyIpamPrefixListResolverRequest,
    EC2ModifyIpamPrefixListResolverResponse,
    EC2ModifyIpamPrefixListResolverTargetRequest,
    EC2ModifyIpamPrefixListResolverTargetResponse,
    EC2ModifyIpamRequest,
    EC2ModifyIpamResourceCidrRequest,
    EC2ModifyIpamResourceCidrResponse,
    EC2ModifyIpamResourceDiscoveryRequest,
    EC2ModifyIpamResourceDiscoveryResponse,
    EC2ModifyIpamResponse,
    EC2ModifyIpamRoutingPolicyRegistrationRequest,
    EC2ModifyIpamRoutingPolicyRegistrationResponse,
    EC2ModifyIpamScopeRequest,
    EC2ModifyIpamScopeResponse,
    EC2ModifyLaunchTemplateRequest,
    EC2ModifyLaunchTemplateResponse,
    EC2ModifyLocalGatewayRouteRequest,
    EC2ModifyLocalGatewayRouteResponse,
    EC2ModifyManagedPrefixListRequest,
    EC2ModifyManagedPrefixListResponse,
    EC2ModifyManagedResourceVisibilityRequest,
    EC2ModifyManagedResourceVisibilityResponse,
    EC2ModifyMetricCategoryRequest,
    EC2ModifyMetricCategoryResponse,
    EC2ModifyNetworkInterfaceAttributeRequest,
    EC2ModifyNetworkInterfaceAttributeResponse,
    EC2ModifyNetworkingFlexCostAllocationPolicyRequest,
    EC2ModifyNetworkingFlexCostAllocationPolicyResponse,
    EC2ModifyPrivateDnsNameOptionsRequest,
    EC2ModifyPrivateDnsNameOptionsResponse,
    EC2ModifyPublicIpDnsNameOptionsRequest,
    EC2ModifyPublicIpDnsNameOptionsResponse,
    EC2ModifyReservedInstancesRequest,
    EC2ModifyReservedInstancesResponse,
    EC2ModifyRouteServerRequest,
    EC2ModifyRouteServerResponse,
    EC2ModifySecurityGroupRulesRequest,
    EC2ModifySecurityGroupRulesResponse,
    EC2ModifySnapshotAttributeRequest,
    EC2ModifySnapshotAttributeResponse,
    EC2ModifySnapshotTierRequest,
    EC2ModifySnapshotTierResponse,
    EC2ModifySpotFleetRequestRequest,
    EC2ModifySpotFleetRequestResponse,
    EC2ModifySubnetAttributeRequest,
    EC2ModifySubnetAttributeResponse,
    EC2ModifyTrafficMirrorFilterNetworkServicesRequest,
    EC2ModifyTrafficMirrorFilterNetworkServicesResponse,
    EC2ModifyTrafficMirrorFilterRuleRequest,
    EC2ModifyTrafficMirrorFilterRuleResponse,
    EC2ModifyTrafficMirrorSessionRequest,
    EC2ModifyTrafficMirrorSessionResponse,
    EC2ModifyTransitGatewayAttachmentNatConfigurationRequest,
    EC2ModifyTransitGatewayAttachmentNatConfigurationResponse,
    EC2ModifyTransitGatewayMeteringPolicyRequest,
    EC2ModifyTransitGatewayMeteringPolicyResponse,
    EC2ModifyTransitGatewayNetworkFunctionAttachmentRequest,
    EC2ModifyTransitGatewayNetworkFunctionAttachmentResponse,
    EC2ModifyTransitGatewayPeeringAttachmentRequest,
    EC2ModifyTransitGatewayPeeringAttachmentResponse,
    EC2ModifyTransitGatewayPolicyTableEntryRequest,
    EC2ModifyTransitGatewayPolicyTableEntryResponse,
    EC2ModifyTransitGatewayPrefixListReferenceRequest,
    EC2ModifyTransitGatewayPrefixListReferenceResponse,
    EC2ModifyTransitGatewayRequest,
    EC2ModifyTransitGatewayResponse,
    EC2ModifyTransitGatewayVpcAttachmentRequest,
    EC2ModifyTransitGatewayVpcAttachmentResponse,
    EC2ModifyVerifiedAccessEndpointPolicyRequest,
    EC2ModifyVerifiedAccessEndpointPolicyResponse,
    EC2ModifyVerifiedAccessEndpointRequest,
    EC2ModifyVerifiedAccessEndpointResponse,
    EC2ModifyVerifiedAccessGroupPolicyRequest,
    EC2ModifyVerifiedAccessGroupPolicyResponse,
    EC2ModifyVerifiedAccessGroupRequest,
    EC2ModifyVerifiedAccessGroupResponse,
    EC2ModifyVerifiedAccessInstanceLoggingConfigurationRequest,
    EC2ModifyVerifiedAccessInstanceLoggingConfigurationResponse,
    EC2ModifyVerifiedAccessInstanceRequest,
    EC2ModifyVerifiedAccessInstanceResponse,
    EC2ModifyVerifiedAccessTrustProviderRequest,
    EC2ModifyVerifiedAccessTrustProviderResponse,
    EC2ModifyVolumeAttributeRequest,
    EC2ModifyVolumeAttributeResponse,
    EC2ModifyVolumeRequest,
    EC2ModifyVolumeResponse,
    EC2ModifyVpcAttributeRequest,
    EC2ModifyVpcAttributeResponse,
    EC2ModifyVpcBlockPublicAccessExclusionRequest,
    EC2ModifyVpcBlockPublicAccessExclusionResponse,
    EC2ModifyVpcBlockPublicAccessOptionsRequest,
    EC2ModifyVpcBlockPublicAccessOptionsResponse,
    EC2ModifyVpcEncryptionControlRequest,
    EC2ModifyVpcEncryptionControlResponse,
    EC2ModifyVpcEndpointConnectionNotificationRequest,
    EC2ModifyVpcEndpointConnectionNotificationResponse,
    EC2ModifyVpcEndpointPayerResponsibilityRequest,
    EC2ModifyVpcEndpointPayerResponsibilityResponse,
    EC2ModifyVpcEndpointRequest,
    EC2ModifyVpcEndpointResponse,
    EC2ModifyVpcEndpointServiceConfigurationRequest,
    EC2ModifyVpcEndpointServiceConfigurationResponse,
    EC2ModifyVpcEndpointServicePayerResponsibilityRequest,
    EC2ModifyVpcEndpointServicePayerResponsibilityResponse,
    EC2ModifyVpcEndpointServicePermissionsRequest,
    EC2ModifyVpcEndpointServicePermissionsResponse,
    EC2ModifyVpcPeeringConnectionOptionsRequest,
    EC2ModifyVpcPeeringConnectionOptionsResponse,
    EC2ModifyVpcTenancyRequest,
    EC2ModifyVpcTenancyResponse,
    EC2ModifyVpnConnectionOptionsRequest,
    EC2ModifyVpnConnectionOptionsResponse,
    EC2ModifyVpnConnectionRequest,
    EC2ModifyVpnConnectionResponse,
    EC2ModifyVpnTunnelCertificateRequest,
    EC2ModifyVpnTunnelCertificateResponse,
    EC2ModifyVpnTunnelOptionsRequest,
    EC2ModifyVpnTunnelOptionsResponse,
    EC2MonitorInstancesRequest,
    EC2MonitorInstancesResponse,
    EC2MoveAddressToVpcRequest,
    EC2MoveAddressToVpcResponse,
    EC2MoveByoipCidrToIpamRequest,
    EC2MoveByoipCidrToIpamResponse,
    EC2MoveCapacityReservationInstancesRequest,
    EC2MoveCapacityReservationInstancesResponse,
    EC2ProvisionByoipCidrRequest,
    EC2ProvisionByoipCidrResponse,
    EC2ProvisionIpamByoasnRequest,
    EC2ProvisionIpamByoasnResponse,
    EC2ProvisionIpamPoolCidrRequest,
    EC2ProvisionIpamPoolCidrResponse,
    EC2ProvisionPublicIpv4PoolCidrRequest,
    EC2ProvisionPublicIpv4PoolCidrResponse,
    EC2PurchaseCapacityBlockExtensionRequest,
    EC2PurchaseCapacityBlockExtensionResponse,
    EC2PurchaseCapacityBlockRequest,
    EC2PurchaseCapacityBlockResponse,
    EC2PurchaseHostReservationRequest,
    EC2PurchaseHostReservationResponse,
    EC2PurchaseReservedInstancesOfferingRequest,
    EC2PurchaseReservedInstancesOfferingResponse,
    EC2PurchaseScheduledInstancesRequest,
    EC2PurchaseScheduledInstancesResponse,
    EC2RegisterImageRequest,
    EC2RegisterImageResponse,
    EC2RegisterInstanceEventNotificationAttributesRequest,
    EC2RegisterInstanceEventNotificationAttributesResponse,
    EC2RegisterTransitGatewayMulticastGroupMembersRequest,
    EC2RegisterTransitGatewayMulticastGroupMembersResponse,
    EC2RegisterTransitGatewayMulticastGroupSourcesRequest,
    EC2RegisterTransitGatewayMulticastGroupSourcesResponse,
    EC2RejectCapacityReservationBillingOwnershipRequest,
    EC2RejectCapacityReservationBillingOwnershipResponse,
    EC2RejectTransitGatewayClientVpnAttachmentRequest,
    EC2RejectTransitGatewayClientVpnAttachmentResponse,
    EC2RejectTransitGatewayMulticastDomainAssociationsRequest,
    EC2RejectTransitGatewayMulticastDomainAssociationsResponse,
    EC2RejectTransitGatewayPeeringAttachmentRequest,
    EC2RejectTransitGatewayPeeringAttachmentResponse,
    EC2RejectTransitGatewayVpcAttachmentRequest,
    EC2RejectTransitGatewayVpcAttachmentResponse,
    EC2RejectVpcEndpointConnectionsRequest,
    EC2RejectVpcEndpointConnectionsResponse,
    EC2RejectVpcPeeringConnectionRequest,
    EC2RejectVpcPeeringConnectionResponse,
    EC2ReleaseAddressRequest,
    EC2ReleaseAddressResponse,
    EC2ReleaseHostsRequest,
    EC2ReleaseHostsResponse,
    EC2ReleaseIpamPoolAllocationRequest,
    EC2ReleaseIpamPoolAllocationResponse,
    EC2ReplaceIamInstanceProfileAssociationRequest,
    EC2ReplaceIamInstanceProfileAssociationResponse,
    EC2ReplaceImageCriteriaInAllowedImagesSettingsRequest,
    EC2ReplaceImageCriteriaInAllowedImagesSettingsResponse,
    EC2ReplaceImageInstanceTypeSpecificationRequest,
    EC2ReplaceImageInstanceTypeSpecificationResponse,
    EC2ReplaceNetworkAclAssociationRequest,
    EC2ReplaceNetworkAclAssociationResponse,
    EC2ReplaceNetworkAclEntryRequest,
    EC2ReplaceNetworkAclEntryResponse,
    EC2ReplaceRouteRequest,
    EC2ReplaceRouteResponse,
    EC2ReplaceRouteTableAssociationRequest,
    EC2ReplaceRouteTableAssociationResponse,
    EC2ReplaceTransitGatewayRouteRequest,
    EC2ReplaceTransitGatewayRouteResponse,
    EC2ReplaceVpnTunnelRequest,
    EC2ReplaceVpnTunnelResponse,
    EC2ReportInstanceStatusRequest,
    EC2ReportInstanceStatusResponse,
    EC2RequestSpotFleetRequest,
    EC2RequestSpotFleetResponse,
    EC2RequestSpotInstancesRequest,
    EC2RequestSpotInstancesResponse,
    EC2ResetAddressAttributeRequest,
    EC2ResetAddressAttributeResponse,
    EC2ResetEbsDefaultKmsKeyIdRequest,
    EC2ResetEbsDefaultKmsKeyIdResponse,
    EC2ResetFpgaImageAttributeRequest,
    EC2ResetFpgaImageAttributeResponse,
    EC2ResetImageAttributeRequest,
    EC2ResetImageAttributeResponse,
    EC2ResetInstanceAttributeRequest,
    EC2ResetInstanceAttributeResponse,
    EC2ResetNetworkInterfaceAttributeRequest,
    EC2ResetNetworkInterfaceAttributeResponse,
    EC2ResetSnapshotAttributeRequest,
    EC2ResetSnapshotAttributeResponse,
    EC2RestoreAddressToClassicRequest,
    EC2RestoreAddressToClassicResponse,
    EC2RestoreImageFromRecycleBinRequest,
    EC2RestoreImageFromRecycleBinResponse,
    EC2RestoreManagedPrefixListVersionRequest,
    EC2RestoreManagedPrefixListVersionResponse,
    EC2RestoreSnapshotFromRecycleBinRequest,
    EC2RestoreSnapshotFromRecycleBinResponse,
    EC2RestoreSnapshotTierRequest,
    EC2RestoreSnapshotTierResponse,
    EC2RestoreVolumeFromRecycleBinRequest,
    EC2RestoreVolumeFromRecycleBinResponse,
    EC2RevokeClientVpnIngressRequest,
    EC2RevokeClientVpnIngressResponse,
    EC2RevokeSecurityGroupEgressRequest,
    EC2RevokeSecurityGroupEgressResponse,
    EC2RevokeSecurityGroupIngressRequest,
    EC2RevokeSecurityGroupIngressResponse,
    EC2RunScheduledInstancesRequest,
    EC2RunScheduledInstancesResponse,
    EC2SearchLocalGatewayRoutesRequest,
    EC2SearchLocalGatewayRoutesResponse,
    EC2SearchTransitGatewayMulticastGroupsRequest,
    EC2SearchTransitGatewayMulticastGroupsResponse,
    EC2SearchTransitGatewayRoutesRequest,
    EC2SearchTransitGatewayRoutesResponse,
    EC2SendDiagnosticInterruptRequest,
    EC2SendDiagnosticInterruptResponse,
    EC2StartDeclarativePoliciesReportRequest,
    EC2StartDeclarativePoliciesReportResponse,
    EC2StartNetworkInsightsAccessScopeAnalysisRequest,
    EC2StartNetworkInsightsAccessScopeAnalysisResponse,
    EC2StartNetworkInsightsAnalysisRequest,
    EC2StartNetworkInsightsAnalysisResponse,
    EC2StartVpcEndpointServicePrivateDnsVerificationRequest,
    EC2StartVpcEndpointServicePrivateDnsVerificationResponse,
    EC2TerminateClientVpnConnectionsRequest,
    EC2TerminateClientVpnConnectionsResponse,
    EC2UnassignIpv6AddressesRequest,
    EC2UnassignIpv6AddressesResponse,
    EC2UnassignPrivateIpAddressesRequest,
    EC2UnassignPrivateIpAddressesResponse,
    EC2UnassignPrivateNatGatewayAddressRequest,
    EC2UnassignPrivateNatGatewayAddressResponse,
    EC2UnlockSnapshotRequest,
    EC2UnlockSnapshotResponse,
    EC2UnmonitorInstancesRequest,
    EC2UnmonitorInstancesResponse,
    EC2UpdateCapacityManagerMonitoredTagKeysRequest,
    EC2UpdateCapacityManagerMonitoredTagKeysResponse,
    EC2UpdateCapacityManagerOrganizationsAccessRequest,
    EC2UpdateCapacityManagerOrganizationsAccessResponse,
    EC2UpdateInterruptibleCapacityReservationAllocationRequest,
    EC2UpdateInterruptibleCapacityReservationAllocationResponse,
    EC2UpdateSecurityGroupRuleDescriptionsEgressRequest,
    EC2UpdateSecurityGroupRuleDescriptionsEgressResponse,
    EC2UpdateSecurityGroupRuleDescriptionsIngressRequest,
    EC2UpdateSecurityGroupRuleDescriptionsIngressResponse,
    EC2ValidateSecurityGroupQuotasForInterfaceRequest,
    EC2ValidateSecurityGroupQuotasForInterfaceResponse,
    EC2WithdrawByoipCidrRequest,
    EC2WithdrawByoipCidrResponse,
)


class AWSEC2(AWSBaseService[EC2Client]):
    service_name = 'EC2'
    boto3_service_name = 'ec2'

    def __init__(self) -> None:
        super().__init__(service_name='EC2', boto3_service_name='ec2')

    async def describe_volumes(
        self,
        query: EC2DescribeVolumesQuery | None = None,
    ) -> EC2DescribeVolumesResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_volumes,
            query or EC2DescribeVolumesQuery(),
            EC2DescribeVolumesResponse,
        )

    async def describe_volumes_paginated(
        self,
        query: EC2DescribeVolumesQuery | None = None,
    ) -> list[EC2DescribeVolumesResponse]:
        return await self._paginate(
            'describe_volumes',
            query or EC2DescribeVolumesQuery(),
            EC2DescribeVolumesResponse,
        )

    describe_results = describe_volumes
    describe_results_paginated = describe_volumes_paginated

    async def create_volume(
        self,
        request: EC2CreateVolumeRequest,
    ) -> EC2Volume:
        client = self._require_client()
        return await self._execute(client.create_volume, request, EC2Volume)

    async def delete_volume(
        self,
        request: EC2DeleteVolumeRequest,
    ) -> EC2EmptyResponse:
        client = self._require_client()
        return await self._execute(client.delete_volume, request, EC2EmptyResponse)

    async def attach_volume(
        self,
        request: EC2AttachVolumeRequest,
    ) -> EC2Attachment:
        client = self._require_client()
        return await self._execute(client.attach_volume, request, EC2Attachment)

    async def detach_volume(
        self,
        request: EC2DetachVolumeRequest,
    ) -> EC2Attachment:
        client = self._require_client()
        return await self._execute(client.detach_volume, request, EC2Attachment)

    async def describe_instances(
        self,
        request: EC2DescribeInstancesRequest | None = None,
    ) -> EC2DescribeInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_instances,
            request or EC2DescribeInstancesRequest(),
            EC2DescribeInstancesResponse,
        )

    async def describe_instances_paginated(
        self,
        request: EC2DescribeInstancesRequest | None = None,
    ) -> list[EC2DescribeInstancesResponse]:
        return await self._paginate(
            'describe_instances',
            request or EC2DescribeInstancesRequest(),
            EC2DescribeInstancesResponse,
        )

    async def run_instances(
        self,
        request: EC2RunInstancesRequest,
    ) -> EC2Reservation:
        client = self._require_client()
        return await self._execute(client.run_instances, request, EC2Reservation)

    async def start_instances(
        self,
        request: EC2StartInstancesRequest,
    ) -> EC2StartInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.start_instances,
            request,
            EC2StartInstancesResponse,
        )

    async def stop_instances(
        self,
        request: EC2StopInstancesRequest,
    ) -> EC2StopInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_instances,
            request,
            EC2StopInstancesResponse,
        )

    async def reboot_instances(
        self,
        request: EC2RebootInstancesRequest,
    ) -> EC2EmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.reboot_instances,
            request,
            EC2EmptyResponse,
        )

    async def terminate_instances(
        self,
        request: EC2TerminateInstancesRequest,
    ) -> EC2TerminateInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.terminate_instances,
            request,
            EC2TerminateInstancesResponse,
        )

    async def describe_vpcs(
        self,
        request: EC2DescribeVpcsRequest | None = None,
    ) -> EC2DescribeVpcsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_vpcs,
            request or EC2DescribeVpcsRequest(),
            EC2DescribeVpcsResponse,
        )

    async def describe_vpcs_paginated(
        self,
        request: EC2DescribeVpcsRequest | None = None,
    ) -> list[EC2DescribeVpcsResponse]:
        return await self._paginate(
            'describe_vpcs',
            request or EC2DescribeVpcsRequest(),
            EC2DescribeVpcsResponse,
        )

    async def describe_subnets(
        self,
        request: EC2DescribeSubnetsRequest | None = None,
    ) -> EC2DescribeSubnetsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_subnets,
            request or EC2DescribeSubnetsRequest(),
            EC2DescribeSubnetsResponse,
        )

    async def describe_subnets_paginated(
        self,
        request: EC2DescribeSubnetsRequest | None = None,
    ) -> list[EC2DescribeSubnetsResponse]:
        return await self._paginate(
            'describe_subnets',
            request or EC2DescribeSubnetsRequest(),
            EC2DescribeSubnetsResponse,
        )

    async def describe_security_groups(
        self,
        request: EC2DescribeSecurityGroupsRequest | None = None,
    ) -> EC2DescribeSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_security_groups,
            request or EC2DescribeSecurityGroupsRequest(),
            EC2DescribeSecurityGroupsResponse,
        )

    async def describe_security_groups_paginated(
        self,
        request: EC2DescribeSecurityGroupsRequest | None = None,
    ) -> list[EC2DescribeSecurityGroupsResponse]:
        return await self._paginate(
            'describe_security_groups',
            request or EC2DescribeSecurityGroupsRequest(),
            EC2DescribeSecurityGroupsResponse,
        )

    async def create_security_group(
        self,
        request: EC2CreateSecurityGroupRequest,
    ) -> EC2CreateSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.create_security_group,
            request,
            EC2CreateSecurityGroupResponse,
        )

    async def delete_security_group(
        self,
        request: EC2DeleteSecurityGroupRequest,
    ) -> EC2DeleteSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_security_group,
            request,
            EC2DeleteSecurityGroupResponse,
        )

    async def describe_snapshots(
        self,
        request: EC2DescribeSnapshotsRequest | None = None,
    ) -> EC2DescribeSnapshotsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_snapshots,
            request or EC2DescribeSnapshotsRequest(),
            EC2DescribeSnapshotsResponse,
        )

    async def describe_snapshots_paginated(
        self,
        request: EC2DescribeSnapshotsRequest | None = None,
    ) -> list[EC2DescribeSnapshotsResponse]:
        return await self._paginate(
            'describe_snapshots',
            request or EC2DescribeSnapshotsRequest(),
            EC2DescribeSnapshotsResponse,
        )

    async def create_snapshot(
        self,
        request: EC2CreateSnapshotRequest,
    ) -> EC2Snapshot:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, EC2Snapshot)

    async def delete_snapshot(
        self,
        request: EC2DeleteSnapshotRequest,
    ) -> EC2EmptyResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot, request, EC2EmptyResponse)

    async def create_tags(
        self,
        request: EC2CreateTagsRequest,
    ) -> EC2EmptyResponse:
        client = self._require_client()
        return await self._execute(client.create_tags, request, EC2EmptyResponse)

    async def delete_tags(
        self,
        request: EC2DeleteTagsRequest,
    ) -> EC2EmptyResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, EC2EmptyResponse)

    async def describe_key_pairs(
        self,
        request: EC2DescribeKeyPairsRequest | None = None,
    ) -> EC2DescribeKeyPairsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_key_pairs,
            request or EC2DescribeKeyPairsRequest(),
            EC2DescribeKeyPairsResponse,
        )

    async def accept_address_transfer(
        self,
        request: EC2AcceptAddressTransferRequest,
    ) -> EC2AcceptAddressTransferResponse:
        client = self._require_client()
        return await self._execute(client.accept_address_transfer, request, EC2AcceptAddressTransferResponse)

    async def accept_capacity_reservation_billing_ownership(
        self,
        request: EC2AcceptCapacityReservationBillingOwnershipRequest,
    ) -> EC2AcceptCapacityReservationBillingOwnershipResponse:
        client = self._require_client()
        return await self._execute(client.accept_capacity_reservation_billing_ownership, request, EC2AcceptCapacityReservationBillingOwnershipResponse)

    async def accept_reserved_instances_exchange_quote(
        self,
        request: EC2AcceptReservedInstancesExchangeQuoteRequest,
    ) -> EC2AcceptReservedInstancesExchangeQuoteResponse:
        client = self._require_client()
        return await self._execute(client.accept_reserved_instances_exchange_quote, request, EC2AcceptReservedInstancesExchangeQuoteResponse)

    async def accept_transit_gateway_client_vpn_attachment(
        self,
        request: EC2AcceptTransitGatewayClientVpnAttachmentRequest,
    ) -> EC2AcceptTransitGatewayClientVpnAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.accept_transit_gateway_client_vpn_attachment, request, EC2AcceptTransitGatewayClientVpnAttachmentResponse)

    async def accept_transit_gateway_multicast_domain_associations(
        self,
        request: EC2AcceptTransitGatewayMulticastDomainAssociationsRequest | None = None,
    ) -> EC2AcceptTransitGatewayMulticastDomainAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.accept_transit_gateway_multicast_domain_associations, request, EC2AcceptTransitGatewayMulticastDomainAssociationsResponse)

    async def accept_transit_gateway_peering_attachment(
        self,
        request: EC2AcceptTransitGatewayPeeringAttachmentRequest,
    ) -> EC2AcceptTransitGatewayPeeringAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.accept_transit_gateway_peering_attachment, request, EC2AcceptTransitGatewayPeeringAttachmentResponse)

    async def accept_transit_gateway_vpc_attachment(
        self,
        request: EC2AcceptTransitGatewayVpcAttachmentRequest,
    ) -> EC2AcceptTransitGatewayVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.accept_transit_gateway_vpc_attachment, request, EC2AcceptTransitGatewayVpcAttachmentResponse)

    async def accept_vpc_endpoint_connections(
        self,
        request: EC2AcceptVpcEndpointConnectionsRequest,
    ) -> EC2AcceptVpcEndpointConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.accept_vpc_endpoint_connections, request, EC2AcceptVpcEndpointConnectionsResponse)

    async def accept_vpc_peering_connection(
        self,
        request: EC2AcceptVpcPeeringConnectionRequest,
    ) -> EC2AcceptVpcPeeringConnectionResponse:
        client = self._require_client()
        return await self._execute(client.accept_vpc_peering_connection, request, EC2AcceptVpcPeeringConnectionResponse)

    async def advertise_byoip_cidr(
        self,
        request: EC2AdvertiseByoipCidrRequest,
    ) -> EC2AdvertiseByoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.advertise_byoip_cidr, request, EC2AdvertiseByoipCidrResponse)

    async def allocate_address(
        self,
        request: EC2AllocateAddressRequest | None = None,
    ) -> EC2AllocateAddressResponse:
        client = self._require_client()
        return await self._execute(client.allocate_address, request, EC2AllocateAddressResponse)

    async def allocate_hosts(
        self,
        request: EC2AllocateHostsRequest | None = None,
    ) -> EC2AllocateHostsResponse:
        client = self._require_client()
        return await self._execute(client.allocate_hosts, request, EC2AllocateHostsResponse)

    async def allocate_ipam_pool_cidr(
        self,
        request: EC2AllocateIpamPoolCidrRequest,
    ) -> EC2AllocateIpamPoolCidrResponse:
        client = self._require_client()
        return await self._execute(client.allocate_ipam_pool_cidr, request, EC2AllocateIpamPoolCidrResponse)

    async def apply_security_groups_to_client_vpn_target_network(
        self,
        request: EC2ApplySecurityGroupsToClientVpnTargetNetworkRequest,
    ) -> EC2ApplySecurityGroupsToClientVpnTargetNetworkResponse:
        client = self._require_client()
        return await self._execute(client.apply_security_groups_to_client_vpn_target_network, request, EC2ApplySecurityGroupsToClientVpnTargetNetworkResponse)

    async def assign_ipv6_addresses(
        self,
        request: EC2AssignIpv6AddressesRequest,
    ) -> EC2AssignIpv6AddressesResponse:
        client = self._require_client()
        return await self._execute(client.assign_ipv6_addresses, request, EC2AssignIpv6AddressesResponse)

    async def assign_private_ip_addresses(
        self,
        request: EC2AssignPrivateIpAddressesRequest,
    ) -> EC2AssignPrivateIpAddressesResponse:
        client = self._require_client()
        return await self._execute(client.assign_private_ip_addresses, request, EC2AssignPrivateIpAddressesResponse)

    async def assign_private_nat_gateway_address(
        self,
        request: EC2AssignPrivateNatGatewayAddressRequest,
    ) -> EC2AssignPrivateNatGatewayAddressResponse:
        client = self._require_client()
        return await self._execute(client.assign_private_nat_gateway_address, request, EC2AssignPrivateNatGatewayAddressResponse)

    async def associate_address(
        self,
        request: EC2AssociateAddressRequest | None = None,
    ) -> EC2AssociateAddressResponse:
        client = self._require_client()
        return await self._execute(client.associate_address, request, EC2AssociateAddressResponse)

    async def associate_application_status_check(
        self,
        request: EC2AssociateApplicationStatusCheckRequest,
    ) -> EC2AssociateApplicationStatusCheckResponse:
        client = self._require_client()
        return await self._execute(client.associate_application_status_check, request, EC2AssociateApplicationStatusCheckResponse)

    async def associate_capacity_reservation_billing_owner(
        self,
        request: EC2AssociateCapacityReservationBillingOwnerRequest,
    ) -> EC2AssociateCapacityReservationBillingOwnerResponse:
        client = self._require_client()
        return await self._execute(client.associate_capacity_reservation_billing_owner, request, EC2AssociateCapacityReservationBillingOwnerResponse)

    async def associate_client_vpn_target_network(
        self,
        request: EC2AssociateClientVpnTargetNetworkRequest,
    ) -> EC2AssociateClientVpnTargetNetworkResponse:
        client = self._require_client()
        return await self._execute(client.associate_client_vpn_target_network, request, EC2AssociateClientVpnTargetNetworkResponse)

    async def associate_dhcp_options(
        self,
        request: EC2AssociateDhcpOptionsRequest,
    ) -> EC2AssociateDhcpOptionsResponse:
        client = self._require_client()
        return await self._execute(client.associate_dhcp_options, request, EC2AssociateDhcpOptionsResponse)

    async def associate_enclave_certificate_iam_role(
        self,
        request: EC2AssociateEnclaveCertificateIamRoleRequest,
    ) -> EC2AssociateEnclaveCertificateIamRoleResponse:
        client = self._require_client()
        return await self._execute(client.associate_enclave_certificate_iam_role, request, EC2AssociateEnclaveCertificateIamRoleResponse)

    async def associate_iam_instance_profile(
        self,
        request: EC2AssociateIamInstanceProfileRequest,
    ) -> EC2AssociateIamInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.associate_iam_instance_profile, request, EC2AssociateIamInstanceProfileResponse)

    async def associate_instance_event_window(
        self,
        request: EC2AssociateInstanceEventWindowRequest,
    ) -> EC2AssociateInstanceEventWindowResponse:
        client = self._require_client()
        return await self._execute(client.associate_instance_event_window, request, EC2AssociateInstanceEventWindowResponse)

    async def associate_ipam_byoasn(
        self,
        request: EC2AssociateIpamByoasnRequest,
    ) -> EC2AssociateIpamByoasnResponse:
        client = self._require_client()
        return await self._execute(client.associate_ipam_byoasn, request, EC2AssociateIpamByoasnResponse)

    async def associate_ipam_resource_discovery(
        self,
        request: EC2AssociateIpamResourceDiscoveryRequest,
    ) -> EC2AssociateIpamResourceDiscoveryResponse:
        client = self._require_client()
        return await self._execute(client.associate_ipam_resource_discovery, request, EC2AssociateIpamResourceDiscoveryResponse)

    async def associate_kms_key_id(
        self,
        request: EC2AssociateKmsKeyIdRequest,
    ) -> EC2AssociateKmsKeyIdResponse:
        client = self._require_client()
        return await self._execute(client.associate_kms_key_id, request, EC2AssociateKmsKeyIdResponse)

    async def associate_nat_gateway_address(
        self,
        request: EC2AssociateNatGatewayAddressRequest,
    ) -> EC2AssociateNatGatewayAddressResponse:
        client = self._require_client()
        return await self._execute(client.associate_nat_gateway_address, request, EC2AssociateNatGatewayAddressResponse)

    async def associate_networking_flex_cost_allocation_policy(
        self,
        request: EC2AssociateNetworkingFlexCostAllocationPolicyRequest,
    ) -> EC2AssociateNetworkingFlexCostAllocationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.associate_networking_flex_cost_allocation_policy, request, EC2AssociateNetworkingFlexCostAllocationPolicyResponse)

    async def associate_route_server(
        self,
        request: EC2AssociateRouteServerRequest,
    ) -> EC2AssociateRouteServerResponse:
        client = self._require_client()
        return await self._execute(client.associate_route_server, request, EC2AssociateRouteServerResponse)

    async def associate_route_table(
        self,
        request: EC2AssociateRouteTableRequest,
    ) -> EC2AssociateRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.associate_route_table, request, EC2AssociateRouteTableResponse)

    async def associate_security_group_vpc(
        self,
        request: EC2AssociateSecurityGroupVpcRequest,
    ) -> EC2AssociateSecurityGroupVpcResponse:
        client = self._require_client()
        return await self._execute(client.associate_security_group_vpc, request, EC2AssociateSecurityGroupVpcResponse)

    async def associate_subnet_cidr_block(
        self,
        request: EC2AssociateSubnetCidrBlockRequest,
    ) -> EC2AssociateSubnetCidrBlockResponse:
        client = self._require_client()
        return await self._execute(client.associate_subnet_cidr_block, request, EC2AssociateSubnetCidrBlockResponse)

    async def associate_transit_gateway_multicast_domain(
        self,
        request: EC2AssociateTransitGatewayMulticastDomainRequest,
    ) -> EC2AssociateTransitGatewayMulticastDomainResponse:
        client = self._require_client()
        return await self._execute(client.associate_transit_gateway_multicast_domain, request, EC2AssociateTransitGatewayMulticastDomainResponse)

    async def associate_transit_gateway_policy_table(
        self,
        request: EC2AssociateTransitGatewayPolicyTableRequest,
    ) -> EC2AssociateTransitGatewayPolicyTableResponse:
        client = self._require_client()
        return await self._execute(client.associate_transit_gateway_policy_table, request, EC2AssociateTransitGatewayPolicyTableResponse)

    async def associate_transit_gateway_route_table(
        self,
        request: EC2AssociateTransitGatewayRouteTableRequest,
    ) -> EC2AssociateTransitGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.associate_transit_gateway_route_table, request, EC2AssociateTransitGatewayRouteTableResponse)

    async def associate_trunk_interface(
        self,
        request: EC2AssociateTrunkInterfaceRequest,
    ) -> EC2AssociateTrunkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.associate_trunk_interface, request, EC2AssociateTrunkInterfaceResponse)

    async def associate_vpc_cidr_block(
        self,
        request: EC2AssociateVpcCidrBlockRequest,
    ) -> EC2AssociateVpcCidrBlockResponse:
        client = self._require_client()
        return await self._execute(client.associate_vpc_cidr_block, request, EC2AssociateVpcCidrBlockResponse)

    async def attach_classic_link_vpc(
        self,
        request: EC2AttachClassicLinkVpcRequest,
    ) -> EC2AttachClassicLinkVpcResponse:
        client = self._require_client()
        return await self._execute(client.attach_classic_link_vpc, request, EC2AttachClassicLinkVpcResponse)

    async def attach_image_watermark(
        self,
        request: EC2AttachImageWatermarkRequest,
    ) -> EC2AttachImageWatermarkResponse:
        client = self._require_client()
        return await self._execute(client.attach_image_watermark, request, EC2AttachImageWatermarkResponse)

    async def attach_internet_gateway(
        self,
        request: EC2AttachInternetGatewayRequest,
    ) -> EC2AttachInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.attach_internet_gateway, request, EC2AttachInternetGatewayResponse)

    async def attach_network_interface(
        self,
        request: EC2AttachNetworkInterfaceRequest,
    ) -> EC2AttachNetworkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.attach_network_interface, request, EC2AttachNetworkInterfaceResponse)

    async def attach_verified_access_trust_provider(
        self,
        request: EC2AttachVerifiedAccessTrustProviderRequest,
    ) -> EC2AttachVerifiedAccessTrustProviderResponse:
        client = self._require_client()
        return await self._execute(client.attach_verified_access_trust_provider, request, EC2AttachVerifiedAccessTrustProviderResponse)

    async def attach_vpn_gateway(
        self,
        request: EC2AttachVpnGatewayRequest,
    ) -> EC2AttachVpnGatewayResponse:
        client = self._require_client()
        return await self._execute(client.attach_vpn_gateway, request, EC2AttachVpnGatewayResponse)

    async def authorize_client_vpn_ingress(
        self,
        request: EC2AuthorizeClientVpnIngressRequest,
    ) -> EC2AuthorizeClientVpnIngressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_client_vpn_ingress, request, EC2AuthorizeClientVpnIngressResponse)

    async def authorize_security_group_egress(
        self,
        request: EC2AuthorizeSecurityGroupEgressRequest,
    ) -> EC2AuthorizeSecurityGroupEgressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_security_group_egress, request, EC2AuthorizeSecurityGroupEgressResponse)

    async def authorize_security_group_ingress(
        self,
        request: EC2AuthorizeSecurityGroupIngressRequest | None = None,
    ) -> EC2AuthorizeSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_security_group_ingress, request, EC2AuthorizeSecurityGroupIngressResponse)

    async def batch_modify_ipam_routing_policy_registrations(
        self,
        request: EC2BatchModifyIpamRoutingPolicyRegistrationsRequest,
    ) -> EC2BatchModifyIpamRoutingPolicyRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_modify_ipam_routing_policy_registrations, request, EC2BatchModifyIpamRoutingPolicyRegistrationsResponse)

    async def bundle_instance(
        self,
        request: EC2BundleInstanceRequest,
    ) -> EC2BundleInstanceResponse:
        client = self._require_client()
        return await self._execute(client.bundle_instance, request, EC2BundleInstanceResponse)

    async def cancel_bundle_task(
        self,
        request: EC2CancelBundleTaskRequest,
    ) -> EC2CancelBundleTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_bundle_task, request, EC2CancelBundleTaskResponse)

    async def cancel_capacity_reservation(
        self,
        request: EC2CancelCapacityReservationRequest,
    ) -> EC2CancelCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_capacity_reservation, request, EC2CancelCapacityReservationResponse)

    async def cancel_capacity_reservation_fleets(
        self,
        request: EC2CancelCapacityReservationFleetsRequest,
    ) -> EC2CancelCapacityReservationFleetsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_capacity_reservation_fleets, request, EC2CancelCapacityReservationFleetsResponse)

    async def cancel_conversion_task(
        self,
        request: EC2CancelConversionTaskRequest,
    ) -> EC2CancelConversionTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_conversion_task, request, EC2CancelConversionTaskResponse)

    async def cancel_declarative_policies_report(
        self,
        request: EC2CancelDeclarativePoliciesReportRequest,
    ) -> EC2CancelDeclarativePoliciesReportResponse:
        client = self._require_client()
        return await self._execute(client.cancel_declarative_policies_report, request, EC2CancelDeclarativePoliciesReportResponse)

    async def cancel_export_task(
        self,
        request: EC2CancelExportTaskRequest,
    ) -> EC2CancelExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_export_task, request, EC2CancelExportTaskResponse)

    async def cancel_image_launch_permission(
        self,
        request: EC2CancelImageLaunchPermissionRequest,
    ) -> EC2CancelImageLaunchPermissionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_image_launch_permission, request, EC2CancelImageLaunchPermissionResponse)

    async def cancel_import_task(
        self,
        request: EC2CancelImportTaskRequest | None = None,
    ) -> EC2CancelImportTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_import_task, request, EC2CancelImportTaskResponse)

    async def cancel_reserved_instances_listing(
        self,
        request: EC2CancelReservedInstancesListingRequest,
    ) -> EC2CancelReservedInstancesListingResponse:
        client = self._require_client()
        return await self._execute(client.cancel_reserved_instances_listing, request, EC2CancelReservedInstancesListingResponse)

    async def cancel_spot_fleet_requests(
        self,
        request: EC2CancelSpotFleetRequestsRequest,
    ) -> EC2CancelSpotFleetRequestsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_spot_fleet_requests, request, EC2CancelSpotFleetRequestsResponse)

    async def cancel_spot_instance_requests(
        self,
        request: EC2CancelSpotInstanceRequestsRequest,
    ) -> EC2CancelSpotInstanceRequestsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_spot_instance_requests, request, EC2CancelSpotInstanceRequestsResponse)

    async def confirm_product_instance(
        self,
        request: EC2ConfirmProductInstanceRequest,
    ) -> EC2ConfirmProductInstanceResponse:
        client = self._require_client()
        return await self._execute(client.confirm_product_instance, request, EC2ConfirmProductInstanceResponse)

    async def copy_fpga_image(
        self,
        request: EC2CopyFpgaImageRequest,
    ) -> EC2CopyFpgaImageResponse:
        client = self._require_client()
        return await self._execute(client.copy_fpga_image, request, EC2CopyFpgaImageResponse)

    async def copy_image(
        self,
        request: EC2CopyImageRequest,
    ) -> EC2CopyImageResponse:
        client = self._require_client()
        return await self._execute(client.copy_image, request, EC2CopyImageResponse)

    async def copy_snapshot(
        self,
        request: EC2CopySnapshotRequest,
    ) -> EC2CopySnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_snapshot, request, EC2CopySnapshotResponse)

    async def copy_volumes(
        self,
        request: EC2CopyVolumesRequest,
    ) -> EC2CopyVolumesResponse:
        client = self._require_client()
        return await self._execute(client.copy_volumes, request, EC2CopyVolumesResponse)

    async def create_application_status_check(
        self,
        request: EC2CreateApplicationStatusCheckRequest,
    ) -> EC2CreateApplicationStatusCheckResponse:
        client = self._require_client()
        return await self._execute(client.create_application_status_check, request, EC2CreateApplicationStatusCheckResponse)

    async def create_capacity_manager_data_export(
        self,
        request: EC2CreateCapacityManagerDataExportRequest,
    ) -> EC2CreateCapacityManagerDataExportResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_manager_data_export, request, EC2CreateCapacityManagerDataExportResponse)

    async def create_capacity_reservation(
        self,
        request: EC2CreateCapacityReservationRequest,
    ) -> EC2CreateCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation, request, EC2CreateCapacityReservationResponse)

    async def create_capacity_reservation_by_splitting(
        self,
        request: EC2CreateCapacityReservationBySplittingRequest,
    ) -> EC2CreateCapacityReservationBySplittingResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation_by_splitting, request, EC2CreateCapacityReservationBySplittingResponse)

    async def create_capacity_reservation_cancellation_quote(
        self,
        request: EC2CreateCapacityReservationCancellationQuoteRequest,
    ) -> EC2CreateCapacityReservationCancellationQuoteResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation_cancellation_quote, request, EC2CreateCapacityReservationCancellationQuoteResponse)

    async def create_capacity_reservation_date_change_quote(
        self,
        request: EC2CreateCapacityReservationDateChangeQuoteRequest,
    ) -> EC2CreateCapacityReservationDateChangeQuoteResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation_date_change_quote, request, EC2CreateCapacityReservationDateChangeQuoteResponse)

    async def create_capacity_reservation_fleet(
        self,
        request: EC2CreateCapacityReservationFleetRequest,
    ) -> EC2CreateCapacityReservationFleetResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation_fleet, request, EC2CreateCapacityReservationFleetResponse)

    async def create_carrier_gateway(
        self,
        request: EC2CreateCarrierGatewayRequest,
    ) -> EC2CreateCarrierGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_carrier_gateway, request, EC2CreateCarrierGatewayResponse)

    async def create_client_vpn_endpoint(
        self,
        request: EC2CreateClientVpnEndpointRequest,
    ) -> EC2CreateClientVpnEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_client_vpn_endpoint, request, EC2CreateClientVpnEndpointResponse)

    async def create_client_vpn_route(
        self,
        request: EC2CreateClientVpnRouteRequest,
    ) -> EC2CreateClientVpnRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_client_vpn_route, request, EC2CreateClientVpnRouteResponse)

    async def create_coip_cidr(
        self,
        request: EC2CreateCoipCidrRequest,
    ) -> EC2CreateCoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.create_coip_cidr, request, EC2CreateCoipCidrResponse)

    async def create_coip_pool(
        self,
        request: EC2CreateCoipPoolRequest,
    ) -> EC2CreateCoipPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_coip_pool, request, EC2CreateCoipPoolResponse)

    async def create_customer_gateway(
        self,
        request: EC2CreateCustomerGatewayRequest,
    ) -> EC2CreateCustomerGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_customer_gateway, request, EC2CreateCustomerGatewayResponse)

    async def create_default_subnet(
        self,
        request: EC2CreateDefaultSubnetRequest | None = None,
    ) -> EC2CreateDefaultSubnetResponse:
        client = self._require_client()
        return await self._execute(client.create_default_subnet, request, EC2CreateDefaultSubnetResponse)

    async def create_default_vpc(
        self,
        request: EC2CreateDefaultVpcRequest | None = None,
    ) -> EC2CreateDefaultVpcResponse:
        client = self._require_client()
        return await self._execute(client.create_default_vpc, request, EC2CreateDefaultVpcResponse)

    async def create_delegate_mac_volume_ownership_task(
        self,
        request: EC2CreateDelegateMacVolumeOwnershipTaskRequest,
    ) -> EC2CreateDelegateMacVolumeOwnershipTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_delegate_mac_volume_ownership_task, request, EC2CreateDelegateMacVolumeOwnershipTaskResponse)

    async def create_dhcp_options(
        self,
        request: EC2CreateDhcpOptionsRequest,
    ) -> EC2CreateDhcpOptionsResponse:
        client = self._require_client()
        return await self._execute(client.create_dhcp_options, request, EC2CreateDhcpOptionsResponse)

    async def create_egress_only_internet_gateway(
        self,
        request: EC2CreateEgressOnlyInternetGatewayRequest,
    ) -> EC2CreateEgressOnlyInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_egress_only_internet_gateway, request, EC2CreateEgressOnlyInternetGatewayResponse)

    async def create_fleet(
        self,
        request: EC2CreateFleetRequest,
    ) -> EC2CreateFleetResponse:
        client = self._require_client()
        return await self._execute(client.create_fleet, request, EC2CreateFleetResponse)

    async def create_flow_logs(
        self,
        request: EC2CreateFlowLogsRequest,
    ) -> EC2CreateFlowLogsResponse:
        client = self._require_client()
        return await self._execute(client.create_flow_logs, request, EC2CreateFlowLogsResponse)

    async def create_fpga_image(
        self,
        request: EC2CreateFpgaImageRequest,
    ) -> EC2CreateFpgaImageResponse:
        client = self._require_client()
        return await self._execute(client.create_fpga_image, request, EC2CreateFpgaImageResponse)

    async def create_image(
        self,
        request: EC2CreateImageRequest,
    ) -> EC2CreateImageResponse:
        client = self._require_client()
        return await self._execute(client.create_image, request, EC2CreateImageResponse)

    async def create_image_usage_report(
        self,
        request: EC2CreateImageUsageReportRequest,
    ) -> EC2CreateImageUsageReportResponse:
        client = self._require_client()
        return await self._execute(client.create_image_usage_report, request, EC2CreateImageUsageReportResponse)

    async def create_instance_connect_endpoint(
        self,
        request: EC2CreateInstanceConnectEndpointRequest,
    ) -> EC2CreateInstanceConnectEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_connect_endpoint, request, EC2CreateInstanceConnectEndpointResponse)

    async def create_instance_event_window(
        self,
        request: EC2CreateInstanceEventWindowRequest | None = None,
    ) -> EC2CreateInstanceEventWindowResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_event_window, request, EC2CreateInstanceEventWindowResponse)

    async def create_instance_export_task(
        self,
        request: EC2CreateInstanceExportTaskRequest,
    ) -> EC2CreateInstanceExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_export_task, request, EC2CreateInstanceExportTaskResponse)

    async def create_internet_gateway(
        self,
        request: EC2CreateInternetGatewayRequest | None = None,
    ) -> EC2CreateInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_internet_gateway, request, EC2CreateInternetGatewayResponse)

    async def create_interruptible_capacity_reservation_allocation(
        self,
        request: EC2CreateInterruptibleCapacityReservationAllocationRequest,
    ) -> EC2CreateInterruptibleCapacityReservationAllocationResponse:
        client = self._require_client()
        return await self._execute(client.create_interruptible_capacity_reservation_allocation, request, EC2CreateInterruptibleCapacityReservationAllocationResponse)

    async def create_ipam(
        self,
        request: EC2CreateIpamRequest | None = None,
    ) -> EC2CreateIpamResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam, request, EC2CreateIpamResponse)

    async def create_ipam_external_resource_verification_token(
        self,
        request: EC2CreateIpamExternalResourceVerificationTokenRequest,
    ) -> EC2CreateIpamExternalResourceVerificationTokenResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_external_resource_verification_token, request, EC2CreateIpamExternalResourceVerificationTokenResponse)

    async def create_ipam_internet_registry_association(
        self,
        request: EC2CreateIpamInternetRegistryAssociationRequest,
    ) -> EC2CreateIpamInternetRegistryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_internet_registry_association, request, EC2CreateIpamInternetRegistryAssociationResponse)

    async def create_ipam_policy(
        self,
        request: EC2CreateIpamPolicyRequest,
    ) -> EC2CreateIpamPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_policy, request, EC2CreateIpamPolicyResponse)

    async def create_ipam_pool(
        self,
        request: EC2CreateIpamPoolRequest,
    ) -> EC2CreateIpamPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_pool, request, EC2CreateIpamPoolResponse)

    async def create_ipam_prefix_list_resolver(
        self,
        request: EC2CreateIpamPrefixListResolverRequest,
    ) -> EC2CreateIpamPrefixListResolverResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_prefix_list_resolver, request, EC2CreateIpamPrefixListResolverResponse)

    async def create_ipam_prefix_list_resolver_target(
        self,
        request: EC2CreateIpamPrefixListResolverTargetRequest,
    ) -> EC2CreateIpamPrefixListResolverTargetResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_prefix_list_resolver_target, request, EC2CreateIpamPrefixListResolverTargetResponse)

    async def create_ipam_resource_discovery(
        self,
        request: EC2CreateIpamResourceDiscoveryRequest | None = None,
    ) -> EC2CreateIpamResourceDiscoveryResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_resource_discovery, request, EC2CreateIpamResourceDiscoveryResponse)

    async def create_ipam_routing_policy_registration(
        self,
        request: EC2CreateIpamRoutingPolicyRegistrationRequest,
    ) -> EC2CreateIpamRoutingPolicyRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_routing_policy_registration, request, EC2CreateIpamRoutingPolicyRegistrationResponse)

    async def create_ipam_scope(
        self,
        request: EC2CreateIpamScopeRequest,
    ) -> EC2CreateIpamScopeResponse:
        client = self._require_client()
        return await self._execute(client.create_ipam_scope, request, EC2CreateIpamScopeResponse)

    async def create_key_pair(
        self,
        request: EC2CreateKeyPairRequest,
    ) -> EC2CreateKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.create_key_pair, request, EC2CreateKeyPairResponse)

    async def create_launch_template(
        self,
        request: EC2CreateLaunchTemplateRequest,
    ) -> EC2CreateLaunchTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_launch_template, request, EC2CreateLaunchTemplateResponse)

    async def create_launch_template_version(
        self,
        request: EC2CreateLaunchTemplateVersionRequest,
    ) -> EC2CreateLaunchTemplateVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_launch_template_version, request, EC2CreateLaunchTemplateVersionResponse)

    async def create_local_gateway_route(
        self,
        request: EC2CreateLocalGatewayRouteRequest,
    ) -> EC2CreateLocalGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_route, request, EC2CreateLocalGatewayRouteResponse)

    async def create_local_gateway_route_table(
        self,
        request: EC2CreateLocalGatewayRouteTableRequest,
    ) -> EC2CreateLocalGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_route_table, request, EC2CreateLocalGatewayRouteTableResponse)

    async def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        request: EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
    ) -> EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_route_table_virtual_interface_group_association, request, EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse)

    async def create_local_gateway_route_table_vpc_association(
        self,
        request: EC2CreateLocalGatewayRouteTableVpcAssociationRequest,
    ) -> EC2CreateLocalGatewayRouteTableVpcAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_route_table_vpc_association, request, EC2CreateLocalGatewayRouteTableVpcAssociationResponse)

    async def create_local_gateway_virtual_interface(
        self,
        request: EC2CreateLocalGatewayVirtualInterfaceRequest,
    ) -> EC2CreateLocalGatewayVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_virtual_interface, request, EC2CreateLocalGatewayVirtualInterfaceResponse)

    async def create_local_gateway_virtual_interface_group(
        self,
        request: EC2CreateLocalGatewayVirtualInterfaceGroupRequest,
    ) -> EC2CreateLocalGatewayVirtualInterfaceGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_local_gateway_virtual_interface_group, request, EC2CreateLocalGatewayVirtualInterfaceGroupResponse)

    async def create_mac_system_integrity_protection_modification_task(
        self,
        request: EC2CreateMacSystemIntegrityProtectionModificationTaskRequest,
    ) -> EC2CreateMacSystemIntegrityProtectionModificationTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_mac_system_integrity_protection_modification_task, request, EC2CreateMacSystemIntegrityProtectionModificationTaskResponse)

    async def create_managed_prefix_list(
        self,
        request: EC2CreateManagedPrefixListRequest,
    ) -> EC2CreateManagedPrefixListResponse:
        client = self._require_client()
        return await self._execute(client.create_managed_prefix_list, request, EC2CreateManagedPrefixListResponse)

    async def create_metric_category(
        self,
        request: EC2CreateMetricCategoryRequest,
    ) -> EC2CreateMetricCategoryResponse:
        client = self._require_client()
        return await self._execute(client.create_metric_category, request, EC2CreateMetricCategoryResponse)

    async def create_nat_gateway(
        self,
        request: EC2CreateNatGatewayRequest | None = None,
    ) -> EC2CreateNatGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_nat_gateway, request, EC2CreateNatGatewayResponse)

    async def create_network_acl(
        self,
        request: EC2CreateNetworkAclRequest,
    ) -> EC2CreateNetworkAclResponse:
        client = self._require_client()
        return await self._execute(client.create_network_acl, request, EC2CreateNetworkAclResponse)

    async def create_network_acl_entry(
        self,
        request: EC2CreateNetworkAclEntryRequest,
    ) -> EC2CreateNetworkAclEntryResponse:
        client = self._require_client()
        return await self._execute(client.create_network_acl_entry, request, EC2CreateNetworkAclEntryResponse)

    async def create_network_insights_access_scope(
        self,
        request: EC2CreateNetworkInsightsAccessScopeRequest,
    ) -> EC2CreateNetworkInsightsAccessScopeResponse:
        client = self._require_client()
        return await self._execute(client.create_network_insights_access_scope, request, EC2CreateNetworkInsightsAccessScopeResponse)

    async def create_network_insights_path(
        self,
        request: EC2CreateNetworkInsightsPathRequest,
    ) -> EC2CreateNetworkInsightsPathResponse:
        client = self._require_client()
        return await self._execute(client.create_network_insights_path, request, EC2CreateNetworkInsightsPathResponse)

    async def create_network_interface(
        self,
        request: EC2CreateNetworkInterfaceRequest,
    ) -> EC2CreateNetworkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.create_network_interface, request, EC2CreateNetworkInterfaceResponse)

    async def create_network_interface_permission(
        self,
        request: EC2CreateNetworkInterfacePermissionRequest,
    ) -> EC2CreateNetworkInterfacePermissionResponse:
        client = self._require_client()
        return await self._execute(client.create_network_interface_permission, request, EC2CreateNetworkInterfacePermissionResponse)

    async def create_networking_flex_cost_allocation_policy(
        self,
        request: EC2CreateNetworkingFlexCostAllocationPolicyRequest,
    ) -> EC2CreateNetworkingFlexCostAllocationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_networking_flex_cost_allocation_policy, request, EC2CreateNetworkingFlexCostAllocationPolicyResponse)

    async def create_placement_group(
        self,
        request: EC2CreatePlacementGroupRequest | None = None,
    ) -> EC2CreatePlacementGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_placement_group, request, EC2CreatePlacementGroupResponse)

    async def create_public_ipv4_pool(
        self,
        request: EC2CreatePublicIpv4PoolRequest | None = None,
    ) -> EC2CreatePublicIpv4PoolResponse:
        client = self._require_client()
        return await self._execute(client.create_public_ipv4_pool, request, EC2CreatePublicIpv4PoolResponse)

    async def create_replace_root_volume_task(
        self,
        request: EC2CreateReplaceRootVolumeTaskRequest,
    ) -> EC2CreateReplaceRootVolumeTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_replace_root_volume_task, request, EC2CreateReplaceRootVolumeTaskResponse)

    async def create_reserved_instances_listing(
        self,
        request: EC2CreateReservedInstancesListingRequest,
    ) -> EC2CreateReservedInstancesListingResponse:
        client = self._require_client()
        return await self._execute(client.create_reserved_instances_listing, request, EC2CreateReservedInstancesListingResponse)

    async def create_restore_image_task(
        self,
        request: EC2CreateRestoreImageTaskRequest,
    ) -> EC2CreateRestoreImageTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_restore_image_task, request, EC2CreateRestoreImageTaskResponse)

    async def create_route(
        self,
        request: EC2CreateRouteRequest,
    ) -> EC2CreateRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_route, request, EC2CreateRouteResponse)

    async def create_route_server(
        self,
        request: EC2CreateRouteServerRequest,
    ) -> EC2CreateRouteServerResponse:
        client = self._require_client()
        return await self._execute(client.create_route_server, request, EC2CreateRouteServerResponse)

    async def create_route_server_endpoint(
        self,
        request: EC2CreateRouteServerEndpointRequest,
    ) -> EC2CreateRouteServerEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_route_server_endpoint, request, EC2CreateRouteServerEndpointResponse)

    async def create_route_server_peer(
        self,
        request: EC2CreateRouteServerPeerRequest,
    ) -> EC2CreateRouteServerPeerResponse:
        client = self._require_client()
        return await self._execute(client.create_route_server_peer, request, EC2CreateRouteServerPeerResponse)

    async def create_route_table(
        self,
        request: EC2CreateRouteTableRequest,
    ) -> EC2CreateRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.create_route_table, request, EC2CreateRouteTableResponse)

    async def create_secondary_network(
        self,
        request: EC2CreateSecondaryNetworkRequest,
    ) -> EC2CreateSecondaryNetworkResponse:
        client = self._require_client()
        return await self._execute(client.create_secondary_network, request, EC2CreateSecondaryNetworkResponse)

    async def create_secondary_subnet(
        self,
        request: EC2CreateSecondarySubnetRequest,
    ) -> EC2CreateSecondarySubnetResponse:
        client = self._require_client()
        return await self._execute(client.create_secondary_subnet, request, EC2CreateSecondarySubnetResponse)

    async def create_snapshots(
        self,
        request: EC2CreateSnapshotsRequest,
    ) -> EC2CreateSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshots, request, EC2CreateSnapshotsResponse)

    async def create_spot_datafeed_subscription(
        self,
        request: EC2CreateSpotDatafeedSubscriptionRequest,
    ) -> EC2CreateSpotDatafeedSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_spot_datafeed_subscription, request, EC2CreateSpotDatafeedSubscriptionResponse)

    async def create_store_image_task(
        self,
        request: EC2CreateStoreImageTaskRequest,
    ) -> EC2CreateStoreImageTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_store_image_task, request, EC2CreateStoreImageTaskResponse)

    async def create_subnet(
        self,
        request: EC2CreateSubnetRequest,
    ) -> EC2CreateSubnetResponse:
        client = self._require_client()
        return await self._execute(client.create_subnet, request, EC2CreateSubnetResponse)

    async def create_subnet_cidr_reservation(
        self,
        request: EC2CreateSubnetCidrReservationRequest,
    ) -> EC2CreateSubnetCidrReservationResponse:
        client = self._require_client()
        return await self._execute(client.create_subnet_cidr_reservation, request, EC2CreateSubnetCidrReservationResponse)

    async def create_traffic_mirror_filter(
        self,
        request: EC2CreateTrafficMirrorFilterRequest | None = None,
    ) -> EC2CreateTrafficMirrorFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_mirror_filter, request, EC2CreateTrafficMirrorFilterResponse)

    async def create_traffic_mirror_filter_rule(
        self,
        request: EC2CreateTrafficMirrorFilterRuleRequest,
    ) -> EC2CreateTrafficMirrorFilterRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_mirror_filter_rule, request, EC2CreateTrafficMirrorFilterRuleResponse)

    async def create_traffic_mirror_session(
        self,
        request: EC2CreateTrafficMirrorSessionRequest,
    ) -> EC2CreateTrafficMirrorSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_mirror_session, request, EC2CreateTrafficMirrorSessionResponse)

    async def create_traffic_mirror_target(
        self,
        request: EC2CreateTrafficMirrorTargetRequest | None = None,
    ) -> EC2CreateTrafficMirrorTargetResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_mirror_target, request, EC2CreateTrafficMirrorTargetResponse)

    async def create_transit_gateway(
        self,
        request: EC2CreateTransitGatewayRequest | None = None,
    ) -> EC2CreateTransitGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway, request, EC2CreateTransitGatewayResponse)

    async def create_transit_gateway_connect(
        self,
        request: EC2CreateTransitGatewayConnectRequest,
    ) -> EC2CreateTransitGatewayConnectResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_connect, request, EC2CreateTransitGatewayConnectResponse)

    async def create_transit_gateway_connect_peer(
        self,
        request: EC2CreateTransitGatewayConnectPeerRequest,
    ) -> EC2CreateTransitGatewayConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_connect_peer, request, EC2CreateTransitGatewayConnectPeerResponse)

    async def create_transit_gateway_metering_policy(
        self,
        request: EC2CreateTransitGatewayMeteringPolicyRequest,
    ) -> EC2CreateTransitGatewayMeteringPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_metering_policy, request, EC2CreateTransitGatewayMeteringPolicyResponse)

    async def create_transit_gateway_metering_policy_entry(
        self,
        request: EC2CreateTransitGatewayMeteringPolicyEntryRequest,
    ) -> EC2CreateTransitGatewayMeteringPolicyEntryResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_metering_policy_entry, request, EC2CreateTransitGatewayMeteringPolicyEntryResponse)

    async def create_transit_gateway_multicast_domain(
        self,
        request: EC2CreateTransitGatewayMulticastDomainRequest,
    ) -> EC2CreateTransitGatewayMulticastDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_multicast_domain, request, EC2CreateTransitGatewayMulticastDomainResponse)

    async def create_transit_gateway_network_function_attachment(
        self,
        request: EC2CreateTransitGatewayNetworkFunctionAttachmentRequest,
    ) -> EC2CreateTransitGatewayNetworkFunctionAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_network_function_attachment, request, EC2CreateTransitGatewayNetworkFunctionAttachmentResponse)

    async def create_transit_gateway_peering_attachment(
        self,
        request: EC2CreateTransitGatewayPeeringAttachmentRequest,
    ) -> EC2CreateTransitGatewayPeeringAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_peering_attachment, request, EC2CreateTransitGatewayPeeringAttachmentResponse)

    async def create_transit_gateway_policy_table(
        self,
        request: EC2CreateTransitGatewayPolicyTableRequest,
    ) -> EC2CreateTransitGatewayPolicyTableResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_policy_table, request, EC2CreateTransitGatewayPolicyTableResponse)

    async def create_transit_gateway_policy_table_entry(
        self,
        request: EC2CreateTransitGatewayPolicyTableEntryRequest,
    ) -> EC2CreateTransitGatewayPolicyTableEntryResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_policy_table_entry, request, EC2CreateTransitGatewayPolicyTableEntryResponse)

    async def create_transit_gateway_prefix_list_reference(
        self,
        request: EC2CreateTransitGatewayPrefixListReferenceRequest,
    ) -> EC2CreateTransitGatewayPrefixListReferenceResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_prefix_list_reference, request, EC2CreateTransitGatewayPrefixListReferenceResponse)

    async def create_transit_gateway_route(
        self,
        request: EC2CreateTransitGatewayRouteRequest,
    ) -> EC2CreateTransitGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_route, request, EC2CreateTransitGatewayRouteResponse)

    async def create_transit_gateway_route_table(
        self,
        request: EC2CreateTransitGatewayRouteTableRequest,
    ) -> EC2CreateTransitGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_route_table, request, EC2CreateTransitGatewayRouteTableResponse)

    async def create_transit_gateway_route_table_announcement(
        self,
        request: EC2CreateTransitGatewayRouteTableAnnouncementRequest,
    ) -> EC2CreateTransitGatewayRouteTableAnnouncementResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_route_table_announcement, request, EC2CreateTransitGatewayRouteTableAnnouncementResponse)

    async def create_transit_gateway_vpc_attachment(
        self,
        request: EC2CreateTransitGatewayVpcAttachmentRequest,
    ) -> EC2CreateTransitGatewayVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_vpc_attachment, request, EC2CreateTransitGatewayVpcAttachmentResponse)

    async def create_verified_access_endpoint(
        self,
        request: EC2CreateVerifiedAccessEndpointRequest,
    ) -> EC2CreateVerifiedAccessEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_verified_access_endpoint, request, EC2CreateVerifiedAccessEndpointResponse)

    async def create_verified_access_group(
        self,
        request: EC2CreateVerifiedAccessGroupRequest,
    ) -> EC2CreateVerifiedAccessGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_verified_access_group, request, EC2CreateVerifiedAccessGroupResponse)

    async def create_verified_access_instance(
        self,
        request: EC2CreateVerifiedAccessInstanceRequest | None = None,
    ) -> EC2CreateVerifiedAccessInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_verified_access_instance, request, EC2CreateVerifiedAccessInstanceResponse)

    async def create_verified_access_trust_provider(
        self,
        request: EC2CreateVerifiedAccessTrustProviderRequest,
    ) -> EC2CreateVerifiedAccessTrustProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_verified_access_trust_provider, request, EC2CreateVerifiedAccessTrustProviderResponse)

    async def create_vpc(
        self,
        request: EC2CreateVpcRequest | None = None,
    ) -> EC2CreateVpcResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc, request, EC2CreateVpcResponse)

    async def create_vpc_block_public_access_exclusion(
        self,
        request: EC2CreateVpcBlockPublicAccessExclusionRequest,
    ) -> EC2CreateVpcBlockPublicAccessExclusionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_block_public_access_exclusion, request, EC2CreateVpcBlockPublicAccessExclusionResponse)

    async def create_vpc_encryption_control(
        self,
        request: EC2CreateVpcEncryptionControlRequest,
    ) -> EC2CreateVpcEncryptionControlResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_encryption_control, request, EC2CreateVpcEncryptionControlResponse)

    async def create_vpc_endpoint(
        self,
        request: EC2CreateVpcEndpointRequest,
    ) -> EC2CreateVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_endpoint, request, EC2CreateVpcEndpointResponse)

    async def create_vpc_endpoint_connection_notification(
        self,
        request: EC2CreateVpcEndpointConnectionNotificationRequest,
    ) -> EC2CreateVpcEndpointConnectionNotificationResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_endpoint_connection_notification, request, EC2CreateVpcEndpointConnectionNotificationResponse)

    async def create_vpc_endpoint_service_configuration(
        self,
        request: EC2CreateVpcEndpointServiceConfigurationRequest | None = None,
    ) -> EC2CreateVpcEndpointServiceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_endpoint_service_configuration, request, EC2CreateVpcEndpointServiceConfigurationResponse)

    async def create_vpc_peering_connection(
        self,
        request: EC2CreateVpcPeeringConnectionRequest,
    ) -> EC2CreateVpcPeeringConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_peering_connection, request, EC2CreateVpcPeeringConnectionResponse)

    async def create_vpn_concentrator(
        self,
        request: EC2CreateVpnConcentratorRequest,
    ) -> EC2CreateVpnConcentratorResponse:
        client = self._require_client()
        return await self._execute(client.create_vpn_concentrator, request, EC2CreateVpnConcentratorResponse)

    async def create_vpn_connection(
        self,
        request: EC2CreateVpnConnectionRequest,
    ) -> EC2CreateVpnConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpn_connection, request, EC2CreateVpnConnectionResponse)

    async def create_vpn_connection_route(
        self,
        request: EC2CreateVpnConnectionRouteRequest,
    ) -> EC2CreateVpnConnectionRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_vpn_connection_route, request, EC2CreateVpnConnectionRouteResponse)

    async def create_vpn_gateway(
        self,
        request: EC2CreateVpnGatewayRequest,
    ) -> EC2CreateVpnGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_vpn_gateway, request, EC2CreateVpnGatewayResponse)

    async def delete_application_status_check(
        self,
        request: EC2DeleteApplicationStatusCheckRequest,
    ) -> EC2DeleteApplicationStatusCheckResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_status_check, request, EC2DeleteApplicationStatusCheckResponse)

    async def delete_capacity_manager_data_export(
        self,
        request: EC2DeleteCapacityManagerDataExportRequest,
    ) -> EC2DeleteCapacityManagerDataExportResponse:
        client = self._require_client()
        return await self._execute(client.delete_capacity_manager_data_export, request, EC2DeleteCapacityManagerDataExportResponse)

    async def delete_carrier_gateway(
        self,
        request: EC2DeleteCarrierGatewayRequest,
    ) -> EC2DeleteCarrierGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_carrier_gateway, request, EC2DeleteCarrierGatewayResponse)

    async def delete_client_vpn_endpoint(
        self,
        request: EC2DeleteClientVpnEndpointRequest,
    ) -> EC2DeleteClientVpnEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_client_vpn_endpoint, request, EC2DeleteClientVpnEndpointResponse)

    async def delete_client_vpn_endpoint_authorization_policy(
        self,
        request: EC2DeleteClientVpnEndpointAuthorizationPolicyRequest,
    ) -> EC2DeleteClientVpnEndpointAuthorizationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_client_vpn_endpoint_authorization_policy, request, EC2DeleteClientVpnEndpointAuthorizationPolicyResponse)

    async def delete_client_vpn_route(
        self,
        request: EC2DeleteClientVpnRouteRequest,
    ) -> EC2DeleteClientVpnRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_client_vpn_route, request, EC2DeleteClientVpnRouteResponse)

    async def delete_coip_cidr(
        self,
        request: EC2DeleteCoipCidrRequest,
    ) -> EC2DeleteCoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.delete_coip_cidr, request, EC2DeleteCoipCidrResponse)

    async def delete_coip_pool(
        self,
        request: EC2DeleteCoipPoolRequest,
    ) -> EC2DeleteCoipPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_coip_pool, request, EC2DeleteCoipPoolResponse)

    async def delete_customer_gateway(
        self,
        request: EC2DeleteCustomerGatewayRequest,
    ) -> EC2DeleteCustomerGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_customer_gateway, request, EC2DeleteCustomerGatewayResponse)

    async def delete_dhcp_options(
        self,
        request: EC2DeleteDhcpOptionsRequest,
    ) -> EC2DeleteDhcpOptionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_dhcp_options, request, EC2DeleteDhcpOptionsResponse)

    async def delete_egress_only_internet_gateway(
        self,
        request: EC2DeleteEgressOnlyInternetGatewayRequest,
    ) -> EC2DeleteEgressOnlyInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_egress_only_internet_gateway, request, EC2DeleteEgressOnlyInternetGatewayResponse)

    async def delete_fleets(
        self,
        request: EC2DeleteFleetsRequest,
    ) -> EC2DeleteFleetsResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleets, request, EC2DeleteFleetsResponse)

    async def delete_flow_logs(
        self,
        request: EC2DeleteFlowLogsRequest,
    ) -> EC2DeleteFlowLogsResponse:
        client = self._require_client()
        return await self._execute(client.delete_flow_logs, request, EC2DeleteFlowLogsResponse)

    async def delete_fpga_image(
        self,
        request: EC2DeleteFpgaImageRequest,
    ) -> EC2DeleteFpgaImageResponse:
        client = self._require_client()
        return await self._execute(client.delete_fpga_image, request, EC2DeleteFpgaImageResponse)

    async def delete_image_usage_report(
        self,
        request: EC2DeleteImageUsageReportRequest,
    ) -> EC2DeleteImageUsageReportResponse:
        client = self._require_client()
        return await self._execute(client.delete_image_usage_report, request, EC2DeleteImageUsageReportResponse)

    async def delete_instance_connect_endpoint(
        self,
        request: EC2DeleteInstanceConnectEndpointRequest,
    ) -> EC2DeleteInstanceConnectEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance_connect_endpoint, request, EC2DeleteInstanceConnectEndpointResponse)

    async def delete_instance_event_window(
        self,
        request: EC2DeleteInstanceEventWindowRequest,
    ) -> EC2DeleteInstanceEventWindowResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance_event_window, request, EC2DeleteInstanceEventWindowResponse)

    async def delete_internet_gateway(
        self,
        request: EC2DeleteInternetGatewayRequest,
    ) -> EC2DeleteInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_internet_gateway, request, EC2DeleteInternetGatewayResponse)

    async def delete_ipam(
        self,
        request: EC2DeleteIpamRequest,
    ) -> EC2DeleteIpamResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam, request, EC2DeleteIpamResponse)

    async def delete_ipam_external_resource_verification_token(
        self,
        request: EC2DeleteIpamExternalResourceVerificationTokenRequest,
    ) -> EC2DeleteIpamExternalResourceVerificationTokenResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_external_resource_verification_token, request, EC2DeleteIpamExternalResourceVerificationTokenResponse)

    async def delete_ipam_internet_registry_association(
        self,
        request: EC2DeleteIpamInternetRegistryAssociationRequest,
    ) -> EC2DeleteIpamInternetRegistryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_internet_registry_association, request, EC2DeleteIpamInternetRegistryAssociationResponse)

    async def delete_ipam_policy(
        self,
        request: EC2DeleteIpamPolicyRequest,
    ) -> EC2DeleteIpamPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_policy, request, EC2DeleteIpamPolicyResponse)

    async def delete_ipam_pool(
        self,
        request: EC2DeleteIpamPoolRequest,
    ) -> EC2DeleteIpamPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_pool, request, EC2DeleteIpamPoolResponse)

    async def delete_ipam_prefix_list_resolver(
        self,
        request: EC2DeleteIpamPrefixListResolverRequest,
    ) -> EC2DeleteIpamPrefixListResolverResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_prefix_list_resolver, request, EC2DeleteIpamPrefixListResolverResponse)

    async def delete_ipam_prefix_list_resolver_target(
        self,
        request: EC2DeleteIpamPrefixListResolverTargetRequest,
    ) -> EC2DeleteIpamPrefixListResolverTargetResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_prefix_list_resolver_target, request, EC2DeleteIpamPrefixListResolverTargetResponse)

    async def delete_ipam_resource_discovery(
        self,
        request: EC2DeleteIpamResourceDiscoveryRequest,
    ) -> EC2DeleteIpamResourceDiscoveryResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_resource_discovery, request, EC2DeleteIpamResourceDiscoveryResponse)

    async def delete_ipam_routing_policy_registration(
        self,
        request: EC2DeleteIpamRoutingPolicyRegistrationRequest,
    ) -> EC2DeleteIpamRoutingPolicyRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_routing_policy_registration, request, EC2DeleteIpamRoutingPolicyRegistrationResponse)

    async def delete_ipam_scope(
        self,
        request: EC2DeleteIpamScopeRequest,
    ) -> EC2DeleteIpamScopeResponse:
        client = self._require_client()
        return await self._execute(client.delete_ipam_scope, request, EC2DeleteIpamScopeResponse)

    async def delete_key_pair(
        self,
        request: EC2DeleteKeyPairRequest | None = None,
    ) -> EC2DeleteKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.delete_key_pair, request, EC2DeleteKeyPairResponse)

    async def delete_launch_template(
        self,
        request: EC2DeleteLaunchTemplateRequest | None = None,
    ) -> EC2DeleteLaunchTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_launch_template, request, EC2DeleteLaunchTemplateResponse)

    async def delete_launch_template_versions(
        self,
        request: EC2DeleteLaunchTemplateVersionsRequest,
    ) -> EC2DeleteLaunchTemplateVersionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_launch_template_versions, request, EC2DeleteLaunchTemplateVersionsResponse)

    async def delete_local_gateway_route(
        self,
        request: EC2DeleteLocalGatewayRouteRequest,
    ) -> EC2DeleteLocalGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_route, request, EC2DeleteLocalGatewayRouteResponse)

    async def delete_local_gateway_route_table(
        self,
        request: EC2DeleteLocalGatewayRouteTableRequest,
    ) -> EC2DeleteLocalGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_route_table, request, EC2DeleteLocalGatewayRouteTableResponse)

    async def delete_local_gateway_route_table_virtual_interface_group_association(
        self,
        request: EC2DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
    ) -> EC2DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_route_table_virtual_interface_group_association, request, EC2DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse)

    async def delete_local_gateway_route_table_vpc_association(
        self,
        request: EC2DeleteLocalGatewayRouteTableVpcAssociationRequest,
    ) -> EC2DeleteLocalGatewayRouteTableVpcAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_route_table_vpc_association, request, EC2DeleteLocalGatewayRouteTableVpcAssociationResponse)

    async def delete_local_gateway_virtual_interface(
        self,
        request: EC2DeleteLocalGatewayVirtualInterfaceRequest,
    ) -> EC2DeleteLocalGatewayVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_virtual_interface, request, EC2DeleteLocalGatewayVirtualInterfaceResponse)

    async def delete_local_gateway_virtual_interface_group(
        self,
        request: EC2DeleteLocalGatewayVirtualInterfaceGroupRequest,
    ) -> EC2DeleteLocalGatewayVirtualInterfaceGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_local_gateway_virtual_interface_group, request, EC2DeleteLocalGatewayVirtualInterfaceGroupResponse)

    async def delete_managed_prefix_list(
        self,
        request: EC2DeleteManagedPrefixListRequest,
    ) -> EC2DeleteManagedPrefixListResponse:
        client = self._require_client()
        return await self._execute(client.delete_managed_prefix_list, request, EC2DeleteManagedPrefixListResponse)

    async def delete_metric_category(
        self,
        request: EC2DeleteMetricCategoryRequest,
    ) -> EC2DeleteMetricCategoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_category, request, EC2DeleteMetricCategoryResponse)

    async def delete_nat_gateway(
        self,
        request: EC2DeleteNatGatewayRequest,
    ) -> EC2DeleteNatGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_nat_gateway, request, EC2DeleteNatGatewayResponse)

    async def delete_network_acl(
        self,
        request: EC2DeleteNetworkAclRequest,
    ) -> EC2DeleteNetworkAclResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_acl, request, EC2DeleteNetworkAclResponse)

    async def delete_network_acl_entry(
        self,
        request: EC2DeleteNetworkAclEntryRequest,
    ) -> EC2DeleteNetworkAclEntryResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_acl_entry, request, EC2DeleteNetworkAclEntryResponse)

    async def delete_network_insights_access_scope(
        self,
        request: EC2DeleteNetworkInsightsAccessScopeRequest,
    ) -> EC2DeleteNetworkInsightsAccessScopeResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_insights_access_scope, request, EC2DeleteNetworkInsightsAccessScopeResponse)

    async def delete_network_insights_access_scope_analysis(
        self,
        request: EC2DeleteNetworkInsightsAccessScopeAnalysisRequest,
    ) -> EC2DeleteNetworkInsightsAccessScopeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_insights_access_scope_analysis, request, EC2DeleteNetworkInsightsAccessScopeAnalysisResponse)

    async def delete_network_insights_analysis(
        self,
        request: EC2DeleteNetworkInsightsAnalysisRequest,
    ) -> EC2DeleteNetworkInsightsAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_insights_analysis, request, EC2DeleteNetworkInsightsAnalysisResponse)

    async def delete_network_insights_path(
        self,
        request: EC2DeleteNetworkInsightsPathRequest,
    ) -> EC2DeleteNetworkInsightsPathResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_insights_path, request, EC2DeleteNetworkInsightsPathResponse)

    async def delete_network_interface(
        self,
        request: EC2DeleteNetworkInterfaceRequest,
    ) -> EC2DeleteNetworkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_interface, request, EC2DeleteNetworkInterfaceResponse)

    async def delete_network_interface_permission(
        self,
        request: EC2DeleteNetworkInterfacePermissionRequest,
    ) -> EC2DeleteNetworkInterfacePermissionResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_interface_permission, request, EC2DeleteNetworkInterfacePermissionResponse)

    async def delete_networking_flex_cost_allocation_policies(
        self,
        request: EC2DeleteNetworkingFlexCostAllocationPoliciesRequest,
    ) -> EC2DeleteNetworkingFlexCostAllocationPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.delete_networking_flex_cost_allocation_policies, request, EC2DeleteNetworkingFlexCostAllocationPoliciesResponse)

    async def delete_placement_group(
        self,
        request: EC2DeletePlacementGroupRequest,
    ) -> EC2DeletePlacementGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_placement_group, request, EC2DeletePlacementGroupResponse)

    async def delete_public_ipv4_pool(
        self,
        request: EC2DeletePublicIpv4PoolRequest,
    ) -> EC2DeletePublicIpv4PoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_public_ipv4_pool, request, EC2DeletePublicIpv4PoolResponse)

    async def delete_queued_reserved_instances(
        self,
        request: EC2DeleteQueuedReservedInstancesRequest,
    ) -> EC2DeleteQueuedReservedInstancesResponse:
        client = self._require_client()
        return await self._execute(client.delete_queued_reserved_instances, request, EC2DeleteQueuedReservedInstancesResponse)

    async def delete_route(
        self,
        request: EC2DeleteRouteRequest,
    ) -> EC2DeleteRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_route, request, EC2DeleteRouteResponse)

    async def delete_route_server(
        self,
        request: EC2DeleteRouteServerRequest,
    ) -> EC2DeleteRouteServerResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_server, request, EC2DeleteRouteServerResponse)

    async def delete_route_server_endpoint(
        self,
        request: EC2DeleteRouteServerEndpointRequest,
    ) -> EC2DeleteRouteServerEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_server_endpoint, request, EC2DeleteRouteServerEndpointResponse)

    async def delete_route_server_peer(
        self,
        request: EC2DeleteRouteServerPeerRequest,
    ) -> EC2DeleteRouteServerPeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_server_peer, request, EC2DeleteRouteServerPeerResponse)

    async def delete_route_table(
        self,
        request: EC2DeleteRouteTableRequest,
    ) -> EC2DeleteRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_table, request, EC2DeleteRouteTableResponse)

    async def delete_secondary_network(
        self,
        request: EC2DeleteSecondaryNetworkRequest,
    ) -> EC2DeleteSecondaryNetworkResponse:
        client = self._require_client()
        return await self._execute(client.delete_secondary_network, request, EC2DeleteSecondaryNetworkResponse)

    async def delete_secondary_subnet(
        self,
        request: EC2DeleteSecondarySubnetRequest,
    ) -> EC2DeleteSecondarySubnetResponse:
        client = self._require_client()
        return await self._execute(client.delete_secondary_subnet, request, EC2DeleteSecondarySubnetResponse)

    async def delete_spot_datafeed_subscription(
        self,
        request: EC2DeleteSpotDatafeedSubscriptionRequest | None = None,
    ) -> EC2DeleteSpotDatafeedSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_spot_datafeed_subscription, request, EC2DeleteSpotDatafeedSubscriptionResponse)

    async def delete_subnet(
        self,
        request: EC2DeleteSubnetRequest,
    ) -> EC2DeleteSubnetResponse:
        client = self._require_client()
        return await self._execute(client.delete_subnet, request, EC2DeleteSubnetResponse)

    async def delete_subnet_cidr_reservation(
        self,
        request: EC2DeleteSubnetCidrReservationRequest,
    ) -> EC2DeleteSubnetCidrReservationResponse:
        client = self._require_client()
        return await self._execute(client.delete_subnet_cidr_reservation, request, EC2DeleteSubnetCidrReservationResponse)

    async def delete_traffic_mirror_filter(
        self,
        request: EC2DeleteTrafficMirrorFilterRequest,
    ) -> EC2DeleteTrafficMirrorFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_mirror_filter, request, EC2DeleteTrafficMirrorFilterResponse)

    async def delete_traffic_mirror_filter_rule(
        self,
        request: EC2DeleteTrafficMirrorFilterRuleRequest,
    ) -> EC2DeleteTrafficMirrorFilterRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_mirror_filter_rule, request, EC2DeleteTrafficMirrorFilterRuleResponse)

    async def delete_traffic_mirror_session(
        self,
        request: EC2DeleteTrafficMirrorSessionRequest,
    ) -> EC2DeleteTrafficMirrorSessionResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_mirror_session, request, EC2DeleteTrafficMirrorSessionResponse)

    async def delete_traffic_mirror_target(
        self,
        request: EC2DeleteTrafficMirrorTargetRequest,
    ) -> EC2DeleteTrafficMirrorTargetResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_mirror_target, request, EC2DeleteTrafficMirrorTargetResponse)

    async def delete_transit_gateway(
        self,
        request: EC2DeleteTransitGatewayRequest,
    ) -> EC2DeleteTransitGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway, request, EC2DeleteTransitGatewayResponse)

    async def delete_transit_gateway_client_vpn_attachment(
        self,
        request: EC2DeleteTransitGatewayClientVpnAttachmentRequest,
    ) -> EC2DeleteTransitGatewayClientVpnAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_client_vpn_attachment, request, EC2DeleteTransitGatewayClientVpnAttachmentResponse)

    async def delete_transit_gateway_connect(
        self,
        request: EC2DeleteTransitGatewayConnectRequest,
    ) -> EC2DeleteTransitGatewayConnectResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_connect, request, EC2DeleteTransitGatewayConnectResponse)

    async def delete_transit_gateway_connect_peer(
        self,
        request: EC2DeleteTransitGatewayConnectPeerRequest,
    ) -> EC2DeleteTransitGatewayConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_connect_peer, request, EC2DeleteTransitGatewayConnectPeerResponse)

    async def delete_transit_gateway_metering_policy(
        self,
        request: EC2DeleteTransitGatewayMeteringPolicyRequest,
    ) -> EC2DeleteTransitGatewayMeteringPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_metering_policy, request, EC2DeleteTransitGatewayMeteringPolicyResponse)

    async def delete_transit_gateway_metering_policy_entry(
        self,
        request: EC2DeleteTransitGatewayMeteringPolicyEntryRequest,
    ) -> EC2DeleteTransitGatewayMeteringPolicyEntryResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_metering_policy_entry, request, EC2DeleteTransitGatewayMeteringPolicyEntryResponse)

    async def delete_transit_gateway_multicast_domain(
        self,
        request: EC2DeleteTransitGatewayMulticastDomainRequest,
    ) -> EC2DeleteTransitGatewayMulticastDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_multicast_domain, request, EC2DeleteTransitGatewayMulticastDomainResponse)

    async def delete_transit_gateway_network_function_attachment(
        self,
        request: EC2DeleteTransitGatewayNetworkFunctionAttachmentRequest,
    ) -> EC2DeleteTransitGatewayNetworkFunctionAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_network_function_attachment, request, EC2DeleteTransitGatewayNetworkFunctionAttachmentResponse)

    async def delete_transit_gateway_peering_attachment(
        self,
        request: EC2DeleteTransitGatewayPeeringAttachmentRequest,
    ) -> EC2DeleteTransitGatewayPeeringAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_peering_attachment, request, EC2DeleteTransitGatewayPeeringAttachmentResponse)

    async def delete_transit_gateway_policy_table(
        self,
        request: EC2DeleteTransitGatewayPolicyTableRequest,
    ) -> EC2DeleteTransitGatewayPolicyTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_policy_table, request, EC2DeleteTransitGatewayPolicyTableResponse)

    async def delete_transit_gateway_policy_table_entry(
        self,
        request: EC2DeleteTransitGatewayPolicyTableEntryRequest,
    ) -> EC2DeleteTransitGatewayPolicyTableEntryResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_policy_table_entry, request, EC2DeleteTransitGatewayPolicyTableEntryResponse)

    async def delete_transit_gateway_prefix_list_reference(
        self,
        request: EC2DeleteTransitGatewayPrefixListReferenceRequest,
    ) -> EC2DeleteTransitGatewayPrefixListReferenceResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_prefix_list_reference, request, EC2DeleteTransitGatewayPrefixListReferenceResponse)

    async def delete_transit_gateway_route(
        self,
        request: EC2DeleteTransitGatewayRouteRequest,
    ) -> EC2DeleteTransitGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_route, request, EC2DeleteTransitGatewayRouteResponse)

    async def delete_transit_gateway_route_table(
        self,
        request: EC2DeleteTransitGatewayRouteTableRequest,
    ) -> EC2DeleteTransitGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_route_table, request, EC2DeleteTransitGatewayRouteTableResponse)

    async def delete_transit_gateway_route_table_announcement(
        self,
        request: EC2DeleteTransitGatewayRouteTableAnnouncementRequest,
    ) -> EC2DeleteTransitGatewayRouteTableAnnouncementResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_route_table_announcement, request, EC2DeleteTransitGatewayRouteTableAnnouncementResponse)

    async def delete_transit_gateway_vpc_attachment(
        self,
        request: EC2DeleteTransitGatewayVpcAttachmentRequest,
    ) -> EC2DeleteTransitGatewayVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_transit_gateway_vpc_attachment, request, EC2DeleteTransitGatewayVpcAttachmentResponse)

    async def delete_verified_access_endpoint(
        self,
        request: EC2DeleteVerifiedAccessEndpointRequest,
    ) -> EC2DeleteVerifiedAccessEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_verified_access_endpoint, request, EC2DeleteVerifiedAccessEndpointResponse)

    async def delete_verified_access_group(
        self,
        request: EC2DeleteVerifiedAccessGroupRequest,
    ) -> EC2DeleteVerifiedAccessGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_verified_access_group, request, EC2DeleteVerifiedAccessGroupResponse)

    async def delete_verified_access_instance(
        self,
        request: EC2DeleteVerifiedAccessInstanceRequest,
    ) -> EC2DeleteVerifiedAccessInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_verified_access_instance, request, EC2DeleteVerifiedAccessInstanceResponse)

    async def delete_verified_access_trust_provider(
        self,
        request: EC2DeleteVerifiedAccessTrustProviderRequest,
    ) -> EC2DeleteVerifiedAccessTrustProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_verified_access_trust_provider, request, EC2DeleteVerifiedAccessTrustProviderResponse)

    async def delete_vpc(
        self,
        request: EC2DeleteVpcRequest,
    ) -> EC2DeleteVpcResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc, request, EC2DeleteVpcResponse)

    async def delete_vpc_block_public_access_exclusion(
        self,
        request: EC2DeleteVpcBlockPublicAccessExclusionRequest,
    ) -> EC2DeleteVpcBlockPublicAccessExclusionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_block_public_access_exclusion, request, EC2DeleteVpcBlockPublicAccessExclusionResponse)

    async def delete_vpc_encryption_control(
        self,
        request: EC2DeleteVpcEncryptionControlRequest,
    ) -> EC2DeleteVpcEncryptionControlResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_encryption_control, request, EC2DeleteVpcEncryptionControlResponse)

    async def delete_vpc_endpoint_connection_notifications(
        self,
        request: EC2DeleteVpcEndpointConnectionNotificationsRequest,
    ) -> EC2DeleteVpcEndpointConnectionNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_endpoint_connection_notifications, request, EC2DeleteVpcEndpointConnectionNotificationsResponse)

    async def delete_vpc_endpoint_service_configurations(
        self,
        request: EC2DeleteVpcEndpointServiceConfigurationsRequest,
    ) -> EC2DeleteVpcEndpointServiceConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_endpoint_service_configurations, request, EC2DeleteVpcEndpointServiceConfigurationsResponse)

    async def delete_vpc_endpoints(
        self,
        request: EC2DeleteVpcEndpointsRequest,
    ) -> EC2DeleteVpcEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_endpoints, request, EC2DeleteVpcEndpointsResponse)

    async def delete_vpc_peering_connection(
        self,
        request: EC2DeleteVpcPeeringConnectionRequest,
    ) -> EC2DeleteVpcPeeringConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_peering_connection, request, EC2DeleteVpcPeeringConnectionResponse)

    async def delete_vpn_concentrator(
        self,
        request: EC2DeleteVpnConcentratorRequest,
    ) -> EC2DeleteVpnConcentratorResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpn_concentrator, request, EC2DeleteVpnConcentratorResponse)

    async def delete_vpn_connection(
        self,
        request: EC2DeleteVpnConnectionRequest,
    ) -> EC2DeleteVpnConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpn_connection, request, EC2DeleteVpnConnectionResponse)

    async def delete_vpn_connection_route(
        self,
        request: EC2DeleteVpnConnectionRouteRequest,
    ) -> EC2DeleteVpnConnectionRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpn_connection_route, request, EC2DeleteVpnConnectionRouteResponse)

    async def delete_vpn_gateway(
        self,
        request: EC2DeleteVpnGatewayRequest,
    ) -> EC2DeleteVpnGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpn_gateway, request, EC2DeleteVpnGatewayResponse)

    async def deprovision_byoip_cidr(
        self,
        request: EC2DeprovisionByoipCidrRequest,
    ) -> EC2DeprovisionByoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.deprovision_byoip_cidr, request, EC2DeprovisionByoipCidrResponse)

    async def deprovision_ipam_byoasn(
        self,
        request: EC2DeprovisionIpamByoasnRequest,
    ) -> EC2DeprovisionIpamByoasnResponse:
        client = self._require_client()
        return await self._execute(client.deprovision_ipam_byoasn, request, EC2DeprovisionIpamByoasnResponse)

    async def deprovision_ipam_pool_cidr(
        self,
        request: EC2DeprovisionIpamPoolCidrRequest,
    ) -> EC2DeprovisionIpamPoolCidrResponse:
        client = self._require_client()
        return await self._execute(client.deprovision_ipam_pool_cidr, request, EC2DeprovisionIpamPoolCidrResponse)

    async def deprovision_public_ipv4_pool_cidr(
        self,
        request: EC2DeprovisionPublicIpv4PoolCidrRequest,
    ) -> EC2DeprovisionPublicIpv4PoolCidrResponse:
        client = self._require_client()
        return await self._execute(client.deprovision_public_ipv4_pool_cidr, request, EC2DeprovisionPublicIpv4PoolCidrResponse)

    async def deregister_image(
        self,
        request: EC2DeregisterImageRequest,
    ) -> EC2DeregisterImageResponse:
        client = self._require_client()
        return await self._execute(client.deregister_image, request, EC2DeregisterImageResponse)

    async def deregister_instance_event_notification_attributes(
        self,
        request: EC2DeregisterInstanceEventNotificationAttributesRequest,
    ) -> EC2DeregisterInstanceEventNotificationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.deregister_instance_event_notification_attributes, request, EC2DeregisterInstanceEventNotificationAttributesResponse)

    async def deregister_transit_gateway_multicast_group_members(
        self,
        request: EC2DeregisterTransitGatewayMulticastGroupMembersRequest | None = None,
    ) -> EC2DeregisterTransitGatewayMulticastGroupMembersResponse:
        client = self._require_client()
        return await self._execute(client.deregister_transit_gateway_multicast_group_members, request, EC2DeregisterTransitGatewayMulticastGroupMembersResponse)

    async def deregister_transit_gateway_multicast_group_sources(
        self,
        request: EC2DeregisterTransitGatewayMulticastGroupSourcesRequest | None = None,
    ) -> EC2DeregisterTransitGatewayMulticastGroupSourcesResponse:
        client = self._require_client()
        return await self._execute(client.deregister_transit_gateway_multicast_group_sources, request, EC2DeregisterTransitGatewayMulticastGroupSourcesResponse)

    async def describe_account_attributes(
        self,
        request: EC2DescribeAccountAttributesRequest | None = None,
    ) -> EC2DescribeAccountAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_attributes, request, EC2DescribeAccountAttributesResponse)

    async def describe_account_vpc_encryption_control(
        self,
        request: EC2DescribeAccountVpcEncryptionControlRequest | None = None,
    ) -> EC2DescribeAccountVpcEncryptionControlResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_vpc_encryption_control, request, EC2DescribeAccountVpcEncryptionControlResponse)

    async def describe_address_transfers(
        self,
        request: EC2DescribeAddressTransfersRequest | None = None,
    ) -> EC2DescribeAddressTransfersResponse:
        client = self._require_client()
        return await self._execute(client.describe_address_transfers, request, EC2DescribeAddressTransfersResponse)

    async def describe_address_transfers_paginated(
        self,
        request: EC2DescribeAddressTransfersRequest | None = None,
    ) -> list[EC2DescribeAddressTransfersResponse]:
        return await self._paginate('describe_address_transfers', request, EC2DescribeAddressTransfersResponse)

    async def describe_addresses(
        self,
        request: EC2DescribeAddressesRequest | None = None,
    ) -> EC2DescribeAddressesResponse:
        client = self._require_client()
        return await self._execute(client.describe_addresses, request, EC2DescribeAddressesResponse)

    async def describe_addresses_attribute(
        self,
        request: EC2DescribeAddressesAttributeRequest | None = None,
    ) -> EC2DescribeAddressesAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_addresses_attribute, request, EC2DescribeAddressesAttributeResponse)

    async def describe_addresses_attribute_paginated(
        self,
        request: EC2DescribeAddressesAttributeRequest | None = None,
    ) -> list[EC2DescribeAddressesAttributeResponse]:
        return await self._paginate('describe_addresses_attribute', request, EC2DescribeAddressesAttributeResponse)

    async def describe_aggregate_id_format(
        self,
        request: EC2DescribeAggregateIdFormatRequest | None = None,
    ) -> EC2DescribeAggregateIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.describe_aggregate_id_format, request, EC2DescribeAggregateIdFormatResponse)

    async def describe_application_status(
        self,
        request: EC2DescribeApplicationStatusRequest | None = None,
    ) -> EC2DescribeApplicationStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_status, request, EC2DescribeApplicationStatusResponse)

    async def describe_application_status_check_associations(
        self,
        request: EC2DescribeApplicationStatusCheckAssociationsRequest | None = None,
    ) -> EC2DescribeApplicationStatusCheckAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_status_check_associations, request, EC2DescribeApplicationStatusCheckAssociationsResponse)

    async def describe_application_status_checks(
        self,
        request: EC2DescribeApplicationStatusChecksRequest | None = None,
    ) -> EC2DescribeApplicationStatusChecksResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_status_checks, request, EC2DescribeApplicationStatusChecksResponse)

    async def describe_availability_zones(
        self,
        request: EC2DescribeAvailabilityZonesRequest | None = None,
    ) -> EC2DescribeAvailabilityZonesResponse:
        client = self._require_client()
        return await self._execute(client.describe_availability_zones, request, EC2DescribeAvailabilityZonesResponse)

    async def describe_aws_network_performance_metric_subscriptions(
        self,
        request: EC2DescribeAwsNetworkPerformanceMetricSubscriptionsRequest | None = None,
    ) -> EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_aws_network_performance_metric_subscriptions, request, EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse)

    async def describe_aws_network_performance_metric_subscriptions_paginated(
        self,
        request: EC2DescribeAwsNetworkPerformanceMetricSubscriptionsRequest | None = None,
    ) -> list[EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse]:
        return await self._paginate('describe_aws_network_performance_metric_subscriptions', request, EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse)

    async def describe_bundle_tasks(
        self,
        request: EC2DescribeBundleTasksRequest | None = None,
    ) -> EC2DescribeBundleTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_bundle_tasks, request, EC2DescribeBundleTasksResponse)

    async def describe_byoip_cidrs(
        self,
        request: EC2DescribeByoipCidrsRequest,
    ) -> EC2DescribeByoipCidrsResponse:
        client = self._require_client()
        return await self._execute(client.describe_byoip_cidrs, request, EC2DescribeByoipCidrsResponse)

    async def describe_byoip_cidrs_paginated(
        self,
        request: EC2DescribeByoipCidrsRequest,
    ) -> list[EC2DescribeByoipCidrsResponse]:
        return await self._paginate('describe_byoip_cidrs', request, EC2DescribeByoipCidrsResponse)

    async def describe_capacity_block_extension_history(
        self,
        request: EC2DescribeCapacityBlockExtensionHistoryRequest | None = None,
    ) -> EC2DescribeCapacityBlockExtensionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_block_extension_history, request, EC2DescribeCapacityBlockExtensionHistoryResponse)

    async def describe_capacity_block_extension_history_paginated(
        self,
        request: EC2DescribeCapacityBlockExtensionHistoryRequest | None = None,
    ) -> list[EC2DescribeCapacityBlockExtensionHistoryResponse]:
        return await self._paginate('describe_capacity_block_extension_history', request, EC2DescribeCapacityBlockExtensionHistoryResponse)

    async def describe_capacity_block_extension_offerings(
        self,
        request: EC2DescribeCapacityBlockExtensionOfferingsRequest,
    ) -> EC2DescribeCapacityBlockExtensionOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_block_extension_offerings, request, EC2DescribeCapacityBlockExtensionOfferingsResponse)

    async def describe_capacity_block_extension_offerings_paginated(
        self,
        request: EC2DescribeCapacityBlockExtensionOfferingsRequest,
    ) -> list[EC2DescribeCapacityBlockExtensionOfferingsResponse]:
        return await self._paginate('describe_capacity_block_extension_offerings', request, EC2DescribeCapacityBlockExtensionOfferingsResponse)

    async def describe_capacity_block_offerings(
        self,
        request: EC2DescribeCapacityBlockOfferingsRequest,
    ) -> EC2DescribeCapacityBlockOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_block_offerings, request, EC2DescribeCapacityBlockOfferingsResponse)

    async def describe_capacity_block_offerings_paginated(
        self,
        request: EC2DescribeCapacityBlockOfferingsRequest,
    ) -> list[EC2DescribeCapacityBlockOfferingsResponse]:
        return await self._paginate('describe_capacity_block_offerings', request, EC2DescribeCapacityBlockOfferingsResponse)

    async def describe_capacity_block_status(
        self,
        request: EC2DescribeCapacityBlockStatusRequest | None = None,
    ) -> EC2DescribeCapacityBlockStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_block_status, request, EC2DescribeCapacityBlockStatusResponse)

    async def describe_capacity_block_status_paginated(
        self,
        request: EC2DescribeCapacityBlockStatusRequest | None = None,
    ) -> list[EC2DescribeCapacityBlockStatusResponse]:
        return await self._paginate('describe_capacity_block_status', request, EC2DescribeCapacityBlockStatusResponse)

    async def describe_capacity_blocks(
        self,
        request: EC2DescribeCapacityBlocksRequest | None = None,
    ) -> EC2DescribeCapacityBlocksResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_blocks, request, EC2DescribeCapacityBlocksResponse)

    async def describe_capacity_blocks_paginated(
        self,
        request: EC2DescribeCapacityBlocksRequest | None = None,
    ) -> list[EC2DescribeCapacityBlocksResponse]:
        return await self._paginate('describe_capacity_blocks', request, EC2DescribeCapacityBlocksResponse)

    async def describe_capacity_manager_data_exports(
        self,
        request: EC2DescribeCapacityManagerDataExportsRequest | None = None,
    ) -> EC2DescribeCapacityManagerDataExportsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_manager_data_exports, request, EC2DescribeCapacityManagerDataExportsResponse)

    async def describe_capacity_manager_data_exports_paginated(
        self,
        request: EC2DescribeCapacityManagerDataExportsRequest | None = None,
    ) -> list[EC2DescribeCapacityManagerDataExportsResponse]:
        return await self._paginate('describe_capacity_manager_data_exports', request, EC2DescribeCapacityManagerDataExportsResponse)

    async def describe_capacity_reservation_billing_requests(
        self,
        request: EC2DescribeCapacityReservationBillingRequestsRequest,
    ) -> EC2DescribeCapacityReservationBillingRequestsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation_billing_requests, request, EC2DescribeCapacityReservationBillingRequestsResponse)

    async def describe_capacity_reservation_billing_requests_paginated(
        self,
        request: EC2DescribeCapacityReservationBillingRequestsRequest,
    ) -> list[EC2DescribeCapacityReservationBillingRequestsResponse]:
        return await self._paginate('describe_capacity_reservation_billing_requests', request, EC2DescribeCapacityReservationBillingRequestsResponse)

    async def describe_capacity_reservation_cancellation_quotes(
        self,
        request: EC2DescribeCapacityReservationCancellationQuotesRequest | None = None,
    ) -> EC2DescribeCapacityReservationCancellationQuotesResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation_cancellation_quotes, request, EC2DescribeCapacityReservationCancellationQuotesResponse)

    async def describe_capacity_reservation_date_change_quotes(
        self,
        request: EC2DescribeCapacityReservationDateChangeQuotesRequest | None = None,
    ) -> EC2DescribeCapacityReservationDateChangeQuotesResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation_date_change_quotes, request, EC2DescribeCapacityReservationDateChangeQuotesResponse)

    async def describe_capacity_reservation_date_change_quotes_paginated(
        self,
        request: EC2DescribeCapacityReservationDateChangeQuotesRequest | None = None,
    ) -> list[EC2DescribeCapacityReservationDateChangeQuotesResponse]:
        return await self._paginate('describe_capacity_reservation_date_change_quotes', request, EC2DescribeCapacityReservationDateChangeQuotesResponse)

    async def describe_capacity_reservation_fleets(
        self,
        request: EC2DescribeCapacityReservationFleetsRequest | None = None,
    ) -> EC2DescribeCapacityReservationFleetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation_fleets, request, EC2DescribeCapacityReservationFleetsResponse)

    async def describe_capacity_reservation_fleets_paginated(
        self,
        request: EC2DescribeCapacityReservationFleetsRequest | None = None,
    ) -> list[EC2DescribeCapacityReservationFleetsResponse]:
        return await self._paginate('describe_capacity_reservation_fleets', request, EC2DescribeCapacityReservationFleetsResponse)

    async def describe_capacity_reservation_topology(
        self,
        request: EC2DescribeCapacityReservationTopologyRequest | None = None,
    ) -> EC2DescribeCapacityReservationTopologyResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation_topology, request, EC2DescribeCapacityReservationTopologyResponse)

    async def describe_capacity_reservations(
        self,
        request: EC2DescribeCapacityReservationsRequest | None = None,
    ) -> EC2DescribeCapacityReservationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservations, request, EC2DescribeCapacityReservationsResponse)

    async def describe_capacity_reservations_paginated(
        self,
        request: EC2DescribeCapacityReservationsRequest | None = None,
    ) -> list[EC2DescribeCapacityReservationsResponse]:
        return await self._paginate('describe_capacity_reservations', request, EC2DescribeCapacityReservationsResponse)

    async def describe_carrier_gateways(
        self,
        request: EC2DescribeCarrierGatewaysRequest | None = None,
    ) -> EC2DescribeCarrierGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_carrier_gateways, request, EC2DescribeCarrierGatewaysResponse)

    async def describe_carrier_gateways_paginated(
        self,
        request: EC2DescribeCarrierGatewaysRequest | None = None,
    ) -> list[EC2DescribeCarrierGatewaysResponse]:
        return await self._paginate('describe_carrier_gateways', request, EC2DescribeCarrierGatewaysResponse)

    async def describe_classic_link_instances(
        self,
        request: EC2DescribeClassicLinkInstancesRequest | None = None,
    ) -> EC2DescribeClassicLinkInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_classic_link_instances, request, EC2DescribeClassicLinkInstancesResponse)

    async def describe_classic_link_instances_paginated(
        self,
        request: EC2DescribeClassicLinkInstancesRequest | None = None,
    ) -> list[EC2DescribeClassicLinkInstancesResponse]:
        return await self._paginate('describe_classic_link_instances', request, EC2DescribeClassicLinkInstancesResponse)

    async def describe_client_vpn_authorization_rules(
        self,
        request: EC2DescribeClientVpnAuthorizationRulesRequest,
    ) -> EC2DescribeClientVpnAuthorizationRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_vpn_authorization_rules, request, EC2DescribeClientVpnAuthorizationRulesResponse)

    async def describe_client_vpn_authorization_rules_paginated(
        self,
        request: EC2DescribeClientVpnAuthorizationRulesRequest,
    ) -> list[EC2DescribeClientVpnAuthorizationRulesResponse]:
        return await self._paginate('describe_client_vpn_authorization_rules', request, EC2DescribeClientVpnAuthorizationRulesResponse)

    async def describe_client_vpn_connections(
        self,
        request: EC2DescribeClientVpnConnectionsRequest,
    ) -> EC2DescribeClientVpnConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_vpn_connections, request, EC2DescribeClientVpnConnectionsResponse)

    async def describe_client_vpn_connections_paginated(
        self,
        request: EC2DescribeClientVpnConnectionsRequest,
    ) -> list[EC2DescribeClientVpnConnectionsResponse]:
        return await self._paginate('describe_client_vpn_connections', request, EC2DescribeClientVpnConnectionsResponse)

    async def describe_client_vpn_endpoints(
        self,
        request: EC2DescribeClientVpnEndpointsRequest | None = None,
    ) -> EC2DescribeClientVpnEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_vpn_endpoints, request, EC2DescribeClientVpnEndpointsResponse)

    async def describe_client_vpn_endpoints_paginated(
        self,
        request: EC2DescribeClientVpnEndpointsRequest | None = None,
    ) -> list[EC2DescribeClientVpnEndpointsResponse]:
        return await self._paginate('describe_client_vpn_endpoints', request, EC2DescribeClientVpnEndpointsResponse)

    async def describe_client_vpn_routes(
        self,
        request: EC2DescribeClientVpnRoutesRequest,
    ) -> EC2DescribeClientVpnRoutesResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_vpn_routes, request, EC2DescribeClientVpnRoutesResponse)

    async def describe_client_vpn_routes_paginated(
        self,
        request: EC2DescribeClientVpnRoutesRequest,
    ) -> list[EC2DescribeClientVpnRoutesResponse]:
        return await self._paginate('describe_client_vpn_routes', request, EC2DescribeClientVpnRoutesResponse)

    async def describe_client_vpn_target_networks(
        self,
        request: EC2DescribeClientVpnTargetNetworksRequest,
    ) -> EC2DescribeClientVpnTargetNetworksResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_vpn_target_networks, request, EC2DescribeClientVpnTargetNetworksResponse)

    async def describe_client_vpn_target_networks_paginated(
        self,
        request: EC2DescribeClientVpnTargetNetworksRequest,
    ) -> list[EC2DescribeClientVpnTargetNetworksResponse]:
        return await self._paginate('describe_client_vpn_target_networks', request, EC2DescribeClientVpnTargetNetworksResponse)

    async def describe_coip_pools(
        self,
        request: EC2DescribeCoipPoolsRequest | None = None,
    ) -> EC2DescribeCoipPoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_coip_pools, request, EC2DescribeCoipPoolsResponse)

    async def describe_coip_pools_paginated(
        self,
        request: EC2DescribeCoipPoolsRequest | None = None,
    ) -> list[EC2DescribeCoipPoolsResponse]:
        return await self._paginate('describe_coip_pools', request, EC2DescribeCoipPoolsResponse)

    async def describe_conversion_tasks(
        self,
        request: EC2DescribeConversionTasksRequest | None = None,
    ) -> EC2DescribeConversionTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_conversion_tasks, request, EC2DescribeConversionTasksResponse)

    async def describe_customer_gateways(
        self,
        request: EC2DescribeCustomerGatewaysRequest | None = None,
    ) -> EC2DescribeCustomerGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_customer_gateways, request, EC2DescribeCustomerGatewaysResponse)

    async def describe_declarative_policies_reports(
        self,
        request: EC2DescribeDeclarativePoliciesReportsRequest | None = None,
    ) -> EC2DescribeDeclarativePoliciesReportsResponse:
        client = self._require_client()
        return await self._execute(client.describe_declarative_policies_reports, request, EC2DescribeDeclarativePoliciesReportsResponse)

    async def describe_dhcp_options(
        self,
        request: EC2DescribeDhcpOptionsRequest | None = None,
    ) -> EC2DescribeDhcpOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_dhcp_options, request, EC2DescribeDhcpOptionsResponse)

    async def describe_dhcp_options_paginated(
        self,
        request: EC2DescribeDhcpOptionsRequest | None = None,
    ) -> list[EC2DescribeDhcpOptionsResponse]:
        return await self._paginate('describe_dhcp_options', request, EC2DescribeDhcpOptionsResponse)

    async def describe_egress_only_internet_gateways(
        self,
        request: EC2DescribeEgressOnlyInternetGatewaysRequest | None = None,
    ) -> EC2DescribeEgressOnlyInternetGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_egress_only_internet_gateways, request, EC2DescribeEgressOnlyInternetGatewaysResponse)

    async def describe_egress_only_internet_gateways_paginated(
        self,
        request: EC2DescribeEgressOnlyInternetGatewaysRequest | None = None,
    ) -> list[EC2DescribeEgressOnlyInternetGatewaysResponse]:
        return await self._paginate('describe_egress_only_internet_gateways', request, EC2DescribeEgressOnlyInternetGatewaysResponse)

    async def describe_elastic_gpus(
        self,
        request: EC2DescribeElasticGpusRequest | None = None,
    ) -> EC2DescribeElasticGpusResponse:
        client = self._require_client()
        return await self._execute(client.describe_elastic_gpus, request, EC2DescribeElasticGpusResponse)

    async def describe_export_image_tasks(
        self,
        request: EC2DescribeExportImageTasksRequest | None = None,
    ) -> EC2DescribeExportImageTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_export_image_tasks, request, EC2DescribeExportImageTasksResponse)

    async def describe_export_image_tasks_paginated(
        self,
        request: EC2DescribeExportImageTasksRequest | None = None,
    ) -> list[EC2DescribeExportImageTasksResponse]:
        return await self._paginate('describe_export_image_tasks', request, EC2DescribeExportImageTasksResponse)

    async def describe_export_tasks(
        self,
        request: EC2DescribeExportTasksRequest | None = None,
    ) -> EC2DescribeExportTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_export_tasks, request, EC2DescribeExportTasksResponse)

    async def describe_fast_launch_images(
        self,
        request: EC2DescribeFastLaunchImagesRequest | None = None,
    ) -> EC2DescribeFastLaunchImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_fast_launch_images, request, EC2DescribeFastLaunchImagesResponse)

    async def describe_fast_launch_images_paginated(
        self,
        request: EC2DescribeFastLaunchImagesRequest | None = None,
    ) -> list[EC2DescribeFastLaunchImagesResponse]:
        return await self._paginate('describe_fast_launch_images', request, EC2DescribeFastLaunchImagesResponse)

    async def describe_fast_snapshot_restores(
        self,
        request: EC2DescribeFastSnapshotRestoresRequest | None = None,
    ) -> EC2DescribeFastSnapshotRestoresResponse:
        client = self._require_client()
        return await self._execute(client.describe_fast_snapshot_restores, request, EC2DescribeFastSnapshotRestoresResponse)

    async def describe_fast_snapshot_restores_paginated(
        self,
        request: EC2DescribeFastSnapshotRestoresRequest | None = None,
    ) -> list[EC2DescribeFastSnapshotRestoresResponse]:
        return await self._paginate('describe_fast_snapshot_restores', request, EC2DescribeFastSnapshotRestoresResponse)

    async def describe_fleet_history(
        self,
        request: EC2DescribeFleetHistoryRequest,
    ) -> EC2DescribeFleetHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_history, request, EC2DescribeFleetHistoryResponse)

    async def describe_fleet_instances(
        self,
        request: EC2DescribeFleetInstancesRequest,
    ) -> EC2DescribeFleetInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_instances, request, EC2DescribeFleetInstancesResponse)

    async def describe_fleets(
        self,
        request: EC2DescribeFleetsRequest | None = None,
    ) -> EC2DescribeFleetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleets, request, EC2DescribeFleetsResponse)

    async def describe_fleets_paginated(
        self,
        request: EC2DescribeFleetsRequest | None = None,
    ) -> list[EC2DescribeFleetsResponse]:
        return await self._paginate('describe_fleets', request, EC2DescribeFleetsResponse)

    async def describe_flow_logs(
        self,
        request: EC2DescribeFlowLogsRequest | None = None,
    ) -> EC2DescribeFlowLogsResponse:
        client = self._require_client()
        return await self._execute(client.describe_flow_logs, request, EC2DescribeFlowLogsResponse)

    async def describe_flow_logs_paginated(
        self,
        request: EC2DescribeFlowLogsRequest | None = None,
    ) -> list[EC2DescribeFlowLogsResponse]:
        return await self._paginate('describe_flow_logs', request, EC2DescribeFlowLogsResponse)

    async def describe_fpga_image_attribute(
        self,
        request: EC2DescribeFpgaImageAttributeRequest,
    ) -> EC2DescribeFpgaImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_fpga_image_attribute, request, EC2DescribeFpgaImageAttributeResponse)

    async def describe_fpga_images(
        self,
        request: EC2DescribeFpgaImagesRequest | None = None,
    ) -> EC2DescribeFpgaImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_fpga_images, request, EC2DescribeFpgaImagesResponse)

    async def describe_fpga_images_paginated(
        self,
        request: EC2DescribeFpgaImagesRequest | None = None,
    ) -> list[EC2DescribeFpgaImagesResponse]:
        return await self._paginate('describe_fpga_images', request, EC2DescribeFpgaImagesResponse)

    async def describe_host_reservation_offerings(
        self,
        request: EC2DescribeHostReservationOfferingsRequest | None = None,
    ) -> EC2DescribeHostReservationOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_host_reservation_offerings, request, EC2DescribeHostReservationOfferingsResponse)

    async def describe_host_reservation_offerings_paginated(
        self,
        request: EC2DescribeHostReservationOfferingsRequest | None = None,
    ) -> list[EC2DescribeHostReservationOfferingsResponse]:
        return await self._paginate('describe_host_reservation_offerings', request, EC2DescribeHostReservationOfferingsResponse)

    async def describe_host_reservations(
        self,
        request: EC2DescribeHostReservationsRequest | None = None,
    ) -> EC2DescribeHostReservationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_host_reservations, request, EC2DescribeHostReservationsResponse)

    async def describe_host_reservations_paginated(
        self,
        request: EC2DescribeHostReservationsRequest | None = None,
    ) -> list[EC2DescribeHostReservationsResponse]:
        return await self._paginate('describe_host_reservations', request, EC2DescribeHostReservationsResponse)

    async def describe_hosts(
        self,
        request: EC2DescribeHostsRequest | None = None,
    ) -> EC2DescribeHostsResponse:
        client = self._require_client()
        return await self._execute(client.describe_hosts, request, EC2DescribeHostsResponse)

    async def describe_hosts_paginated(
        self,
        request: EC2DescribeHostsRequest | None = None,
    ) -> list[EC2DescribeHostsResponse]:
        return await self._paginate('describe_hosts', request, EC2DescribeHostsResponse)

    async def describe_iam_instance_profile_associations(
        self,
        request: EC2DescribeIamInstanceProfileAssociationsRequest | None = None,
    ) -> EC2DescribeIamInstanceProfileAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_iam_instance_profile_associations, request, EC2DescribeIamInstanceProfileAssociationsResponse)

    async def describe_iam_instance_profile_associations_paginated(
        self,
        request: EC2DescribeIamInstanceProfileAssociationsRequest | None = None,
    ) -> list[EC2DescribeIamInstanceProfileAssociationsResponse]:
        return await self._paginate('describe_iam_instance_profile_associations', request, EC2DescribeIamInstanceProfileAssociationsResponse)

    async def describe_id_format(
        self,
        request: EC2DescribeIdFormatRequest | None = None,
    ) -> EC2DescribeIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.describe_id_format, request, EC2DescribeIdFormatResponse)

    async def describe_identity_id_format(
        self,
        request: EC2DescribeIdentityIdFormatRequest,
    ) -> EC2DescribeIdentityIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_id_format, request, EC2DescribeIdentityIdFormatResponse)

    async def describe_image_attribute(
        self,
        request: EC2DescribeImageAttributeRequest,
    ) -> EC2DescribeImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_attribute, request, EC2DescribeImageAttributeResponse)

    async def describe_image_references(
        self,
        request: EC2DescribeImageReferencesRequest,
    ) -> EC2DescribeImageReferencesResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_references, request, EC2DescribeImageReferencesResponse)

    async def describe_image_references_paginated(
        self,
        request: EC2DescribeImageReferencesRequest,
    ) -> list[EC2DescribeImageReferencesResponse]:
        return await self._paginate('describe_image_references', request, EC2DescribeImageReferencesResponse)

    async def describe_image_usage_report_entries(
        self,
        request: EC2DescribeImageUsageReportEntriesRequest | None = None,
    ) -> EC2DescribeImageUsageReportEntriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_usage_report_entries, request, EC2DescribeImageUsageReportEntriesResponse)

    async def describe_image_usage_report_entries_paginated(
        self,
        request: EC2DescribeImageUsageReportEntriesRequest | None = None,
    ) -> list[EC2DescribeImageUsageReportEntriesResponse]:
        return await self._paginate('describe_image_usage_report_entries', request, EC2DescribeImageUsageReportEntriesResponse)

    async def describe_image_usage_reports(
        self,
        request: EC2DescribeImageUsageReportsRequest | None = None,
    ) -> EC2DescribeImageUsageReportsResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_usage_reports, request, EC2DescribeImageUsageReportsResponse)

    async def describe_image_usage_reports_paginated(
        self,
        request: EC2DescribeImageUsageReportsRequest | None = None,
    ) -> list[EC2DescribeImageUsageReportsResponse]:
        return await self._paginate('describe_image_usage_reports', request, EC2DescribeImageUsageReportsResponse)

    async def describe_images(
        self,
        request: EC2DescribeImagesRequest | None = None,
    ) -> EC2DescribeImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_images, request, EC2DescribeImagesResponse)

    async def describe_images_paginated(
        self,
        request: EC2DescribeImagesRequest | None = None,
    ) -> list[EC2DescribeImagesResponse]:
        return await self._paginate('describe_images', request, EC2DescribeImagesResponse)

    async def describe_import_image_tasks(
        self,
        request: EC2DescribeImportImageTasksRequest | None = None,
    ) -> EC2DescribeImportImageTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_import_image_tasks, request, EC2DescribeImportImageTasksResponse)

    async def describe_import_image_tasks_paginated(
        self,
        request: EC2DescribeImportImageTasksRequest | None = None,
    ) -> list[EC2DescribeImportImageTasksResponse]:
        return await self._paginate('describe_import_image_tasks', request, EC2DescribeImportImageTasksResponse)

    async def describe_import_snapshot_tasks(
        self,
        request: EC2DescribeImportSnapshotTasksRequest | None = None,
    ) -> EC2DescribeImportSnapshotTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_import_snapshot_tasks, request, EC2DescribeImportSnapshotTasksResponse)

    async def describe_import_snapshot_tasks_paginated(
        self,
        request: EC2DescribeImportSnapshotTasksRequest | None = None,
    ) -> list[EC2DescribeImportSnapshotTasksResponse]:
        return await self._paginate('describe_import_snapshot_tasks', request, EC2DescribeImportSnapshotTasksResponse)

    async def describe_instance_attribute(
        self,
        request: EC2DescribeInstanceAttributeRequest,
    ) -> EC2DescribeInstanceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_attribute, request, EC2DescribeInstanceAttributeResponse)

    async def describe_instance_connect_endpoints(
        self,
        request: EC2DescribeInstanceConnectEndpointsRequest | None = None,
    ) -> EC2DescribeInstanceConnectEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_connect_endpoints, request, EC2DescribeInstanceConnectEndpointsResponse)

    async def describe_instance_connect_endpoints_paginated(
        self,
        request: EC2DescribeInstanceConnectEndpointsRequest | None = None,
    ) -> list[EC2DescribeInstanceConnectEndpointsResponse]:
        return await self._paginate('describe_instance_connect_endpoints', request, EC2DescribeInstanceConnectEndpointsResponse)

    async def describe_instance_credit_specifications(
        self,
        request: EC2DescribeInstanceCreditSpecificationsRequest | None = None,
    ) -> EC2DescribeInstanceCreditSpecificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_credit_specifications, request, EC2DescribeInstanceCreditSpecificationsResponse)

    async def describe_instance_credit_specifications_paginated(
        self,
        request: EC2DescribeInstanceCreditSpecificationsRequest | None = None,
    ) -> list[EC2DescribeInstanceCreditSpecificationsResponse]:
        return await self._paginate('describe_instance_credit_specifications', request, EC2DescribeInstanceCreditSpecificationsResponse)

    async def describe_instance_event_notification_attributes(
        self,
        request: EC2DescribeInstanceEventNotificationAttributesRequest | None = None,
    ) -> EC2DescribeInstanceEventNotificationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_event_notification_attributes, request, EC2DescribeInstanceEventNotificationAttributesResponse)

    async def describe_instance_event_windows(
        self,
        request: EC2DescribeInstanceEventWindowsRequest | None = None,
    ) -> EC2DescribeInstanceEventWindowsResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_event_windows, request, EC2DescribeInstanceEventWindowsResponse)

    async def describe_instance_event_windows_paginated(
        self,
        request: EC2DescribeInstanceEventWindowsRequest | None = None,
    ) -> list[EC2DescribeInstanceEventWindowsResponse]:
        return await self._paginate('describe_instance_event_windows', request, EC2DescribeInstanceEventWindowsResponse)

    async def describe_instance_image_metadata(
        self,
        request: EC2DescribeInstanceImageMetadataRequest | None = None,
    ) -> EC2DescribeInstanceImageMetadataResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_image_metadata, request, EC2DescribeInstanceImageMetadataResponse)

    async def describe_instance_image_metadata_paginated(
        self,
        request: EC2DescribeInstanceImageMetadataRequest | None = None,
    ) -> list[EC2DescribeInstanceImageMetadataResponse]:
        return await self._paginate('describe_instance_image_metadata', request, EC2DescribeInstanceImageMetadataResponse)

    async def describe_instance_sql_ha_history_states(
        self,
        request: EC2DescribeInstanceSqlHaHistoryStatesRequest | None = None,
    ) -> EC2DescribeInstanceSqlHaHistoryStatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_sql_ha_history_states, request, EC2DescribeInstanceSqlHaHistoryStatesResponse)

    async def describe_instance_sql_ha_states(
        self,
        request: EC2DescribeInstanceSqlHaStatesRequest | None = None,
    ) -> EC2DescribeInstanceSqlHaStatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_sql_ha_states, request, EC2DescribeInstanceSqlHaStatesResponse)

    async def describe_instance_status(
        self,
        request: EC2DescribeInstanceStatusRequest | None = None,
    ) -> EC2DescribeInstanceStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_status, request, EC2DescribeInstanceStatusResponse)

    async def describe_instance_status_paginated(
        self,
        request: EC2DescribeInstanceStatusRequest | None = None,
    ) -> list[EC2DescribeInstanceStatusResponse]:
        return await self._paginate('describe_instance_status', request, EC2DescribeInstanceStatusResponse)

    async def describe_instance_topology(
        self,
        request: EC2DescribeInstanceTopologyRequest | None = None,
    ) -> EC2DescribeInstanceTopologyResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_topology, request, EC2DescribeInstanceTopologyResponse)

    async def describe_instance_topology_paginated(
        self,
        request: EC2DescribeInstanceTopologyRequest | None = None,
    ) -> list[EC2DescribeInstanceTopologyResponse]:
        return await self._paginate('describe_instance_topology', request, EC2DescribeInstanceTopologyResponse)

    async def describe_instance_type_offerings(
        self,
        request: EC2DescribeInstanceTypeOfferingsRequest | None = None,
    ) -> EC2DescribeInstanceTypeOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_type_offerings, request, EC2DescribeInstanceTypeOfferingsResponse)

    async def describe_instance_type_offerings_paginated(
        self,
        request: EC2DescribeInstanceTypeOfferingsRequest | None = None,
    ) -> list[EC2DescribeInstanceTypeOfferingsResponse]:
        return await self._paginate('describe_instance_type_offerings', request, EC2DescribeInstanceTypeOfferingsResponse)

    async def describe_instance_types(
        self,
        request: EC2DescribeInstanceTypesRequest | None = None,
    ) -> EC2DescribeInstanceTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_types, request, EC2DescribeInstanceTypesResponse)

    async def describe_instance_types_paginated(
        self,
        request: EC2DescribeInstanceTypesRequest | None = None,
    ) -> list[EC2DescribeInstanceTypesResponse]:
        return await self._paginate('describe_instance_types', request, EC2DescribeInstanceTypesResponse)

    async def describe_internet_gateways(
        self,
        request: EC2DescribeInternetGatewaysRequest | None = None,
    ) -> EC2DescribeInternetGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_internet_gateways, request, EC2DescribeInternetGatewaysResponse)

    async def describe_internet_gateways_paginated(
        self,
        request: EC2DescribeInternetGatewaysRequest | None = None,
    ) -> list[EC2DescribeInternetGatewaysResponse]:
        return await self._paginate('describe_internet_gateways', request, EC2DescribeInternetGatewaysResponse)

    async def describe_ipam_byoasn(
        self,
        request: EC2DescribeIpamByoasnRequest | None = None,
    ) -> EC2DescribeIpamByoasnResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_byoasn, request, EC2DescribeIpamByoasnResponse)

    async def describe_ipam_external_resource_verification_tokens(
        self,
        request: EC2DescribeIpamExternalResourceVerificationTokensRequest | None = None,
    ) -> EC2DescribeIpamExternalResourceVerificationTokensResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_external_resource_verification_tokens, request, EC2DescribeIpamExternalResourceVerificationTokensResponse)

    async def describe_ipam_internet_registry_associations(
        self,
        request: EC2DescribeIpamInternetRegistryAssociationsRequest | None = None,
    ) -> EC2DescribeIpamInternetRegistryAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_internet_registry_associations, request, EC2DescribeIpamInternetRegistryAssociationsResponse)

    async def describe_ipam_policies(
        self,
        request: EC2DescribeIpamPoliciesRequest | None = None,
    ) -> EC2DescribeIpamPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_policies, request, EC2DescribeIpamPoliciesResponse)

    async def describe_ipam_pool_allocations(
        self,
        request: EC2DescribeIpamPoolAllocationsRequest | None = None,
    ) -> EC2DescribeIpamPoolAllocationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_pool_allocations, request, EC2DescribeIpamPoolAllocationsResponse)

    async def describe_ipam_pool_allocations_paginated(
        self,
        request: EC2DescribeIpamPoolAllocationsRequest | None = None,
    ) -> list[EC2DescribeIpamPoolAllocationsResponse]:
        return await self._paginate('describe_ipam_pool_allocations', request, EC2DescribeIpamPoolAllocationsResponse)

    async def describe_ipam_pools(
        self,
        request: EC2DescribeIpamPoolsRequest | None = None,
    ) -> EC2DescribeIpamPoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_pools, request, EC2DescribeIpamPoolsResponse)

    async def describe_ipam_pools_paginated(
        self,
        request: EC2DescribeIpamPoolsRequest | None = None,
    ) -> list[EC2DescribeIpamPoolsResponse]:
        return await self._paginate('describe_ipam_pools', request, EC2DescribeIpamPoolsResponse)

    async def describe_ipam_prefix_list_resolver_targets(
        self,
        request: EC2DescribeIpamPrefixListResolverTargetsRequest | None = None,
    ) -> EC2DescribeIpamPrefixListResolverTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_prefix_list_resolver_targets, request, EC2DescribeIpamPrefixListResolverTargetsResponse)

    async def describe_ipam_prefix_list_resolver_targets_paginated(
        self,
        request: EC2DescribeIpamPrefixListResolverTargetsRequest | None = None,
    ) -> list[EC2DescribeIpamPrefixListResolverTargetsResponse]:
        return await self._paginate('describe_ipam_prefix_list_resolver_targets', request, EC2DescribeIpamPrefixListResolverTargetsResponse)

    async def describe_ipam_prefix_list_resolvers(
        self,
        request: EC2DescribeIpamPrefixListResolversRequest | None = None,
    ) -> EC2DescribeIpamPrefixListResolversResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_prefix_list_resolvers, request, EC2DescribeIpamPrefixListResolversResponse)

    async def describe_ipam_prefix_list_resolvers_paginated(
        self,
        request: EC2DescribeIpamPrefixListResolversRequest | None = None,
    ) -> list[EC2DescribeIpamPrefixListResolversResponse]:
        return await self._paginate('describe_ipam_prefix_list_resolvers', request, EC2DescribeIpamPrefixListResolversResponse)

    async def describe_ipam_resource_discoveries(
        self,
        request: EC2DescribeIpamResourceDiscoveriesRequest | None = None,
    ) -> EC2DescribeIpamResourceDiscoveriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_resource_discoveries, request, EC2DescribeIpamResourceDiscoveriesResponse)

    async def describe_ipam_resource_discoveries_paginated(
        self,
        request: EC2DescribeIpamResourceDiscoveriesRequest | None = None,
    ) -> list[EC2DescribeIpamResourceDiscoveriesResponse]:
        return await self._paginate('describe_ipam_resource_discoveries', request, EC2DescribeIpamResourceDiscoveriesResponse)

    async def describe_ipam_resource_discovery_associations(
        self,
        request: EC2DescribeIpamResourceDiscoveryAssociationsRequest | None = None,
    ) -> EC2DescribeIpamResourceDiscoveryAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_resource_discovery_associations, request, EC2DescribeIpamResourceDiscoveryAssociationsResponse)

    async def describe_ipam_resource_discovery_associations_paginated(
        self,
        request: EC2DescribeIpamResourceDiscoveryAssociationsRequest | None = None,
    ) -> list[EC2DescribeIpamResourceDiscoveryAssociationsResponse]:
        return await self._paginate('describe_ipam_resource_discovery_associations', request, EC2DescribeIpamResourceDiscoveryAssociationsResponse)

    async def describe_ipam_scopes(
        self,
        request: EC2DescribeIpamScopesRequest | None = None,
    ) -> EC2DescribeIpamScopesResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipam_scopes, request, EC2DescribeIpamScopesResponse)

    async def describe_ipam_scopes_paginated(
        self,
        request: EC2DescribeIpamScopesRequest | None = None,
    ) -> list[EC2DescribeIpamScopesResponse]:
        return await self._paginate('describe_ipam_scopes', request, EC2DescribeIpamScopesResponse)

    async def describe_ipams(
        self,
        request: EC2DescribeIpamsRequest | None = None,
    ) -> EC2DescribeIpamsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipams, request, EC2DescribeIpamsResponse)

    async def describe_ipams_paginated(
        self,
        request: EC2DescribeIpamsRequest | None = None,
    ) -> list[EC2DescribeIpamsResponse]:
        return await self._paginate('describe_ipams', request, EC2DescribeIpamsResponse)

    async def describe_ipv6_pools(
        self,
        request: EC2DescribeIpv6PoolsRequest | None = None,
    ) -> EC2DescribeIpv6PoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ipv6_pools, request, EC2DescribeIpv6PoolsResponse)

    async def describe_ipv6_pools_paginated(
        self,
        request: EC2DescribeIpv6PoolsRequest | None = None,
    ) -> list[EC2DescribeIpv6PoolsResponse]:
        return await self._paginate('describe_ipv6_pools', request, EC2DescribeIpv6PoolsResponse)

    async def describe_launch_template_versions(
        self,
        request: EC2DescribeLaunchTemplateVersionsRequest | None = None,
    ) -> EC2DescribeLaunchTemplateVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_launch_template_versions, request, EC2DescribeLaunchTemplateVersionsResponse)

    async def describe_launch_template_versions_paginated(
        self,
        request: EC2DescribeLaunchTemplateVersionsRequest | None = None,
    ) -> list[EC2DescribeLaunchTemplateVersionsResponse]:
        return await self._paginate('describe_launch_template_versions', request, EC2DescribeLaunchTemplateVersionsResponse)

    async def describe_launch_templates(
        self,
        request: EC2DescribeLaunchTemplatesRequest | None = None,
    ) -> EC2DescribeLaunchTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_launch_templates, request, EC2DescribeLaunchTemplatesResponse)

    async def describe_launch_templates_paginated(
        self,
        request: EC2DescribeLaunchTemplatesRequest | None = None,
    ) -> list[EC2DescribeLaunchTemplatesResponse]:
        return await self._paginate('describe_launch_templates', request, EC2DescribeLaunchTemplatesResponse)

    async def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        request: EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest | None = None,
    ) -> EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateway_route_table_virtual_interface_group_associations, request, EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponse)

    async def describe_local_gateway_route_table_virtual_interface_group_associations_paginated(
        self,
        request: EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest | None = None,
    ) -> list[EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponse]:
        return await self._paginate('describe_local_gateway_route_table_virtual_interface_group_associations', request, EC2DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponse)

    async def describe_local_gateway_route_table_vpc_associations(
        self,
        request: EC2DescribeLocalGatewayRouteTableVpcAssociationsRequest | None = None,
    ) -> EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateway_route_table_vpc_associations, request, EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse)

    async def describe_local_gateway_route_table_vpc_associations_paginated(
        self,
        request: EC2DescribeLocalGatewayRouteTableVpcAssociationsRequest | None = None,
    ) -> list[EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse]:
        return await self._paginate('describe_local_gateway_route_table_vpc_associations', request, EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse)

    async def describe_local_gateway_route_tables(
        self,
        request: EC2DescribeLocalGatewayRouteTablesRequest | None = None,
    ) -> EC2DescribeLocalGatewayRouteTablesResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateway_route_tables, request, EC2DescribeLocalGatewayRouteTablesResponse)

    async def describe_local_gateway_route_tables_paginated(
        self,
        request: EC2DescribeLocalGatewayRouteTablesRequest | None = None,
    ) -> list[EC2DescribeLocalGatewayRouteTablesResponse]:
        return await self._paginate('describe_local_gateway_route_tables', request, EC2DescribeLocalGatewayRouteTablesResponse)

    async def describe_local_gateway_virtual_interface_groups(
        self,
        request: EC2DescribeLocalGatewayVirtualInterfaceGroupsRequest | None = None,
    ) -> EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateway_virtual_interface_groups, request, EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse)

    async def describe_local_gateway_virtual_interface_groups_paginated(
        self,
        request: EC2DescribeLocalGatewayVirtualInterfaceGroupsRequest | None = None,
    ) -> list[EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse]:
        return await self._paginate('describe_local_gateway_virtual_interface_groups', request, EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse)

    async def describe_local_gateway_virtual_interfaces(
        self,
        request: EC2DescribeLocalGatewayVirtualInterfacesRequest | None = None,
    ) -> EC2DescribeLocalGatewayVirtualInterfacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateway_virtual_interfaces, request, EC2DescribeLocalGatewayVirtualInterfacesResponse)

    async def describe_local_gateway_virtual_interfaces_paginated(
        self,
        request: EC2DescribeLocalGatewayVirtualInterfacesRequest | None = None,
    ) -> list[EC2DescribeLocalGatewayVirtualInterfacesResponse]:
        return await self._paginate('describe_local_gateway_virtual_interfaces', request, EC2DescribeLocalGatewayVirtualInterfacesResponse)

    async def describe_local_gateways(
        self,
        request: EC2DescribeLocalGatewaysRequest | None = None,
    ) -> EC2DescribeLocalGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_local_gateways, request, EC2DescribeLocalGatewaysResponse)

    async def describe_local_gateways_paginated(
        self,
        request: EC2DescribeLocalGatewaysRequest | None = None,
    ) -> list[EC2DescribeLocalGatewaysResponse]:
        return await self._paginate('describe_local_gateways', request, EC2DescribeLocalGatewaysResponse)

    async def describe_locked_snapshots(
        self,
        request: EC2DescribeLockedSnapshotsRequest | None = None,
    ) -> EC2DescribeLockedSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_locked_snapshots, request, EC2DescribeLockedSnapshotsResponse)

    async def describe_mac_hosts(
        self,
        request: EC2DescribeMacHostsRequest | None = None,
    ) -> EC2DescribeMacHostsResponse:
        client = self._require_client()
        return await self._execute(client.describe_mac_hosts, request, EC2DescribeMacHostsResponse)

    async def describe_mac_hosts_paginated(
        self,
        request: EC2DescribeMacHostsRequest | None = None,
    ) -> list[EC2DescribeMacHostsResponse]:
        return await self._paginate('describe_mac_hosts', request, EC2DescribeMacHostsResponse)

    async def describe_mac_modification_tasks(
        self,
        request: EC2DescribeMacModificationTasksRequest | None = None,
    ) -> EC2DescribeMacModificationTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_mac_modification_tasks, request, EC2DescribeMacModificationTasksResponse)

    async def describe_mac_modification_tasks_paginated(
        self,
        request: EC2DescribeMacModificationTasksRequest | None = None,
    ) -> list[EC2DescribeMacModificationTasksResponse]:
        return await self._paginate('describe_mac_modification_tasks', request, EC2DescribeMacModificationTasksResponse)

    async def describe_managed_prefix_lists(
        self,
        request: EC2DescribeManagedPrefixListsRequest | None = None,
    ) -> EC2DescribeManagedPrefixListsResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_prefix_lists, request, EC2DescribeManagedPrefixListsResponse)

    async def describe_managed_prefix_lists_paginated(
        self,
        request: EC2DescribeManagedPrefixListsRequest | None = None,
    ) -> list[EC2DescribeManagedPrefixListsResponse]:
        return await self._paginate('describe_managed_prefix_lists', request, EC2DescribeManagedPrefixListsResponse)

    async def describe_metric_categories(
        self,
        request: EC2DescribeMetricCategoriesRequest | None = None,
    ) -> EC2DescribeMetricCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_metric_categories, request, EC2DescribeMetricCategoriesResponse)

    async def describe_metric_categories_paginated(
        self,
        request: EC2DescribeMetricCategoriesRequest | None = None,
    ) -> list[EC2DescribeMetricCategoriesResponse]:
        return await self._paginate('describe_metric_categories', request, EC2DescribeMetricCategoriesResponse)

    async def describe_moving_addresses(
        self,
        request: EC2DescribeMovingAddressesRequest | None = None,
    ) -> EC2DescribeMovingAddressesResponse:
        client = self._require_client()
        return await self._execute(client.describe_moving_addresses, request, EC2DescribeMovingAddressesResponse)

    async def describe_moving_addresses_paginated(
        self,
        request: EC2DescribeMovingAddressesRequest | None = None,
    ) -> list[EC2DescribeMovingAddressesResponse]:
        return await self._paginate('describe_moving_addresses', request, EC2DescribeMovingAddressesResponse)

    async def describe_nat_gateways(
        self,
        request: EC2DescribeNatGatewaysRequest | None = None,
    ) -> EC2DescribeNatGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_nat_gateways, request, EC2DescribeNatGatewaysResponse)

    async def describe_nat_gateways_paginated(
        self,
        request: EC2DescribeNatGatewaysRequest | None = None,
    ) -> list[EC2DescribeNatGatewaysResponse]:
        return await self._paginate('describe_nat_gateways', request, EC2DescribeNatGatewaysResponse)

    async def describe_network_acls(
        self,
        request: EC2DescribeNetworkAclsRequest | None = None,
    ) -> EC2DescribeNetworkAclsResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_acls, request, EC2DescribeNetworkAclsResponse)

    async def describe_network_acls_paginated(
        self,
        request: EC2DescribeNetworkAclsRequest | None = None,
    ) -> list[EC2DescribeNetworkAclsResponse]:
        return await self._paginate('describe_network_acls', request, EC2DescribeNetworkAclsResponse)

    async def describe_network_insights_access_scope_analyses(
        self,
        request: EC2DescribeNetworkInsightsAccessScopeAnalysesRequest | None = None,
    ) -> EC2DescribeNetworkInsightsAccessScopeAnalysesResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_insights_access_scope_analyses, request, EC2DescribeNetworkInsightsAccessScopeAnalysesResponse)

    async def describe_network_insights_access_scope_analyses_paginated(
        self,
        request: EC2DescribeNetworkInsightsAccessScopeAnalysesRequest | None = None,
    ) -> list[EC2DescribeNetworkInsightsAccessScopeAnalysesResponse]:
        return await self._paginate('describe_network_insights_access_scope_analyses', request, EC2DescribeNetworkInsightsAccessScopeAnalysesResponse)

    async def describe_network_insights_access_scopes(
        self,
        request: EC2DescribeNetworkInsightsAccessScopesRequest | None = None,
    ) -> EC2DescribeNetworkInsightsAccessScopesResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_insights_access_scopes, request, EC2DescribeNetworkInsightsAccessScopesResponse)

    async def describe_network_insights_access_scopes_paginated(
        self,
        request: EC2DescribeNetworkInsightsAccessScopesRequest | None = None,
    ) -> list[EC2DescribeNetworkInsightsAccessScopesResponse]:
        return await self._paginate('describe_network_insights_access_scopes', request, EC2DescribeNetworkInsightsAccessScopesResponse)

    async def describe_network_insights_analyses(
        self,
        request: EC2DescribeNetworkInsightsAnalysesRequest | None = None,
    ) -> EC2DescribeNetworkInsightsAnalysesResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_insights_analyses, request, EC2DescribeNetworkInsightsAnalysesResponse)

    async def describe_network_insights_analyses_paginated(
        self,
        request: EC2DescribeNetworkInsightsAnalysesRequest | None = None,
    ) -> list[EC2DescribeNetworkInsightsAnalysesResponse]:
        return await self._paginate('describe_network_insights_analyses', request, EC2DescribeNetworkInsightsAnalysesResponse)

    async def describe_network_insights_paths(
        self,
        request: EC2DescribeNetworkInsightsPathsRequest | None = None,
    ) -> EC2DescribeNetworkInsightsPathsResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_insights_paths, request, EC2DescribeNetworkInsightsPathsResponse)

    async def describe_network_insights_paths_paginated(
        self,
        request: EC2DescribeNetworkInsightsPathsRequest | None = None,
    ) -> list[EC2DescribeNetworkInsightsPathsResponse]:
        return await self._paginate('describe_network_insights_paths', request, EC2DescribeNetworkInsightsPathsResponse)

    async def describe_network_interface_attribute(
        self,
        request: EC2DescribeNetworkInterfaceAttributeRequest,
    ) -> EC2DescribeNetworkInterfaceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_interface_attribute, request, EC2DescribeNetworkInterfaceAttributeResponse)

    async def describe_network_interface_permissions(
        self,
        request: EC2DescribeNetworkInterfacePermissionsRequest | None = None,
    ) -> EC2DescribeNetworkInterfacePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_interface_permissions, request, EC2DescribeNetworkInterfacePermissionsResponse)

    async def describe_network_interface_permissions_paginated(
        self,
        request: EC2DescribeNetworkInterfacePermissionsRequest | None = None,
    ) -> list[EC2DescribeNetworkInterfacePermissionsResponse]:
        return await self._paginate('describe_network_interface_permissions', request, EC2DescribeNetworkInterfacePermissionsResponse)

    async def describe_network_interfaces(
        self,
        request: EC2DescribeNetworkInterfacesRequest | None = None,
    ) -> EC2DescribeNetworkInterfacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_network_interfaces, request, EC2DescribeNetworkInterfacesResponse)

    async def describe_network_interfaces_paginated(
        self,
        request: EC2DescribeNetworkInterfacesRequest | None = None,
    ) -> list[EC2DescribeNetworkInterfacesResponse]:
        return await self._paginate('describe_network_interfaces', request, EC2DescribeNetworkInterfacesResponse)

    async def describe_networking_flex_cost_allocation_policies(
        self,
        request: EC2DescribeNetworkingFlexCostAllocationPoliciesRequest | None = None,
    ) -> EC2DescribeNetworkingFlexCostAllocationPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_networking_flex_cost_allocation_policies, request, EC2DescribeNetworkingFlexCostAllocationPoliciesResponse)

    async def describe_networking_flex_cost_allocation_policies_paginated(
        self,
        request: EC2DescribeNetworkingFlexCostAllocationPoliciesRequest | None = None,
    ) -> list[EC2DescribeNetworkingFlexCostAllocationPoliciesResponse]:
        return await self._paginate('describe_networking_flex_cost_allocation_policies', request, EC2DescribeNetworkingFlexCostAllocationPoliciesResponse)

    async def describe_networking_flex_cost_allocation_policy_associations(
        self,
        request: EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsRequest | None = None,
    ) -> EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_networking_flex_cost_allocation_policy_associations, request, EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse)

    async def describe_networking_flex_cost_allocation_policy_associations_paginated(
        self,
        request: EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsRequest | None = None,
    ) -> list[EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse]:
        return await self._paginate('describe_networking_flex_cost_allocation_policy_associations', request, EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse)

    async def describe_outpost_lags(
        self,
        request: EC2DescribeOutpostLagsRequest | None = None,
    ) -> EC2DescribeOutpostLagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_outpost_lags, request, EC2DescribeOutpostLagsResponse)

    async def describe_placement_groups(
        self,
        request: EC2DescribePlacementGroupsRequest | None = None,
    ) -> EC2DescribePlacementGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_placement_groups, request, EC2DescribePlacementGroupsResponse)

    async def describe_prefix_lists(
        self,
        request: EC2DescribePrefixListsRequest | None = None,
    ) -> EC2DescribePrefixListsResponse:
        client = self._require_client()
        return await self._execute(client.describe_prefix_lists, request, EC2DescribePrefixListsResponse)

    async def describe_prefix_lists_paginated(
        self,
        request: EC2DescribePrefixListsRequest | None = None,
    ) -> list[EC2DescribePrefixListsResponse]:
        return await self._paginate('describe_prefix_lists', request, EC2DescribePrefixListsResponse)

    async def describe_principal_id_format(
        self,
        request: EC2DescribePrincipalIdFormatRequest | None = None,
    ) -> EC2DescribePrincipalIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.describe_principal_id_format, request, EC2DescribePrincipalIdFormatResponse)

    async def describe_principal_id_format_paginated(
        self,
        request: EC2DescribePrincipalIdFormatRequest | None = None,
    ) -> list[EC2DescribePrincipalIdFormatResponse]:
        return await self._paginate('describe_principal_id_format', request, EC2DescribePrincipalIdFormatResponse)

    async def describe_public_ipv4_pools(
        self,
        request: EC2DescribePublicIpv4PoolsRequest | None = None,
    ) -> EC2DescribePublicIpv4PoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_public_ipv4_pools, request, EC2DescribePublicIpv4PoolsResponse)

    async def describe_public_ipv4_pools_paginated(
        self,
        request: EC2DescribePublicIpv4PoolsRequest | None = None,
    ) -> list[EC2DescribePublicIpv4PoolsResponse]:
        return await self._paginate('describe_public_ipv4_pools', request, EC2DescribePublicIpv4PoolsResponse)

    async def describe_regions(
        self,
        request: EC2DescribeRegionsRequest | None = None,
    ) -> EC2DescribeRegionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_regions, request, EC2DescribeRegionsResponse)

    async def describe_replace_root_volume_tasks(
        self,
        request: EC2DescribeReplaceRootVolumeTasksRequest | None = None,
    ) -> EC2DescribeReplaceRootVolumeTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_replace_root_volume_tasks, request, EC2DescribeReplaceRootVolumeTasksResponse)

    async def describe_replace_root_volume_tasks_paginated(
        self,
        request: EC2DescribeReplaceRootVolumeTasksRequest | None = None,
    ) -> list[EC2DescribeReplaceRootVolumeTasksResponse]:
        return await self._paginate('describe_replace_root_volume_tasks', request, EC2DescribeReplaceRootVolumeTasksResponse)

    async def describe_reserved_instances(
        self,
        request: EC2DescribeReservedInstancesRequest | None = None,
    ) -> EC2DescribeReservedInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instances, request, EC2DescribeReservedInstancesResponse)

    async def describe_reserved_instances_listings(
        self,
        request: EC2DescribeReservedInstancesListingsRequest | None = None,
    ) -> EC2DescribeReservedInstancesListingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instances_listings, request, EC2DescribeReservedInstancesListingsResponse)

    async def describe_reserved_instances_modifications(
        self,
        request: EC2DescribeReservedInstancesModificationsRequest | None = None,
    ) -> EC2DescribeReservedInstancesModificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instances_modifications, request, EC2DescribeReservedInstancesModificationsResponse)

    async def describe_reserved_instances_modifications_paginated(
        self,
        request: EC2DescribeReservedInstancesModificationsRequest | None = None,
    ) -> list[EC2DescribeReservedInstancesModificationsResponse]:
        return await self._paginate('describe_reserved_instances_modifications', request, EC2DescribeReservedInstancesModificationsResponse)

    async def describe_reserved_instances_offerings(
        self,
        request: EC2DescribeReservedInstancesOfferingsRequest | None = None,
    ) -> EC2DescribeReservedInstancesOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instances_offerings, request, EC2DescribeReservedInstancesOfferingsResponse)

    async def describe_reserved_instances_offerings_paginated(
        self,
        request: EC2DescribeReservedInstancesOfferingsRequest | None = None,
    ) -> list[EC2DescribeReservedInstancesOfferingsResponse]:
        return await self._paginate('describe_reserved_instances_offerings', request, EC2DescribeReservedInstancesOfferingsResponse)

    async def describe_route_server_endpoints(
        self,
        request: EC2DescribeRouteServerEndpointsRequest | None = None,
    ) -> EC2DescribeRouteServerEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_route_server_endpoints, request, EC2DescribeRouteServerEndpointsResponse)

    async def describe_route_server_endpoints_paginated(
        self,
        request: EC2DescribeRouteServerEndpointsRequest | None = None,
    ) -> list[EC2DescribeRouteServerEndpointsResponse]:
        return await self._paginate('describe_route_server_endpoints', request, EC2DescribeRouteServerEndpointsResponse)

    async def describe_route_server_peers(
        self,
        request: EC2DescribeRouteServerPeersRequest | None = None,
    ) -> EC2DescribeRouteServerPeersResponse:
        client = self._require_client()
        return await self._execute(client.describe_route_server_peers, request, EC2DescribeRouteServerPeersResponse)

    async def describe_route_server_peers_paginated(
        self,
        request: EC2DescribeRouteServerPeersRequest | None = None,
    ) -> list[EC2DescribeRouteServerPeersResponse]:
        return await self._paginate('describe_route_server_peers', request, EC2DescribeRouteServerPeersResponse)

    async def describe_route_servers(
        self,
        request: EC2DescribeRouteServersRequest | None = None,
    ) -> EC2DescribeRouteServersResponse:
        client = self._require_client()
        return await self._execute(client.describe_route_servers, request, EC2DescribeRouteServersResponse)

    async def describe_route_servers_paginated(
        self,
        request: EC2DescribeRouteServersRequest | None = None,
    ) -> list[EC2DescribeRouteServersResponse]:
        return await self._paginate('describe_route_servers', request, EC2DescribeRouteServersResponse)

    async def describe_route_tables(
        self,
        request: EC2DescribeRouteTablesRequest | None = None,
    ) -> EC2DescribeRouteTablesResponse:
        client = self._require_client()
        return await self._execute(client.describe_route_tables, request, EC2DescribeRouteTablesResponse)

    async def describe_route_tables_paginated(
        self,
        request: EC2DescribeRouteTablesRequest | None = None,
    ) -> list[EC2DescribeRouteTablesResponse]:
        return await self._paginate('describe_route_tables', request, EC2DescribeRouteTablesResponse)

    async def describe_scheduled_instance_availability(
        self,
        request: EC2DescribeScheduledInstanceAvailabilityRequest,
    ) -> EC2DescribeScheduledInstanceAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_instance_availability, request, EC2DescribeScheduledInstanceAvailabilityResponse)

    async def describe_scheduled_instance_availability_paginated(
        self,
        request: EC2DescribeScheduledInstanceAvailabilityRequest,
    ) -> list[EC2DescribeScheduledInstanceAvailabilityResponse]:
        return await self._paginate('describe_scheduled_instance_availability', request, EC2DescribeScheduledInstanceAvailabilityResponse)

    async def describe_scheduled_instances(
        self,
        request: EC2DescribeScheduledInstancesRequest | None = None,
    ) -> EC2DescribeScheduledInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_instances, request, EC2DescribeScheduledInstancesResponse)

    async def describe_scheduled_instances_paginated(
        self,
        request: EC2DescribeScheduledInstancesRequest | None = None,
    ) -> list[EC2DescribeScheduledInstancesResponse]:
        return await self._paginate('describe_scheduled_instances', request, EC2DescribeScheduledInstancesResponse)

    async def describe_secondary_interfaces(
        self,
        request: EC2DescribeSecondaryInterfacesRequest | None = None,
    ) -> EC2DescribeSecondaryInterfacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_secondary_interfaces, request, EC2DescribeSecondaryInterfacesResponse)

    async def describe_secondary_interfaces_paginated(
        self,
        request: EC2DescribeSecondaryInterfacesRequest | None = None,
    ) -> list[EC2DescribeSecondaryInterfacesResponse]:
        return await self._paginate('describe_secondary_interfaces', request, EC2DescribeSecondaryInterfacesResponse)

    async def describe_secondary_networks(
        self,
        request: EC2DescribeSecondaryNetworksRequest | None = None,
    ) -> EC2DescribeSecondaryNetworksResponse:
        client = self._require_client()
        return await self._execute(client.describe_secondary_networks, request, EC2DescribeSecondaryNetworksResponse)

    async def describe_secondary_networks_paginated(
        self,
        request: EC2DescribeSecondaryNetworksRequest | None = None,
    ) -> list[EC2DescribeSecondaryNetworksResponse]:
        return await self._paginate('describe_secondary_networks', request, EC2DescribeSecondaryNetworksResponse)

    async def describe_secondary_subnets(
        self,
        request: EC2DescribeSecondarySubnetsRequest | None = None,
    ) -> EC2DescribeSecondarySubnetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_secondary_subnets, request, EC2DescribeSecondarySubnetsResponse)

    async def describe_secondary_subnets_paginated(
        self,
        request: EC2DescribeSecondarySubnetsRequest | None = None,
    ) -> list[EC2DescribeSecondarySubnetsResponse]:
        return await self._paginate('describe_secondary_subnets', request, EC2DescribeSecondarySubnetsResponse)

    async def describe_security_group_references(
        self,
        request: EC2DescribeSecurityGroupReferencesRequest,
    ) -> EC2DescribeSecurityGroupReferencesResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_group_references, request, EC2DescribeSecurityGroupReferencesResponse)

    async def describe_security_group_rules(
        self,
        request: EC2DescribeSecurityGroupRulesRequest | None = None,
    ) -> EC2DescribeSecurityGroupRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_group_rules, request, EC2DescribeSecurityGroupRulesResponse)

    async def describe_security_group_rules_paginated(
        self,
        request: EC2DescribeSecurityGroupRulesRequest | None = None,
    ) -> list[EC2DescribeSecurityGroupRulesResponse]:
        return await self._paginate('describe_security_group_rules', request, EC2DescribeSecurityGroupRulesResponse)

    async def describe_security_group_vpc_associations(
        self,
        request: EC2DescribeSecurityGroupVpcAssociationsRequest | None = None,
    ) -> EC2DescribeSecurityGroupVpcAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_group_vpc_associations, request, EC2DescribeSecurityGroupVpcAssociationsResponse)

    async def describe_security_group_vpc_associations_paginated(
        self,
        request: EC2DescribeSecurityGroupVpcAssociationsRequest | None = None,
    ) -> list[EC2DescribeSecurityGroupVpcAssociationsResponse]:
        return await self._paginate('describe_security_group_vpc_associations', request, EC2DescribeSecurityGroupVpcAssociationsResponse)

    async def describe_service_link_virtual_interfaces(
        self,
        request: EC2DescribeServiceLinkVirtualInterfacesRequest | None = None,
    ) -> EC2DescribeServiceLinkVirtualInterfacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_link_virtual_interfaces, request, EC2DescribeServiceLinkVirtualInterfacesResponse)

    async def describe_snapshot_attribute(
        self,
        request: EC2DescribeSnapshotAttributeRequest,
    ) -> EC2DescribeSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_attribute, request, EC2DescribeSnapshotAttributeResponse)

    async def describe_snapshot_tier_status(
        self,
        request: EC2DescribeSnapshotTierStatusRequest | None = None,
    ) -> EC2DescribeSnapshotTierStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_tier_status, request, EC2DescribeSnapshotTierStatusResponse)

    async def describe_snapshot_tier_status_paginated(
        self,
        request: EC2DescribeSnapshotTierStatusRequest | None = None,
    ) -> list[EC2DescribeSnapshotTierStatusResponse]:
        return await self._paginate('describe_snapshot_tier_status', request, EC2DescribeSnapshotTierStatusResponse)

    async def describe_spot_datafeed_subscription(
        self,
        request: EC2DescribeSpotDatafeedSubscriptionRequest | None = None,
    ) -> EC2DescribeSpotDatafeedSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_datafeed_subscription, request, EC2DescribeSpotDatafeedSubscriptionResponse)

    async def describe_spot_fleet_instances(
        self,
        request: EC2DescribeSpotFleetInstancesRequest,
    ) -> EC2DescribeSpotFleetInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_fleet_instances, request, EC2DescribeSpotFleetInstancesResponse)

    async def describe_spot_fleet_instances_paginated(
        self,
        request: EC2DescribeSpotFleetInstancesRequest,
    ) -> list[EC2DescribeSpotFleetInstancesResponse]:
        return await self._paginate('describe_spot_fleet_instances', request, EC2DescribeSpotFleetInstancesResponse)

    async def describe_spot_fleet_request_history(
        self,
        request: EC2DescribeSpotFleetRequestHistoryRequest,
    ) -> EC2DescribeSpotFleetRequestHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_fleet_request_history, request, EC2DescribeSpotFleetRequestHistoryResponse)

    async def describe_spot_fleet_requests(
        self,
        request: EC2DescribeSpotFleetRequestsRequest | None = None,
    ) -> EC2DescribeSpotFleetRequestsResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_fleet_requests, request, EC2DescribeSpotFleetRequestsResponse)

    async def describe_spot_fleet_requests_paginated(
        self,
        request: EC2DescribeSpotFleetRequestsRequest | None = None,
    ) -> list[EC2DescribeSpotFleetRequestsResponse]:
        return await self._paginate('describe_spot_fleet_requests', request, EC2DescribeSpotFleetRequestsResponse)

    async def describe_spot_instance_requests(
        self,
        request: EC2DescribeSpotInstanceRequestsRequest | None = None,
    ) -> EC2DescribeSpotInstanceRequestsResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_instance_requests, request, EC2DescribeSpotInstanceRequestsResponse)

    async def describe_spot_instance_requests_paginated(
        self,
        request: EC2DescribeSpotInstanceRequestsRequest | None = None,
    ) -> list[EC2DescribeSpotInstanceRequestsResponse]:
        return await self._paginate('describe_spot_instance_requests', request, EC2DescribeSpotInstanceRequestsResponse)

    async def describe_spot_price_history(
        self,
        request: EC2DescribeSpotPriceHistoryRequest | None = None,
    ) -> EC2DescribeSpotPriceHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_spot_price_history, request, EC2DescribeSpotPriceHistoryResponse)

    async def describe_spot_price_history_paginated(
        self,
        request: EC2DescribeSpotPriceHistoryRequest | None = None,
    ) -> list[EC2DescribeSpotPriceHistoryResponse]:
        return await self._paginate('describe_spot_price_history', request, EC2DescribeSpotPriceHistoryResponse)

    async def describe_stale_security_groups(
        self,
        request: EC2DescribeStaleSecurityGroupsRequest,
    ) -> EC2DescribeStaleSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_stale_security_groups, request, EC2DescribeStaleSecurityGroupsResponse)

    async def describe_stale_security_groups_paginated(
        self,
        request: EC2DescribeStaleSecurityGroupsRequest,
    ) -> list[EC2DescribeStaleSecurityGroupsResponse]:
        return await self._paginate('describe_stale_security_groups', request, EC2DescribeStaleSecurityGroupsResponse)

    async def describe_store_image_tasks(
        self,
        request: EC2DescribeStoreImageTasksRequest | None = None,
    ) -> EC2DescribeStoreImageTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_store_image_tasks, request, EC2DescribeStoreImageTasksResponse)

    async def describe_store_image_tasks_paginated(
        self,
        request: EC2DescribeStoreImageTasksRequest | None = None,
    ) -> list[EC2DescribeStoreImageTasksResponse]:
        return await self._paginate('describe_store_image_tasks', request, EC2DescribeStoreImageTasksResponse)

    async def describe_tags(
        self,
        request: EC2DescribeTagsRequest | None = None,
    ) -> EC2DescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, EC2DescribeTagsResponse)

    async def describe_tags_paginated(
        self,
        request: EC2DescribeTagsRequest | None = None,
    ) -> list[EC2DescribeTagsResponse]:
        return await self._paginate('describe_tags', request, EC2DescribeTagsResponse)

    async def describe_traffic_mirror_filter_rules(
        self,
        request: EC2DescribeTrafficMirrorFilterRulesRequest | None = None,
    ) -> EC2DescribeTrafficMirrorFilterRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_mirror_filter_rules, request, EC2DescribeTrafficMirrorFilterRulesResponse)

    async def describe_traffic_mirror_filters(
        self,
        request: EC2DescribeTrafficMirrorFiltersRequest | None = None,
    ) -> EC2DescribeTrafficMirrorFiltersResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_mirror_filters, request, EC2DescribeTrafficMirrorFiltersResponse)

    async def describe_traffic_mirror_filters_paginated(
        self,
        request: EC2DescribeTrafficMirrorFiltersRequest | None = None,
    ) -> list[EC2DescribeTrafficMirrorFiltersResponse]:
        return await self._paginate('describe_traffic_mirror_filters', request, EC2DescribeTrafficMirrorFiltersResponse)

    async def describe_traffic_mirror_sessions(
        self,
        request: EC2DescribeTrafficMirrorSessionsRequest | None = None,
    ) -> EC2DescribeTrafficMirrorSessionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_mirror_sessions, request, EC2DescribeTrafficMirrorSessionsResponse)

    async def describe_traffic_mirror_sessions_paginated(
        self,
        request: EC2DescribeTrafficMirrorSessionsRequest | None = None,
    ) -> list[EC2DescribeTrafficMirrorSessionsResponse]:
        return await self._paginate('describe_traffic_mirror_sessions', request, EC2DescribeTrafficMirrorSessionsResponse)

    async def describe_traffic_mirror_targets(
        self,
        request: EC2DescribeTrafficMirrorTargetsRequest | None = None,
    ) -> EC2DescribeTrafficMirrorTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_mirror_targets, request, EC2DescribeTrafficMirrorTargetsResponse)

    async def describe_traffic_mirror_targets_paginated(
        self,
        request: EC2DescribeTrafficMirrorTargetsRequest | None = None,
    ) -> list[EC2DescribeTrafficMirrorTargetsResponse]:
        return await self._paginate('describe_traffic_mirror_targets', request, EC2DescribeTrafficMirrorTargetsResponse)

    async def describe_transit_gateway_attachments(
        self,
        request: EC2DescribeTransitGatewayAttachmentsRequest | None = None,
    ) -> EC2DescribeTransitGatewayAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_attachments, request, EC2DescribeTransitGatewayAttachmentsResponse)

    async def describe_transit_gateway_attachments_paginated(
        self,
        request: EC2DescribeTransitGatewayAttachmentsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayAttachmentsResponse]:
        return await self._paginate('describe_transit_gateway_attachments', request, EC2DescribeTransitGatewayAttachmentsResponse)

    async def describe_transit_gateway_connect_peers(
        self,
        request: EC2DescribeTransitGatewayConnectPeersRequest | None = None,
    ) -> EC2DescribeTransitGatewayConnectPeersResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_connect_peers, request, EC2DescribeTransitGatewayConnectPeersResponse)

    async def describe_transit_gateway_connect_peers_paginated(
        self,
        request: EC2DescribeTransitGatewayConnectPeersRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayConnectPeersResponse]:
        return await self._paginate('describe_transit_gateway_connect_peers', request, EC2DescribeTransitGatewayConnectPeersResponse)

    async def describe_transit_gateway_connects(
        self,
        request: EC2DescribeTransitGatewayConnectsRequest | None = None,
    ) -> EC2DescribeTransitGatewayConnectsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_connects, request, EC2DescribeTransitGatewayConnectsResponse)

    async def describe_transit_gateway_connects_paginated(
        self,
        request: EC2DescribeTransitGatewayConnectsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayConnectsResponse]:
        return await self._paginate('describe_transit_gateway_connects', request, EC2DescribeTransitGatewayConnectsResponse)

    async def describe_transit_gateway_metering_policies(
        self,
        request: EC2DescribeTransitGatewayMeteringPoliciesRequest | None = None,
    ) -> EC2DescribeTransitGatewayMeteringPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_metering_policies, request, EC2DescribeTransitGatewayMeteringPoliciesResponse)

    async def describe_transit_gateway_multicast_domains(
        self,
        request: EC2DescribeTransitGatewayMulticastDomainsRequest | None = None,
    ) -> EC2DescribeTransitGatewayMulticastDomainsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_multicast_domains, request, EC2DescribeTransitGatewayMulticastDomainsResponse)

    async def describe_transit_gateway_multicast_domains_paginated(
        self,
        request: EC2DescribeTransitGatewayMulticastDomainsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayMulticastDomainsResponse]:
        return await self._paginate('describe_transit_gateway_multicast_domains', request, EC2DescribeTransitGatewayMulticastDomainsResponse)

    async def describe_transit_gateway_network_function_attachments(
        self,
        request: EC2DescribeTransitGatewayNetworkFunctionAttachmentsRequest | None = None,
    ) -> EC2DescribeTransitGatewayNetworkFunctionAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_network_function_attachments, request, EC2DescribeTransitGatewayNetworkFunctionAttachmentsResponse)

    async def describe_transit_gateway_peering_attachments(
        self,
        request: EC2DescribeTransitGatewayPeeringAttachmentsRequest | None = None,
    ) -> EC2DescribeTransitGatewayPeeringAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_peering_attachments, request, EC2DescribeTransitGatewayPeeringAttachmentsResponse)

    async def describe_transit_gateway_peering_attachments_paginated(
        self,
        request: EC2DescribeTransitGatewayPeeringAttachmentsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayPeeringAttachmentsResponse]:
        return await self._paginate('describe_transit_gateway_peering_attachments', request, EC2DescribeTransitGatewayPeeringAttachmentsResponse)

    async def describe_transit_gateway_policy_tables(
        self,
        request: EC2DescribeTransitGatewayPolicyTablesRequest | None = None,
    ) -> EC2DescribeTransitGatewayPolicyTablesResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_policy_tables, request, EC2DescribeTransitGatewayPolicyTablesResponse)

    async def describe_transit_gateway_policy_tables_paginated(
        self,
        request: EC2DescribeTransitGatewayPolicyTablesRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayPolicyTablesResponse]:
        return await self._paginate('describe_transit_gateway_policy_tables', request, EC2DescribeTransitGatewayPolicyTablesResponse)

    async def describe_transit_gateway_route_table_announcements(
        self,
        request: EC2DescribeTransitGatewayRouteTableAnnouncementsRequest | None = None,
    ) -> EC2DescribeTransitGatewayRouteTableAnnouncementsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_route_table_announcements, request, EC2DescribeTransitGatewayRouteTableAnnouncementsResponse)

    async def describe_transit_gateway_route_table_announcements_paginated(
        self,
        request: EC2DescribeTransitGatewayRouteTableAnnouncementsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayRouteTableAnnouncementsResponse]:
        return await self._paginate('describe_transit_gateway_route_table_announcements', request, EC2DescribeTransitGatewayRouteTableAnnouncementsResponse)

    async def describe_transit_gateway_route_tables(
        self,
        request: EC2DescribeTransitGatewayRouteTablesRequest | None = None,
    ) -> EC2DescribeTransitGatewayRouteTablesResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_route_tables, request, EC2DescribeTransitGatewayRouteTablesResponse)

    async def describe_transit_gateway_route_tables_paginated(
        self,
        request: EC2DescribeTransitGatewayRouteTablesRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayRouteTablesResponse]:
        return await self._paginate('describe_transit_gateway_route_tables', request, EC2DescribeTransitGatewayRouteTablesResponse)

    async def describe_transit_gateway_vpc_attachments(
        self,
        request: EC2DescribeTransitGatewayVpcAttachmentsRequest | None = None,
    ) -> EC2DescribeTransitGatewayVpcAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateway_vpc_attachments, request, EC2DescribeTransitGatewayVpcAttachmentsResponse)

    async def describe_transit_gateway_vpc_attachments_paginated(
        self,
        request: EC2DescribeTransitGatewayVpcAttachmentsRequest | None = None,
    ) -> list[EC2DescribeTransitGatewayVpcAttachmentsResponse]:
        return await self._paginate('describe_transit_gateway_vpc_attachments', request, EC2DescribeTransitGatewayVpcAttachmentsResponse)

    async def describe_transit_gateways(
        self,
        request: EC2DescribeTransitGatewaysRequest | None = None,
    ) -> EC2DescribeTransitGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_transit_gateways, request, EC2DescribeTransitGatewaysResponse)

    async def describe_transit_gateways_paginated(
        self,
        request: EC2DescribeTransitGatewaysRequest | None = None,
    ) -> list[EC2DescribeTransitGatewaysResponse]:
        return await self._paginate('describe_transit_gateways', request, EC2DescribeTransitGatewaysResponse)

    async def describe_trunk_interface_associations(
        self,
        request: EC2DescribeTrunkInterfaceAssociationsRequest | None = None,
    ) -> EC2DescribeTrunkInterfaceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_trunk_interface_associations, request, EC2DescribeTrunkInterfaceAssociationsResponse)

    async def describe_trunk_interface_associations_paginated(
        self,
        request: EC2DescribeTrunkInterfaceAssociationsRequest | None = None,
    ) -> list[EC2DescribeTrunkInterfaceAssociationsResponse]:
        return await self._paginate('describe_trunk_interface_associations', request, EC2DescribeTrunkInterfaceAssociationsResponse)

    async def describe_verified_access_endpoints(
        self,
        request: EC2DescribeVerifiedAccessEndpointsRequest | None = None,
    ) -> EC2DescribeVerifiedAccessEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_access_endpoints, request, EC2DescribeVerifiedAccessEndpointsResponse)

    async def describe_verified_access_endpoints_paginated(
        self,
        request: EC2DescribeVerifiedAccessEndpointsRequest | None = None,
    ) -> list[EC2DescribeVerifiedAccessEndpointsResponse]:
        return await self._paginate('describe_verified_access_endpoints', request, EC2DescribeVerifiedAccessEndpointsResponse)

    async def describe_verified_access_groups(
        self,
        request: EC2DescribeVerifiedAccessGroupsRequest | None = None,
    ) -> EC2DescribeVerifiedAccessGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_access_groups, request, EC2DescribeVerifiedAccessGroupsResponse)

    async def describe_verified_access_groups_paginated(
        self,
        request: EC2DescribeVerifiedAccessGroupsRequest | None = None,
    ) -> list[EC2DescribeVerifiedAccessGroupsResponse]:
        return await self._paginate('describe_verified_access_groups', request, EC2DescribeVerifiedAccessGroupsResponse)

    async def describe_verified_access_instance_logging_configurations(
        self,
        request: EC2DescribeVerifiedAccessInstanceLoggingConfigurationsRequest | None = None,
    ) -> EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_access_instance_logging_configurations, request, EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse)

    async def describe_verified_access_instance_logging_configurations_paginated(
        self,
        request: EC2DescribeVerifiedAccessInstanceLoggingConfigurationsRequest | None = None,
    ) -> list[EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse]:
        return await self._paginate('describe_verified_access_instance_logging_configurations', request, EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse)

    async def describe_verified_access_instances(
        self,
        request: EC2DescribeVerifiedAccessInstancesRequest | None = None,
    ) -> EC2DescribeVerifiedAccessInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_access_instances, request, EC2DescribeVerifiedAccessInstancesResponse)

    async def describe_verified_access_instances_paginated(
        self,
        request: EC2DescribeVerifiedAccessInstancesRequest | None = None,
    ) -> list[EC2DescribeVerifiedAccessInstancesResponse]:
        return await self._paginate('describe_verified_access_instances', request, EC2DescribeVerifiedAccessInstancesResponse)

    async def describe_verified_access_trust_providers(
        self,
        request: EC2DescribeVerifiedAccessTrustProvidersRequest | None = None,
    ) -> EC2DescribeVerifiedAccessTrustProvidersResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_access_trust_providers, request, EC2DescribeVerifiedAccessTrustProvidersResponse)

    async def describe_verified_access_trust_providers_paginated(
        self,
        request: EC2DescribeVerifiedAccessTrustProvidersRequest | None = None,
    ) -> list[EC2DescribeVerifiedAccessTrustProvidersResponse]:
        return await self._paginate('describe_verified_access_trust_providers', request, EC2DescribeVerifiedAccessTrustProvidersResponse)

    async def describe_volume_attribute(
        self,
        request: EC2DescribeVolumeAttributeRequest,
    ) -> EC2DescribeVolumeAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_volume_attribute, request, EC2DescribeVolumeAttributeResponse)

    async def describe_volume_status(
        self,
        request: EC2DescribeVolumeStatusRequest | None = None,
    ) -> EC2DescribeVolumeStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_volume_status, request, EC2DescribeVolumeStatusResponse)

    async def describe_volume_status_paginated(
        self,
        request: EC2DescribeVolumeStatusRequest | None = None,
    ) -> list[EC2DescribeVolumeStatusResponse]:
        return await self._paginate('describe_volume_status', request, EC2DescribeVolumeStatusResponse)

    async def describe_volumes_modifications(
        self,
        request: EC2DescribeVolumesModificationsRequest | None = None,
    ) -> EC2DescribeVolumesModificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_volumes_modifications, request, EC2DescribeVolumesModificationsResponse)

    async def describe_volumes_modifications_paginated(
        self,
        request: EC2DescribeVolumesModificationsRequest | None = None,
    ) -> list[EC2DescribeVolumesModificationsResponse]:
        return await self._paginate('describe_volumes_modifications', request, EC2DescribeVolumesModificationsResponse)

    async def describe_vpc_attribute(
        self,
        request: EC2DescribeVpcAttributeRequest,
    ) -> EC2DescribeVpcAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_attribute, request, EC2DescribeVpcAttributeResponse)

    async def describe_vpc_block_public_access_exclusions(
        self,
        request: EC2DescribeVpcBlockPublicAccessExclusionsRequest | None = None,
    ) -> EC2DescribeVpcBlockPublicAccessExclusionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_block_public_access_exclusions, request, EC2DescribeVpcBlockPublicAccessExclusionsResponse)

    async def describe_vpc_block_public_access_options(
        self,
        request: EC2DescribeVpcBlockPublicAccessOptionsRequest | None = None,
    ) -> EC2DescribeVpcBlockPublicAccessOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_block_public_access_options, request, EC2DescribeVpcBlockPublicAccessOptionsResponse)

    async def describe_vpc_classic_link(
        self,
        request: EC2DescribeVpcClassicLinkRequest | None = None,
    ) -> EC2DescribeVpcClassicLinkResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_classic_link, request, EC2DescribeVpcClassicLinkResponse)

    async def describe_vpc_classic_link_dns_support(
        self,
        request: EC2DescribeVpcClassicLinkDnsSupportRequest | None = None,
    ) -> EC2DescribeVpcClassicLinkDnsSupportResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_classic_link_dns_support, request, EC2DescribeVpcClassicLinkDnsSupportResponse)

    async def describe_vpc_classic_link_dns_support_paginated(
        self,
        request: EC2DescribeVpcClassicLinkDnsSupportRequest | None = None,
    ) -> list[EC2DescribeVpcClassicLinkDnsSupportResponse]:
        return await self._paginate('describe_vpc_classic_link_dns_support', request, EC2DescribeVpcClassicLinkDnsSupportResponse)

    async def describe_vpc_encryption_controls(
        self,
        request: EC2DescribeVpcEncryptionControlsRequest | None = None,
    ) -> EC2DescribeVpcEncryptionControlsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_encryption_controls, request, EC2DescribeVpcEncryptionControlsResponse)

    async def describe_vpc_endpoint_associations(
        self,
        request: EC2DescribeVpcEndpointAssociationsRequest | None = None,
    ) -> EC2DescribeVpcEndpointAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_associations, request, EC2DescribeVpcEndpointAssociationsResponse)

    async def describe_vpc_endpoint_connection_notifications(
        self,
        request: EC2DescribeVpcEndpointConnectionNotificationsRequest | None = None,
    ) -> EC2DescribeVpcEndpointConnectionNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_connection_notifications, request, EC2DescribeVpcEndpointConnectionNotificationsResponse)

    async def describe_vpc_endpoint_connection_notifications_paginated(
        self,
        request: EC2DescribeVpcEndpointConnectionNotificationsRequest | None = None,
    ) -> list[EC2DescribeVpcEndpointConnectionNotificationsResponse]:
        return await self._paginate('describe_vpc_endpoint_connection_notifications', request, EC2DescribeVpcEndpointConnectionNotificationsResponse)

    async def describe_vpc_endpoint_connections(
        self,
        request: EC2DescribeVpcEndpointConnectionsRequest | None = None,
    ) -> EC2DescribeVpcEndpointConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_connections, request, EC2DescribeVpcEndpointConnectionsResponse)

    async def describe_vpc_endpoint_connections_paginated(
        self,
        request: EC2DescribeVpcEndpointConnectionsRequest | None = None,
    ) -> list[EC2DescribeVpcEndpointConnectionsResponse]:
        return await self._paginate('describe_vpc_endpoint_connections', request, EC2DescribeVpcEndpointConnectionsResponse)

    async def describe_vpc_endpoint_service_configurations(
        self,
        request: EC2DescribeVpcEndpointServiceConfigurationsRequest | None = None,
    ) -> EC2DescribeVpcEndpointServiceConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_service_configurations, request, EC2DescribeVpcEndpointServiceConfigurationsResponse)

    async def describe_vpc_endpoint_service_configurations_paginated(
        self,
        request: EC2DescribeVpcEndpointServiceConfigurationsRequest | None = None,
    ) -> list[EC2DescribeVpcEndpointServiceConfigurationsResponse]:
        return await self._paginate('describe_vpc_endpoint_service_configurations', request, EC2DescribeVpcEndpointServiceConfigurationsResponse)

    async def describe_vpc_endpoint_service_permissions(
        self,
        request: EC2DescribeVpcEndpointServicePermissionsRequest,
    ) -> EC2DescribeVpcEndpointServicePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_service_permissions, request, EC2DescribeVpcEndpointServicePermissionsResponse)

    async def describe_vpc_endpoint_service_permissions_paginated(
        self,
        request: EC2DescribeVpcEndpointServicePermissionsRequest,
    ) -> list[EC2DescribeVpcEndpointServicePermissionsResponse]:
        return await self._paginate('describe_vpc_endpoint_service_permissions', request, EC2DescribeVpcEndpointServicePermissionsResponse)

    async def describe_vpc_endpoint_services(
        self,
        request: EC2DescribeVpcEndpointServicesRequest | None = None,
    ) -> EC2DescribeVpcEndpointServicesResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoint_services, request, EC2DescribeVpcEndpointServicesResponse)

    async def describe_vpc_endpoint_services_paginated(
        self,
        request: EC2DescribeVpcEndpointServicesRequest | None = None,
    ) -> list[EC2DescribeVpcEndpointServicesResponse]:
        return await self._paginate('describe_vpc_endpoint_services', request, EC2DescribeVpcEndpointServicesResponse)

    async def describe_vpc_endpoints(
        self,
        request: EC2DescribeVpcEndpointsRequest | None = None,
    ) -> EC2DescribeVpcEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoints, request, EC2DescribeVpcEndpointsResponse)

    async def describe_vpc_endpoints_paginated(
        self,
        request: EC2DescribeVpcEndpointsRequest | None = None,
    ) -> list[EC2DescribeVpcEndpointsResponse]:
        return await self._paginate('describe_vpc_endpoints', request, EC2DescribeVpcEndpointsResponse)

    async def describe_vpc_peering_connections(
        self,
        request: EC2DescribeVpcPeeringConnectionsRequest | None = None,
    ) -> EC2DescribeVpcPeeringConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_peering_connections, request, EC2DescribeVpcPeeringConnectionsResponse)

    async def describe_vpc_peering_connections_paginated(
        self,
        request: EC2DescribeVpcPeeringConnectionsRequest | None = None,
    ) -> list[EC2DescribeVpcPeeringConnectionsResponse]:
        return await self._paginate('describe_vpc_peering_connections', request, EC2DescribeVpcPeeringConnectionsResponse)

    async def describe_vpn_concentrators(
        self,
        request: EC2DescribeVpnConcentratorsRequest | None = None,
    ) -> EC2DescribeVpnConcentratorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpn_concentrators, request, EC2DescribeVpnConcentratorsResponse)

    async def describe_vpn_concentrators_paginated(
        self,
        request: EC2DescribeVpnConcentratorsRequest | None = None,
    ) -> list[EC2DescribeVpnConcentratorsResponse]:
        return await self._paginate('describe_vpn_concentrators', request, EC2DescribeVpnConcentratorsResponse)

    async def describe_vpn_connections(
        self,
        request: EC2DescribeVpnConnectionsRequest | None = None,
    ) -> EC2DescribeVpnConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpn_connections, request, EC2DescribeVpnConnectionsResponse)

    async def describe_vpn_gateways(
        self,
        request: EC2DescribeVpnGatewaysRequest | None = None,
    ) -> EC2DescribeVpnGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpn_gateways, request, EC2DescribeVpnGatewaysResponse)

    async def detach_classic_link_vpc(
        self,
        request: EC2DetachClassicLinkVpcRequest,
    ) -> EC2DetachClassicLinkVpcResponse:
        client = self._require_client()
        return await self._execute(client.detach_classic_link_vpc, request, EC2DetachClassicLinkVpcResponse)

    async def detach_image_watermark(
        self,
        request: EC2DetachImageWatermarkRequest,
    ) -> EC2DetachImageWatermarkResponse:
        client = self._require_client()
        return await self._execute(client.detach_image_watermark, request, EC2DetachImageWatermarkResponse)

    async def detach_internet_gateway(
        self,
        request: EC2DetachInternetGatewayRequest,
    ) -> EC2DetachInternetGatewayResponse:
        client = self._require_client()
        return await self._execute(client.detach_internet_gateway, request, EC2DetachInternetGatewayResponse)

    async def detach_network_interface(
        self,
        request: EC2DetachNetworkInterfaceRequest,
    ) -> EC2DetachNetworkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.detach_network_interface, request, EC2DetachNetworkInterfaceResponse)

    async def detach_verified_access_trust_provider(
        self,
        request: EC2DetachVerifiedAccessTrustProviderRequest,
    ) -> EC2DetachVerifiedAccessTrustProviderResponse:
        client = self._require_client()
        return await self._execute(client.detach_verified_access_trust_provider, request, EC2DetachVerifiedAccessTrustProviderResponse)

    async def detach_vpn_gateway(
        self,
        request: EC2DetachVpnGatewayRequest,
    ) -> EC2DetachVpnGatewayResponse:
        client = self._require_client()
        return await self._execute(client.detach_vpn_gateway, request, EC2DetachVpnGatewayResponse)

    async def disable_address_transfer(
        self,
        request: EC2DisableAddressTransferRequest,
    ) -> EC2DisableAddressTransferResponse:
        client = self._require_client()
        return await self._execute(client.disable_address_transfer, request, EC2DisableAddressTransferResponse)

    async def disable_allowed_images_settings(
        self,
        request: EC2DisableAllowedImagesSettingsRequest | None = None,
    ) -> EC2DisableAllowedImagesSettingsResponse:
        client = self._require_client()
        return await self._execute(client.disable_allowed_images_settings, request, EC2DisableAllowedImagesSettingsResponse)

    async def disable_application_status_check_suppression(
        self,
        request: EC2DisableApplicationStatusCheckSuppressionRequest | None = None,
    ) -> EC2DisableApplicationStatusCheckSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.disable_application_status_check_suppression, request, EC2DisableApplicationStatusCheckSuppressionResponse)

    async def disable_aws_network_performance_metric_subscription(
        self,
        request: EC2DisableAwsNetworkPerformanceMetricSubscriptionRequest | None = None,
    ) -> EC2DisableAwsNetworkPerformanceMetricSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.disable_aws_network_performance_metric_subscription, request, EC2DisableAwsNetworkPerformanceMetricSubscriptionResponse)

    async def disable_capacity_manager(
        self,
        request: EC2DisableCapacityManagerRequest | None = None,
    ) -> EC2DisableCapacityManagerResponse:
        client = self._require_client()
        return await self._execute(client.disable_capacity_manager, request, EC2DisableCapacityManagerResponse)

    async def disable_ebs_encryption_by_default(
        self,
        request: EC2DisableEbsEncryptionByDefaultRequest | None = None,
    ) -> EC2DisableEbsEncryptionByDefaultResponse:
        client = self._require_client()
        return await self._execute(client.disable_ebs_encryption_by_default, request, EC2DisableEbsEncryptionByDefaultResponse)

    async def disable_fast_launch(
        self,
        request: EC2DisableFastLaunchRequest,
    ) -> EC2DisableFastLaunchResponse:
        client = self._require_client()
        return await self._execute(client.disable_fast_launch, request, EC2DisableFastLaunchResponse)

    async def disable_fast_snapshot_restores(
        self,
        request: EC2DisableFastSnapshotRestoresRequest,
    ) -> EC2DisableFastSnapshotRestoresResponse:
        client = self._require_client()
        return await self._execute(client.disable_fast_snapshot_restores, request, EC2DisableFastSnapshotRestoresResponse)

    async def disable_image(
        self,
        request: EC2DisableImageRequest,
    ) -> EC2DisableImageResponse:
        client = self._require_client()
        return await self._execute(client.disable_image, request, EC2DisableImageResponse)

    async def disable_image_block_public_access(
        self,
        request: EC2DisableImageBlockPublicAccessRequest | None = None,
    ) -> EC2DisableImageBlockPublicAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_image_block_public_access, request, EC2DisableImageBlockPublicAccessResponse)

    async def disable_image_deprecation(
        self,
        request: EC2DisableImageDeprecationRequest,
    ) -> EC2DisableImageDeprecationResponse:
        client = self._require_client()
        return await self._execute(client.disable_image_deprecation, request, EC2DisableImageDeprecationResponse)

    async def disable_image_deregistration_protection(
        self,
        request: EC2DisableImageDeregistrationProtectionRequest,
    ) -> EC2DisableImageDeregistrationProtectionResponse:
        client = self._require_client()
        return await self._execute(client.disable_image_deregistration_protection, request, EC2DisableImageDeregistrationProtectionResponse)

    async def disable_instance_sql_ha_standby_detections(
        self,
        request: EC2DisableInstanceSqlHaStandbyDetectionsRequest,
    ) -> EC2DisableInstanceSqlHaStandbyDetectionsResponse:
        client = self._require_client()
        return await self._execute(client.disable_instance_sql_ha_standby_detections, request, EC2DisableInstanceSqlHaStandbyDetectionsResponse)

    async def disable_ipam_organization_admin_account(
        self,
        request: EC2DisableIpamOrganizationAdminAccountRequest,
    ) -> EC2DisableIpamOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disable_ipam_organization_admin_account, request, EC2DisableIpamOrganizationAdminAccountResponse)

    async def disable_ipam_policy(
        self,
        request: EC2DisableIpamPolicyRequest,
    ) -> EC2DisableIpamPolicyResponse:
        client = self._require_client()
        return await self._execute(client.disable_ipam_policy, request, EC2DisableIpamPolicyResponse)

    async def disable_route_server_propagation(
        self,
        request: EC2DisableRouteServerPropagationRequest,
    ) -> EC2DisableRouteServerPropagationResponse:
        client = self._require_client()
        return await self._execute(client.disable_route_server_propagation, request, EC2DisableRouteServerPropagationResponse)

    async def disable_serial_console_access(
        self,
        request: EC2DisableSerialConsoleAccessRequest | None = None,
    ) -> EC2DisableSerialConsoleAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_serial_console_access, request, EC2DisableSerialConsoleAccessResponse)

    async def disable_snapshot_block_public_access(
        self,
        request: EC2DisableSnapshotBlockPublicAccessRequest | None = None,
    ) -> EC2DisableSnapshotBlockPublicAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_snapshot_block_public_access, request, EC2DisableSnapshotBlockPublicAccessResponse)

    async def disable_transit_gateway_route_table_propagation(
        self,
        request: EC2DisableTransitGatewayRouteTablePropagationRequest,
    ) -> EC2DisableTransitGatewayRouteTablePropagationResponse:
        client = self._require_client()
        return await self._execute(client.disable_transit_gateway_route_table_propagation, request, EC2DisableTransitGatewayRouteTablePropagationResponse)

    async def disable_vgw_route_propagation(
        self,
        request: EC2DisableVgwRoutePropagationRequest,
    ) -> EC2DisableVgwRoutePropagationResponse:
        client = self._require_client()
        return await self._execute(client.disable_vgw_route_propagation, request, EC2DisableVgwRoutePropagationResponse)

    async def disable_vpc_classic_link(
        self,
        request: EC2DisableVpcClassicLinkRequest,
    ) -> EC2DisableVpcClassicLinkResponse:
        client = self._require_client()
        return await self._execute(client.disable_vpc_classic_link, request, EC2DisableVpcClassicLinkResponse)

    async def disable_vpc_classic_link_dns_support(
        self,
        request: EC2DisableVpcClassicLinkDnsSupportRequest | None = None,
    ) -> EC2DisableVpcClassicLinkDnsSupportResponse:
        client = self._require_client()
        return await self._execute(client.disable_vpc_classic_link_dns_support, request, EC2DisableVpcClassicLinkDnsSupportResponse)

    async def disassociate_address(
        self,
        request: EC2DisassociateAddressRequest | None = None,
    ) -> EC2DisassociateAddressResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_address, request, EC2DisassociateAddressResponse)

    async def disassociate_application_status_check(
        self,
        request: EC2DisassociateApplicationStatusCheckRequest,
    ) -> EC2DisassociateApplicationStatusCheckResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_application_status_check, request, EC2DisassociateApplicationStatusCheckResponse)

    async def disassociate_capacity_reservation_billing_owner(
        self,
        request: EC2DisassociateCapacityReservationBillingOwnerRequest,
    ) -> EC2DisassociateCapacityReservationBillingOwnerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_capacity_reservation_billing_owner, request, EC2DisassociateCapacityReservationBillingOwnerResponse)

    async def disassociate_client_vpn_target_network(
        self,
        request: EC2DisassociateClientVpnTargetNetworkRequest,
    ) -> EC2DisassociateClientVpnTargetNetworkResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_client_vpn_target_network, request, EC2DisassociateClientVpnTargetNetworkResponse)

    async def disassociate_enclave_certificate_iam_role(
        self,
        request: EC2DisassociateEnclaveCertificateIamRoleRequest,
    ) -> EC2DisassociateEnclaveCertificateIamRoleResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_enclave_certificate_iam_role, request, EC2DisassociateEnclaveCertificateIamRoleResponse)

    async def disassociate_iam_instance_profile(
        self,
        request: EC2DisassociateIamInstanceProfileRequest,
    ) -> EC2DisassociateIamInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_iam_instance_profile, request, EC2DisassociateIamInstanceProfileResponse)

    async def disassociate_instance_event_window(
        self,
        request: EC2DisassociateInstanceEventWindowRequest,
    ) -> EC2DisassociateInstanceEventWindowResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_instance_event_window, request, EC2DisassociateInstanceEventWindowResponse)

    async def disassociate_ipam_byoasn(
        self,
        request: EC2DisassociateIpamByoasnRequest,
    ) -> EC2DisassociateIpamByoasnResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_ipam_byoasn, request, EC2DisassociateIpamByoasnResponse)

    async def disassociate_ipam_resource_discovery(
        self,
        request: EC2DisassociateIpamResourceDiscoveryRequest,
    ) -> EC2DisassociateIpamResourceDiscoveryResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_ipam_resource_discovery, request, EC2DisassociateIpamResourceDiscoveryResponse)

    async def disassociate_kms_key_id(
        self,
        request: EC2DisassociateKmsKeyIdRequest,
    ) -> EC2DisassociateKmsKeyIdResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_kms_key_id, request, EC2DisassociateKmsKeyIdResponse)

    async def disassociate_nat_gateway_address(
        self,
        request: EC2DisassociateNatGatewayAddressRequest,
    ) -> EC2DisassociateNatGatewayAddressResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_nat_gateway_address, request, EC2DisassociateNatGatewayAddressResponse)

    async def disassociate_networking_flex_cost_allocation_policy(
        self,
        request: EC2DisassociateNetworkingFlexCostAllocationPolicyRequest,
    ) -> EC2DisassociateNetworkingFlexCostAllocationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_networking_flex_cost_allocation_policy, request, EC2DisassociateNetworkingFlexCostAllocationPolicyResponse)

    async def disassociate_route_server(
        self,
        request: EC2DisassociateRouteServerRequest,
    ) -> EC2DisassociateRouteServerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_route_server, request, EC2DisassociateRouteServerResponse)

    async def disassociate_route_table(
        self,
        request: EC2DisassociateRouteTableRequest,
    ) -> EC2DisassociateRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_route_table, request, EC2DisassociateRouteTableResponse)

    async def disassociate_security_group_vpc(
        self,
        request: EC2DisassociateSecurityGroupVpcRequest,
    ) -> EC2DisassociateSecurityGroupVpcResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_security_group_vpc, request, EC2DisassociateSecurityGroupVpcResponse)

    async def disassociate_subnet_cidr_block(
        self,
        request: EC2DisassociateSubnetCidrBlockRequest,
    ) -> EC2DisassociateSubnetCidrBlockResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_subnet_cidr_block, request, EC2DisassociateSubnetCidrBlockResponse)

    async def disassociate_transit_gateway_multicast_domain(
        self,
        request: EC2DisassociateTransitGatewayMulticastDomainRequest,
    ) -> EC2DisassociateTransitGatewayMulticastDomainResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_transit_gateway_multicast_domain, request, EC2DisassociateTransitGatewayMulticastDomainResponse)

    async def disassociate_transit_gateway_policy_table(
        self,
        request: EC2DisassociateTransitGatewayPolicyTableRequest,
    ) -> EC2DisassociateTransitGatewayPolicyTableResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_transit_gateway_policy_table, request, EC2DisassociateTransitGatewayPolicyTableResponse)

    async def disassociate_transit_gateway_route_table(
        self,
        request: EC2DisassociateTransitGatewayRouteTableRequest,
    ) -> EC2DisassociateTransitGatewayRouteTableResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_transit_gateway_route_table, request, EC2DisassociateTransitGatewayRouteTableResponse)

    async def disassociate_trunk_interface(
        self,
        request: EC2DisassociateTrunkInterfaceRequest,
    ) -> EC2DisassociateTrunkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_trunk_interface, request, EC2DisassociateTrunkInterfaceResponse)

    async def disassociate_vpc_cidr_block(
        self,
        request: EC2DisassociateVpcCidrBlockRequest,
    ) -> EC2DisassociateVpcCidrBlockResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_vpc_cidr_block, request, EC2DisassociateVpcCidrBlockResponse)

    async def enable_address_transfer(
        self,
        request: EC2EnableAddressTransferRequest,
    ) -> EC2EnableAddressTransferResponse:
        client = self._require_client()
        return await self._execute(client.enable_address_transfer, request, EC2EnableAddressTransferResponse)

    async def enable_allowed_images_settings(
        self,
        request: EC2EnableAllowedImagesSettingsRequest,
    ) -> EC2EnableAllowedImagesSettingsResponse:
        client = self._require_client()
        return await self._execute(client.enable_allowed_images_settings, request, EC2EnableAllowedImagesSettingsResponse)

    async def enable_application_status_check_suppression(
        self,
        request: EC2EnableApplicationStatusCheckSuppressionRequest | None = None,
    ) -> EC2EnableApplicationStatusCheckSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.enable_application_status_check_suppression, request, EC2EnableApplicationStatusCheckSuppressionResponse)

    async def enable_aws_network_performance_metric_subscription(
        self,
        request: EC2EnableAwsNetworkPerformanceMetricSubscriptionRequest | None = None,
    ) -> EC2EnableAwsNetworkPerformanceMetricSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.enable_aws_network_performance_metric_subscription, request, EC2EnableAwsNetworkPerformanceMetricSubscriptionResponse)

    async def enable_capacity_manager(
        self,
        request: EC2EnableCapacityManagerRequest | None = None,
    ) -> EC2EnableCapacityManagerResponse:
        client = self._require_client()
        return await self._execute(client.enable_capacity_manager, request, EC2EnableCapacityManagerResponse)

    async def enable_ebs_encryption_by_default(
        self,
        request: EC2EnableEbsEncryptionByDefaultRequest | None = None,
    ) -> EC2EnableEbsEncryptionByDefaultResponse:
        client = self._require_client()
        return await self._execute(client.enable_ebs_encryption_by_default, request, EC2EnableEbsEncryptionByDefaultResponse)

    async def enable_fast_launch(
        self,
        request: EC2EnableFastLaunchRequest,
    ) -> EC2EnableFastLaunchResponse:
        client = self._require_client()
        return await self._execute(client.enable_fast_launch, request, EC2EnableFastLaunchResponse)

    async def enable_fast_snapshot_restores(
        self,
        request: EC2EnableFastSnapshotRestoresRequest,
    ) -> EC2EnableFastSnapshotRestoresResponse:
        client = self._require_client()
        return await self._execute(client.enable_fast_snapshot_restores, request, EC2EnableFastSnapshotRestoresResponse)

    async def enable_image(
        self,
        request: EC2EnableImageRequest,
    ) -> EC2EnableImageResponse:
        client = self._require_client()
        return await self._execute(client.enable_image, request, EC2EnableImageResponse)

    async def enable_image_block_public_access(
        self,
        request: EC2EnableImageBlockPublicAccessRequest,
    ) -> EC2EnableImageBlockPublicAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_image_block_public_access, request, EC2EnableImageBlockPublicAccessResponse)

    async def enable_image_deprecation(
        self,
        request: EC2EnableImageDeprecationRequest,
    ) -> EC2EnableImageDeprecationResponse:
        client = self._require_client()
        return await self._execute(client.enable_image_deprecation, request, EC2EnableImageDeprecationResponse)

    async def enable_image_deregistration_protection(
        self,
        request: EC2EnableImageDeregistrationProtectionRequest,
    ) -> EC2EnableImageDeregistrationProtectionResponse:
        client = self._require_client()
        return await self._execute(client.enable_image_deregistration_protection, request, EC2EnableImageDeregistrationProtectionResponse)

    async def enable_instance_sql_ha_standby_detections(
        self,
        request: EC2EnableInstanceSqlHaStandbyDetectionsRequest,
    ) -> EC2EnableInstanceSqlHaStandbyDetectionsResponse:
        client = self._require_client()
        return await self._execute(client.enable_instance_sql_ha_standby_detections, request, EC2EnableInstanceSqlHaStandbyDetectionsResponse)

    async def enable_ipam_internet_registry_association(
        self,
        request: EC2EnableIpamInternetRegistryAssociationRequest,
    ) -> EC2EnableIpamInternetRegistryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.enable_ipam_internet_registry_association, request, EC2EnableIpamInternetRegistryAssociationResponse)

    async def enable_ipam_organization_admin_account(
        self,
        request: EC2EnableIpamOrganizationAdminAccountRequest,
    ) -> EC2EnableIpamOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.enable_ipam_organization_admin_account, request, EC2EnableIpamOrganizationAdminAccountResponse)

    async def enable_ipam_policy(
        self,
        request: EC2EnableIpamPolicyRequest,
    ) -> EC2EnableIpamPolicyResponse:
        client = self._require_client()
        return await self._execute(client.enable_ipam_policy, request, EC2EnableIpamPolicyResponse)

    async def enable_reachability_analyzer_organization_sharing(
        self,
        request: EC2EnableReachabilityAnalyzerOrganizationSharingRequest | None = None,
    ) -> EC2EnableReachabilityAnalyzerOrganizationSharingResponse:
        client = self._require_client()
        return await self._execute(client.enable_reachability_analyzer_organization_sharing, request, EC2EnableReachabilityAnalyzerOrganizationSharingResponse)

    async def enable_route_server_propagation(
        self,
        request: EC2EnableRouteServerPropagationRequest,
    ) -> EC2EnableRouteServerPropagationResponse:
        client = self._require_client()
        return await self._execute(client.enable_route_server_propagation, request, EC2EnableRouteServerPropagationResponse)

    async def enable_serial_console_access(
        self,
        request: EC2EnableSerialConsoleAccessRequest | None = None,
    ) -> EC2EnableSerialConsoleAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_serial_console_access, request, EC2EnableSerialConsoleAccessResponse)

    async def enable_snapshot_block_public_access(
        self,
        request: EC2EnableSnapshotBlockPublicAccessRequest,
    ) -> EC2EnableSnapshotBlockPublicAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_snapshot_block_public_access, request, EC2EnableSnapshotBlockPublicAccessResponse)

    async def enable_transit_gateway_route_table_propagation(
        self,
        request: EC2EnableTransitGatewayRouteTablePropagationRequest,
    ) -> EC2EnableTransitGatewayRouteTablePropagationResponse:
        client = self._require_client()
        return await self._execute(client.enable_transit_gateway_route_table_propagation, request, EC2EnableTransitGatewayRouteTablePropagationResponse)

    async def enable_vgw_route_propagation(
        self,
        request: EC2EnableVgwRoutePropagationRequest,
    ) -> EC2EnableVgwRoutePropagationResponse:
        client = self._require_client()
        return await self._execute(client.enable_vgw_route_propagation, request, EC2EnableVgwRoutePropagationResponse)

    async def enable_volume_io(
        self,
        request: EC2EnableVolumeIORequest,
    ) -> EC2EnableVolumeIOResponse:
        client = self._require_client()
        return await self._execute(client.enable_volume_io, request, EC2EnableVolumeIOResponse)

    async def enable_vpc_classic_link(
        self,
        request: EC2EnableVpcClassicLinkRequest,
    ) -> EC2EnableVpcClassicLinkResponse:
        client = self._require_client()
        return await self._execute(client.enable_vpc_classic_link, request, EC2EnableVpcClassicLinkResponse)

    async def enable_vpc_classic_link_dns_support(
        self,
        request: EC2EnableVpcClassicLinkDnsSupportRequest | None = None,
    ) -> EC2EnableVpcClassicLinkDnsSupportResponse:
        client = self._require_client()
        return await self._execute(client.enable_vpc_classic_link_dns_support, request, EC2EnableVpcClassicLinkDnsSupportResponse)

    async def export_client_vpn_client_certificate_revocation_list(
        self,
        request: EC2ExportClientVpnClientCertificateRevocationListRequest,
    ) -> EC2ExportClientVpnClientCertificateRevocationListResponse:
        client = self._require_client()
        return await self._execute(client.export_client_vpn_client_certificate_revocation_list, request, EC2ExportClientVpnClientCertificateRevocationListResponse)

    async def export_client_vpn_client_configuration(
        self,
        request: EC2ExportClientVpnClientConfigurationRequest,
    ) -> EC2ExportClientVpnClientConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.export_client_vpn_client_configuration, request, EC2ExportClientVpnClientConfigurationResponse)

    async def export_image(
        self,
        request: EC2ExportImageRequest,
    ) -> EC2ExportImageResponse:
        client = self._require_client()
        return await self._execute(client.export_image, request, EC2ExportImageResponse)

    async def export_transit_gateway_routes(
        self,
        request: EC2ExportTransitGatewayRoutesRequest,
    ) -> EC2ExportTransitGatewayRoutesResponse:
        client = self._require_client()
        return await self._execute(client.export_transit_gateway_routes, request, EC2ExportTransitGatewayRoutesResponse)

    async def export_verified_access_instance_client_configuration(
        self,
        request: EC2ExportVerifiedAccessInstanceClientConfigurationRequest,
    ) -> EC2ExportVerifiedAccessInstanceClientConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.export_verified_access_instance_client_configuration, request, EC2ExportVerifiedAccessInstanceClientConfigurationResponse)

    async def get_active_vpn_tunnel_status(
        self,
        request: EC2GetActiveVpnTunnelStatusRequest,
    ) -> EC2GetActiveVpnTunnelStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_active_vpn_tunnel_status, request, EC2GetActiveVpnTunnelStatusResponse)

    async def get_allowed_images_settings(
        self,
        request: EC2GetAllowedImagesSettingsRequest | None = None,
    ) -> EC2GetAllowedImagesSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_allowed_images_settings, request, EC2GetAllowedImagesSettingsResponse)

    async def get_associated_enclave_certificate_iam_roles(
        self,
        request: EC2GetAssociatedEnclaveCertificateIamRolesRequest,
    ) -> EC2GetAssociatedEnclaveCertificateIamRolesResponse:
        client = self._require_client()
        return await self._execute(client.get_associated_enclave_certificate_iam_roles, request, EC2GetAssociatedEnclaveCertificateIamRolesResponse)

    async def get_associated_ipv6_pool_cidrs(
        self,
        request: EC2GetAssociatedIpv6PoolCidrsRequest,
    ) -> EC2GetAssociatedIpv6PoolCidrsResponse:
        client = self._require_client()
        return await self._execute(client.get_associated_ipv6_pool_cidrs, request, EC2GetAssociatedIpv6PoolCidrsResponse)

    async def get_associated_ipv6_pool_cidrs_paginated(
        self,
        request: EC2GetAssociatedIpv6PoolCidrsRequest,
    ) -> list[EC2GetAssociatedIpv6PoolCidrsResponse]:
        return await self._paginate('get_associated_ipv6_pool_cidrs', request, EC2GetAssociatedIpv6PoolCidrsResponse)

    async def get_aws_network_performance_data(
        self,
        request: EC2GetAwsNetworkPerformanceDataRequest | None = None,
    ) -> EC2GetAwsNetworkPerformanceDataResponse:
        client = self._require_client()
        return await self._execute(client.get_aws_network_performance_data, request, EC2GetAwsNetworkPerformanceDataResponse)

    async def get_aws_network_performance_data_paginated(
        self,
        request: EC2GetAwsNetworkPerformanceDataRequest | None = None,
    ) -> list[EC2GetAwsNetworkPerformanceDataResponse]:
        return await self._paginate('get_aws_network_performance_data', request, EC2GetAwsNetworkPerformanceDataResponse)

    async def get_capacity_manager_attributes(
        self,
        request: EC2GetCapacityManagerAttributesRequest | None = None,
    ) -> EC2GetCapacityManagerAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_manager_attributes, request, EC2GetCapacityManagerAttributesResponse)

    async def get_capacity_manager_metric_data(
        self,
        request: EC2GetCapacityManagerMetricDataRequest,
    ) -> EC2GetCapacityManagerMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_manager_metric_data, request, EC2GetCapacityManagerMetricDataResponse)

    async def get_capacity_manager_metric_data_paginated(
        self,
        request: EC2GetCapacityManagerMetricDataRequest,
    ) -> list[EC2GetCapacityManagerMetricDataResponse]:
        return await self._paginate('get_capacity_manager_metric_data', request, EC2GetCapacityManagerMetricDataResponse)

    async def get_capacity_manager_metric_dimensions(
        self,
        request: EC2GetCapacityManagerMetricDimensionsRequest,
    ) -> EC2GetCapacityManagerMetricDimensionsResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_manager_metric_dimensions, request, EC2GetCapacityManagerMetricDimensionsResponse)

    async def get_capacity_manager_metric_dimensions_paginated(
        self,
        request: EC2GetCapacityManagerMetricDimensionsRequest,
    ) -> list[EC2GetCapacityManagerMetricDimensionsResponse]:
        return await self._paginate('get_capacity_manager_metric_dimensions', request, EC2GetCapacityManagerMetricDimensionsResponse)

    async def get_capacity_manager_monitored_tag_keys(
        self,
        request: EC2GetCapacityManagerMonitoredTagKeysRequest | None = None,
    ) -> EC2GetCapacityManagerMonitoredTagKeysResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_manager_monitored_tag_keys, request, EC2GetCapacityManagerMonitoredTagKeysResponse)

    async def get_capacity_manager_monitored_tag_keys_paginated(
        self,
        request: EC2GetCapacityManagerMonitoredTagKeysRequest | None = None,
    ) -> list[EC2GetCapacityManagerMonitoredTagKeysResponse]:
        return await self._paginate('get_capacity_manager_monitored_tag_keys', request, EC2GetCapacityManagerMonitoredTagKeysResponse)

    async def get_capacity_manager_supportability_scores(
        self,
        request: EC2GetCapacityManagerSupportabilityScoresRequest,
    ) -> EC2GetCapacityManagerSupportabilityScoresResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_manager_supportability_scores, request, EC2GetCapacityManagerSupportabilityScoresResponse)

    async def get_capacity_reservation_usage(
        self,
        request: EC2GetCapacityReservationUsageRequest,
    ) -> EC2GetCapacityReservationUsageResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_reservation_usage, request, EC2GetCapacityReservationUsageResponse)

    async def get_client_vpn_endpoint_authorization_policy(
        self,
        request: EC2GetClientVpnEndpointAuthorizationPolicyRequest,
    ) -> EC2GetClientVpnEndpointAuthorizationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_client_vpn_endpoint_authorization_policy, request, EC2GetClientVpnEndpointAuthorizationPolicyResponse)

    async def get_coip_pool_usage(
        self,
        request: EC2GetCoipPoolUsageRequest,
    ) -> EC2GetCoipPoolUsageResponse:
        client = self._require_client()
        return await self._execute(client.get_coip_pool_usage, request, EC2GetCoipPoolUsageResponse)

    async def get_console_output(
        self,
        request: EC2GetConsoleOutputRequest,
    ) -> EC2GetConsoleOutputResponse:
        client = self._require_client()
        return await self._execute(client.get_console_output, request, EC2GetConsoleOutputResponse)

    async def get_console_screenshot(
        self,
        request: EC2GetConsoleScreenshotRequest,
    ) -> EC2GetConsoleScreenshotResponse:
        client = self._require_client()
        return await self._execute(client.get_console_screenshot, request, EC2GetConsoleScreenshotResponse)

    async def get_declarative_policies_report_summary(
        self,
        request: EC2GetDeclarativePoliciesReportSummaryRequest,
    ) -> EC2GetDeclarativePoliciesReportSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_declarative_policies_report_summary, request, EC2GetDeclarativePoliciesReportSummaryResponse)

    async def get_default_credit_specification(
        self,
        request: EC2GetDefaultCreditSpecificationRequest,
    ) -> EC2GetDefaultCreditSpecificationResponse:
        client = self._require_client()
        return await self._execute(client.get_default_credit_specification, request, EC2GetDefaultCreditSpecificationResponse)

    async def get_ebs_default_kms_key_id(
        self,
        request: EC2GetEbsDefaultKmsKeyIdRequest | None = None,
    ) -> EC2GetEbsDefaultKmsKeyIdResponse:
        client = self._require_client()
        return await self._execute(client.get_ebs_default_kms_key_id, request, EC2GetEbsDefaultKmsKeyIdResponse)

    async def get_ebs_encryption_by_default(
        self,
        request: EC2GetEbsEncryptionByDefaultRequest | None = None,
    ) -> EC2GetEbsEncryptionByDefaultResponse:
        client = self._require_client()
        return await self._execute(client.get_ebs_encryption_by_default, request, EC2GetEbsEncryptionByDefaultResponse)

    async def get_enabled_ipam_policy(
        self,
        request: EC2GetEnabledIpamPolicyRequest | None = None,
    ) -> EC2GetEnabledIpamPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_enabled_ipam_policy, request, EC2GetEnabledIpamPolicyResponse)

    async def get_flow_logs_integration_template(
        self,
        request: EC2GetFlowLogsIntegrationTemplateRequest,
    ) -> EC2GetFlowLogsIntegrationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_flow_logs_integration_template, request, EC2GetFlowLogsIntegrationTemplateResponse)

    async def get_groups_for_capacity_reservation(
        self,
        request: EC2GetGroupsForCapacityReservationRequest,
    ) -> EC2GetGroupsForCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.get_groups_for_capacity_reservation, request, EC2GetGroupsForCapacityReservationResponse)

    async def get_groups_for_capacity_reservation_paginated(
        self,
        request: EC2GetGroupsForCapacityReservationRequest,
    ) -> list[EC2GetGroupsForCapacityReservationResponse]:
        return await self._paginate('get_groups_for_capacity_reservation', request, EC2GetGroupsForCapacityReservationResponse)

    async def get_host_reservation_purchase_preview(
        self,
        request: EC2GetHostReservationPurchasePreviewRequest,
    ) -> EC2GetHostReservationPurchasePreviewResponse:
        client = self._require_client()
        return await self._execute(client.get_host_reservation_purchase_preview, request, EC2GetHostReservationPurchasePreviewResponse)

    async def get_image_ancestry(
        self,
        request: EC2GetImageAncestryRequest,
    ) -> EC2GetImageAncestryResponse:
        client = self._require_client()
        return await self._execute(client.get_image_ancestry, request, EC2GetImageAncestryResponse)

    async def get_image_block_public_access_state(
        self,
        request: EC2GetImageBlockPublicAccessStateRequest | None = None,
    ) -> EC2GetImageBlockPublicAccessStateResponse:
        client = self._require_client()
        return await self._execute(client.get_image_block_public_access_state, request, EC2GetImageBlockPublicAccessStateResponse)

    async def get_image_findings(
        self,
        request: EC2GetImageFindingsRequest,
    ) -> EC2GetImageFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_image_findings, request, EC2GetImageFindingsResponse)

    async def get_image_findings_paginated(
        self,
        request: EC2GetImageFindingsRequest,
    ) -> list[EC2GetImageFindingsResponse]:
        return await self._paginate('get_image_findings', request, EC2GetImageFindingsResponse)

    async def get_instance_metadata_defaults(
        self,
        request: EC2GetInstanceMetadataDefaultsRequest | None = None,
    ) -> EC2GetInstanceMetadataDefaultsResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_metadata_defaults, request, EC2GetInstanceMetadataDefaultsResponse)

    async def get_instance_tpm_ek_pub(
        self,
        request: EC2GetInstanceTpmEkPubRequest,
    ) -> EC2GetInstanceTpmEkPubResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_tpm_ek_pub, request, EC2GetInstanceTpmEkPubResponse)

    async def get_instance_types_from_instance_requirements(
        self,
        request: EC2GetInstanceTypesFromInstanceRequirementsRequest,
    ) -> EC2GetInstanceTypesFromInstanceRequirementsResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_types_from_instance_requirements, request, EC2GetInstanceTypesFromInstanceRequirementsResponse)

    async def get_instance_types_from_instance_requirements_paginated(
        self,
        request: EC2GetInstanceTypesFromInstanceRequirementsRequest,
    ) -> list[EC2GetInstanceTypesFromInstanceRequirementsResponse]:
        return await self._paginate('get_instance_types_from_instance_requirements', request, EC2GetInstanceTypesFromInstanceRequirementsResponse)

    async def get_instance_uefi_data(
        self,
        request: EC2GetInstanceUefiDataRequest,
    ) -> EC2GetInstanceUefiDataResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_uefi_data, request, EC2GetInstanceUefiDataResponse)

    async def get_ipam_address_history(
        self,
        request: EC2GetIpamAddressHistoryRequest,
    ) -> EC2GetIpamAddressHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_address_history, request, EC2GetIpamAddressHistoryResponse)

    async def get_ipam_address_history_paginated(
        self,
        request: EC2GetIpamAddressHistoryRequest,
    ) -> list[EC2GetIpamAddressHistoryResponse]:
        return await self._paginate('get_ipam_address_history', request, EC2GetIpamAddressHistoryResponse)

    async def get_ipam_discovered_accounts(
        self,
        request: EC2GetIpamDiscoveredAccountsRequest,
    ) -> EC2GetIpamDiscoveredAccountsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_discovered_accounts, request, EC2GetIpamDiscoveredAccountsResponse)

    async def get_ipam_discovered_accounts_paginated(
        self,
        request: EC2GetIpamDiscoveredAccountsRequest,
    ) -> list[EC2GetIpamDiscoveredAccountsResponse]:
        return await self._paginate('get_ipam_discovered_accounts', request, EC2GetIpamDiscoveredAccountsResponse)

    async def get_ipam_discovered_public_addresses(
        self,
        request: EC2GetIpamDiscoveredPublicAddressesRequest,
    ) -> EC2GetIpamDiscoveredPublicAddressesResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_discovered_public_addresses, request, EC2GetIpamDiscoveredPublicAddressesResponse)

    async def get_ipam_discovered_resource_cidrs(
        self,
        request: EC2GetIpamDiscoveredResourceCidrsRequest,
    ) -> EC2GetIpamDiscoveredResourceCidrsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_discovered_resource_cidrs, request, EC2GetIpamDiscoveredResourceCidrsResponse)

    async def get_ipam_discovered_resource_cidrs_paginated(
        self,
        request: EC2GetIpamDiscoveredResourceCidrsRequest,
    ) -> list[EC2GetIpamDiscoveredResourceCidrsResponse]:
        return await self._paginate('get_ipam_discovered_resource_cidrs', request, EC2GetIpamDiscoveredResourceCidrsResponse)

    async def get_ipam_discovered_routes(
        self,
        request: EC2GetIpamDiscoveredRoutesRequest,
    ) -> EC2GetIpamDiscoveredRoutesResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_discovered_routes, request, EC2GetIpamDiscoveredRoutesResponse)

    async def get_ipam_internet_registry_association_asns(
        self,
        request: EC2GetIpamInternetRegistryAssociationAsnsRequest,
    ) -> EC2GetIpamInternetRegistryAssociationAsnsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_internet_registry_association_asns, request, EC2GetIpamInternetRegistryAssociationAsnsResponse)

    async def get_ipam_internet_registry_association_cidrs(
        self,
        request: EC2GetIpamInternetRegistryAssociationCidrsRequest,
    ) -> EC2GetIpamInternetRegistryAssociationCidrsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_internet_registry_association_cidrs, request, EC2GetIpamInternetRegistryAssociationCidrsResponse)

    async def get_ipam_policy_allocation_rules(
        self,
        request: EC2GetIpamPolicyAllocationRulesRequest,
    ) -> EC2GetIpamPolicyAllocationRulesResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_policy_allocation_rules, request, EC2GetIpamPolicyAllocationRulesResponse)

    async def get_ipam_policy_organization_targets(
        self,
        request: EC2GetIpamPolicyOrganizationTargetsRequest,
    ) -> EC2GetIpamPolicyOrganizationTargetsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_policy_organization_targets, request, EC2GetIpamPolicyOrganizationTargetsResponse)

    async def get_ipam_pool_allocations(
        self,
        request: EC2GetIpamPoolAllocationsRequest,
    ) -> EC2GetIpamPoolAllocationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_pool_allocations, request, EC2GetIpamPoolAllocationsResponse)

    async def get_ipam_pool_allocations_paginated(
        self,
        request: EC2GetIpamPoolAllocationsRequest,
    ) -> list[EC2GetIpamPoolAllocationsResponse]:
        return await self._paginate('get_ipam_pool_allocations', request, EC2GetIpamPoolAllocationsResponse)

    async def get_ipam_pool_cidrs(
        self,
        request: EC2GetIpamPoolCidrsRequest,
    ) -> EC2GetIpamPoolCidrsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_pool_cidrs, request, EC2GetIpamPoolCidrsResponse)

    async def get_ipam_pool_cidrs_paginated(
        self,
        request: EC2GetIpamPoolCidrsRequest,
    ) -> list[EC2GetIpamPoolCidrsResponse]:
        return await self._paginate('get_ipam_pool_cidrs', request, EC2GetIpamPoolCidrsResponse)

    async def get_ipam_prefix_list_resolver_rules(
        self,
        request: EC2GetIpamPrefixListResolverRulesRequest,
    ) -> EC2GetIpamPrefixListResolverRulesResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_prefix_list_resolver_rules, request, EC2GetIpamPrefixListResolverRulesResponse)

    async def get_ipam_prefix_list_resolver_rules_paginated(
        self,
        request: EC2GetIpamPrefixListResolverRulesRequest,
    ) -> list[EC2GetIpamPrefixListResolverRulesResponse]:
        return await self._paginate('get_ipam_prefix_list_resolver_rules', request, EC2GetIpamPrefixListResolverRulesResponse)

    async def get_ipam_prefix_list_resolver_version_entries(
        self,
        request: EC2GetIpamPrefixListResolverVersionEntriesRequest,
    ) -> EC2GetIpamPrefixListResolverVersionEntriesResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_prefix_list_resolver_version_entries, request, EC2GetIpamPrefixListResolverVersionEntriesResponse)

    async def get_ipam_prefix_list_resolver_version_entries_paginated(
        self,
        request: EC2GetIpamPrefixListResolverVersionEntriesRequest,
    ) -> list[EC2GetIpamPrefixListResolverVersionEntriesResponse]:
        return await self._paginate('get_ipam_prefix_list_resolver_version_entries', request, EC2GetIpamPrefixListResolverVersionEntriesResponse)

    async def get_ipam_prefix_list_resolver_versions(
        self,
        request: EC2GetIpamPrefixListResolverVersionsRequest,
    ) -> EC2GetIpamPrefixListResolverVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_prefix_list_resolver_versions, request, EC2GetIpamPrefixListResolverVersionsResponse)

    async def get_ipam_prefix_list_resolver_versions_paginated(
        self,
        request: EC2GetIpamPrefixListResolverVersionsRequest,
    ) -> list[EC2GetIpamPrefixListResolverVersionsResponse]:
        return await self._paginate('get_ipam_prefix_list_resolver_versions', request, EC2GetIpamPrefixListResolverVersionsResponse)

    async def get_ipam_resource_cidrs(
        self,
        request: EC2GetIpamResourceCidrsRequest,
    ) -> EC2GetIpamResourceCidrsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_resource_cidrs, request, EC2GetIpamResourceCidrsResponse)

    async def get_ipam_resource_cidrs_paginated(
        self,
        request: EC2GetIpamResourceCidrsRequest,
    ) -> list[EC2GetIpamResourceCidrsResponse]:
        return await self._paginate('get_ipam_resource_cidrs', request, EC2GetIpamResourceCidrsResponse)

    async def get_ipam_route_origin_authorizations(
        self,
        request: EC2GetIpamRouteOriginAuthorizationsRequest,
    ) -> EC2GetIpamRouteOriginAuthorizationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_route_origin_authorizations, request, EC2GetIpamRouteOriginAuthorizationsResponse)

    async def get_ipam_route_protection_findings(
        self,
        request: EC2GetIpamRouteProtectionFindingsRequest,
    ) -> EC2GetIpamRouteProtectionFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_route_protection_findings, request, EC2GetIpamRouteProtectionFindingsResponse)

    async def get_ipam_routing_policy_registration_deltas(
        self,
        request: EC2GetIpamRoutingPolicyRegistrationDeltasRequest,
    ) -> EC2GetIpamRoutingPolicyRegistrationDeltasResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_routing_policy_registration_deltas, request, EC2GetIpamRoutingPolicyRegistrationDeltasResponse)

    async def get_ipam_routing_policy_registrations(
        self,
        request: EC2GetIpamRoutingPolicyRegistrationsRequest,
    ) -> EC2GetIpamRoutingPolicyRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ipam_routing_policy_registrations, request, EC2GetIpamRoutingPolicyRegistrationsResponse)

    async def get_launch_template_data(
        self,
        request: EC2GetLaunchTemplateDataRequest,
    ) -> EC2GetLaunchTemplateDataResponse:
        client = self._require_client()
        return await self._execute(client.get_launch_template_data, request, EC2GetLaunchTemplateDataResponse)

    async def get_managed_prefix_list_associations(
        self,
        request: EC2GetManagedPrefixListAssociationsRequest,
    ) -> EC2GetManagedPrefixListAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_prefix_list_associations, request, EC2GetManagedPrefixListAssociationsResponse)

    async def get_managed_prefix_list_associations_paginated(
        self,
        request: EC2GetManagedPrefixListAssociationsRequest,
    ) -> list[EC2GetManagedPrefixListAssociationsResponse]:
        return await self._paginate('get_managed_prefix_list_associations', request, EC2GetManagedPrefixListAssociationsResponse)

    async def get_managed_prefix_list_entries(
        self,
        request: EC2GetManagedPrefixListEntriesRequest,
    ) -> EC2GetManagedPrefixListEntriesResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_prefix_list_entries, request, EC2GetManagedPrefixListEntriesResponse)

    async def get_managed_prefix_list_entries_paginated(
        self,
        request: EC2GetManagedPrefixListEntriesRequest,
    ) -> list[EC2GetManagedPrefixListEntriesResponse]:
        return await self._paginate('get_managed_prefix_list_entries', request, EC2GetManagedPrefixListEntriesResponse)

    async def get_managed_resource_visibility(
        self,
        request: EC2GetManagedResourceVisibilityRequest | None = None,
    ) -> EC2GetManagedResourceVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_resource_visibility, request, EC2GetManagedResourceVisibilityResponse)

    async def get_network_insights_access_scope_analysis_findings(
        self,
        request: EC2GetNetworkInsightsAccessScopeAnalysisFindingsRequest,
    ) -> EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_network_insights_access_scope_analysis_findings, request, EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse)

    async def get_network_insights_access_scope_analysis_findings_paginated(
        self,
        request: EC2GetNetworkInsightsAccessScopeAnalysisFindingsRequest,
    ) -> list[EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse]:
        return await self._paginate('get_network_insights_access_scope_analysis_findings', request, EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse)

    async def get_network_insights_access_scope_content(
        self,
        request: EC2GetNetworkInsightsAccessScopeContentRequest,
    ) -> EC2GetNetworkInsightsAccessScopeContentResponse:
        client = self._require_client()
        return await self._execute(client.get_network_insights_access_scope_content, request, EC2GetNetworkInsightsAccessScopeContentResponse)

    async def get_networking_flex_cost_allocation_policy_versions(
        self,
        request: EC2GetNetworkingFlexCostAllocationPolicyVersionsRequest,
    ) -> EC2GetNetworkingFlexCostAllocationPolicyVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_networking_flex_cost_allocation_policy_versions, request, EC2GetNetworkingFlexCostAllocationPolicyVersionsResponse)

    async def get_password_data(
        self,
        request: EC2GetPasswordDataRequest,
    ) -> EC2GetPasswordDataResponse:
        client = self._require_client()
        return await self._execute(client.get_password_data, request, EC2GetPasswordDataResponse)

    async def get_reserved_instances_exchange_quote(
        self,
        request: EC2GetReservedInstancesExchangeQuoteRequest,
    ) -> EC2GetReservedInstancesExchangeQuoteResponse:
        client = self._require_client()
        return await self._execute(client.get_reserved_instances_exchange_quote, request, EC2GetReservedInstancesExchangeQuoteResponse)

    async def get_route_server_associations(
        self,
        request: EC2GetRouteServerAssociationsRequest,
    ) -> EC2GetRouteServerAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_route_server_associations, request, EC2GetRouteServerAssociationsResponse)

    async def get_route_server_propagations(
        self,
        request: EC2GetRouteServerPropagationsRequest,
    ) -> EC2GetRouteServerPropagationsResponse:
        client = self._require_client()
        return await self._execute(client.get_route_server_propagations, request, EC2GetRouteServerPropagationsResponse)

    async def get_route_server_routing_database(
        self,
        request: EC2GetRouteServerRoutingDatabaseRequest,
    ) -> EC2GetRouteServerRoutingDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.get_route_server_routing_database, request, EC2GetRouteServerRoutingDatabaseResponse)

    async def get_security_groups_for_vpc(
        self,
        request: EC2GetSecurityGroupsForVpcRequest,
    ) -> EC2GetSecurityGroupsForVpcResponse:
        client = self._require_client()
        return await self._execute(client.get_security_groups_for_vpc, request, EC2GetSecurityGroupsForVpcResponse)

    async def get_security_groups_for_vpc_paginated(
        self,
        request: EC2GetSecurityGroupsForVpcRequest,
    ) -> list[EC2GetSecurityGroupsForVpcResponse]:
        return await self._paginate('get_security_groups_for_vpc', request, EC2GetSecurityGroupsForVpcResponse)

    async def get_serial_console_access_status(
        self,
        request: EC2GetSerialConsoleAccessStatusRequest | None = None,
    ) -> EC2GetSerialConsoleAccessStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_serial_console_access_status, request, EC2GetSerialConsoleAccessStatusResponse)

    async def get_snapshot_block_public_access_state(
        self,
        request: EC2GetSnapshotBlockPublicAccessStateRequest | None = None,
    ) -> EC2GetSnapshotBlockPublicAccessStateResponse:
        client = self._require_client()
        return await self._execute(client.get_snapshot_block_public_access_state, request, EC2GetSnapshotBlockPublicAccessStateResponse)

    async def get_spot_placement_scores(
        self,
        request: EC2GetSpotPlacementScoresRequest,
    ) -> EC2GetSpotPlacementScoresResponse:
        client = self._require_client()
        return await self._execute(client.get_spot_placement_scores, request, EC2GetSpotPlacementScoresResponse)

    async def get_spot_placement_scores_paginated(
        self,
        request: EC2GetSpotPlacementScoresRequest,
    ) -> list[EC2GetSpotPlacementScoresResponse]:
        return await self._paginate('get_spot_placement_scores', request, EC2GetSpotPlacementScoresResponse)

    async def get_subnet_cidr_reservations(
        self,
        request: EC2GetSubnetCidrReservationsRequest,
    ) -> EC2GetSubnetCidrReservationsResponse:
        client = self._require_client()
        return await self._execute(client.get_subnet_cidr_reservations, request, EC2GetSubnetCidrReservationsResponse)

    async def get_transit_gateway_attachment_nat_configuration(
        self,
        request: EC2GetTransitGatewayAttachmentNatConfigurationRequest,
    ) -> EC2GetTransitGatewayAttachmentNatConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_attachment_nat_configuration, request, EC2GetTransitGatewayAttachmentNatConfigurationResponse)

    async def get_transit_gateway_attachment_propagations(
        self,
        request: EC2GetTransitGatewayAttachmentPropagationsRequest,
    ) -> EC2GetTransitGatewayAttachmentPropagationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_attachment_propagations, request, EC2GetTransitGatewayAttachmentPropagationsResponse)

    async def get_transit_gateway_attachment_propagations_paginated(
        self,
        request: EC2GetTransitGatewayAttachmentPropagationsRequest,
    ) -> list[EC2GetTransitGatewayAttachmentPropagationsResponse]:
        return await self._paginate('get_transit_gateway_attachment_propagations', request, EC2GetTransitGatewayAttachmentPropagationsResponse)

    async def get_transit_gateway_metering_policy_entries(
        self,
        request: EC2GetTransitGatewayMeteringPolicyEntriesRequest,
    ) -> EC2GetTransitGatewayMeteringPolicyEntriesResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_metering_policy_entries, request, EC2GetTransitGatewayMeteringPolicyEntriesResponse)

    async def get_transit_gateway_multicast_domain_associations(
        self,
        request: EC2GetTransitGatewayMulticastDomainAssociationsRequest,
    ) -> EC2GetTransitGatewayMulticastDomainAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_multicast_domain_associations, request, EC2GetTransitGatewayMulticastDomainAssociationsResponse)

    async def get_transit_gateway_multicast_domain_associations_paginated(
        self,
        request: EC2GetTransitGatewayMulticastDomainAssociationsRequest,
    ) -> list[EC2GetTransitGatewayMulticastDomainAssociationsResponse]:
        return await self._paginate('get_transit_gateway_multicast_domain_associations', request, EC2GetTransitGatewayMulticastDomainAssociationsResponse)

    async def get_transit_gateway_policy_table_associations(
        self,
        request: EC2GetTransitGatewayPolicyTableAssociationsRequest,
    ) -> EC2GetTransitGatewayPolicyTableAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_policy_table_associations, request, EC2GetTransitGatewayPolicyTableAssociationsResponse)

    async def get_transit_gateway_policy_table_associations_paginated(
        self,
        request: EC2GetTransitGatewayPolicyTableAssociationsRequest,
    ) -> list[EC2GetTransitGatewayPolicyTableAssociationsResponse]:
        return await self._paginate('get_transit_gateway_policy_table_associations', request, EC2GetTransitGatewayPolicyTableAssociationsResponse)

    async def get_transit_gateway_policy_table_entries(
        self,
        request: EC2GetTransitGatewayPolicyTableEntriesRequest,
    ) -> EC2GetTransitGatewayPolicyTableEntriesResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_policy_table_entries, request, EC2GetTransitGatewayPolicyTableEntriesResponse)

    async def get_transit_gateway_policy_table_entries_paginated(
        self,
        request: EC2GetTransitGatewayPolicyTableEntriesRequest,
    ) -> list[EC2GetTransitGatewayPolicyTableEntriesResponse]:
        return await self._paginate('get_transit_gateway_policy_table_entries', request, EC2GetTransitGatewayPolicyTableEntriesResponse)

    async def get_transit_gateway_prefix_list_references(
        self,
        request: EC2GetTransitGatewayPrefixListReferencesRequest,
    ) -> EC2GetTransitGatewayPrefixListReferencesResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_prefix_list_references, request, EC2GetTransitGatewayPrefixListReferencesResponse)

    async def get_transit_gateway_prefix_list_references_paginated(
        self,
        request: EC2GetTransitGatewayPrefixListReferencesRequest,
    ) -> list[EC2GetTransitGatewayPrefixListReferencesResponse]:
        return await self._paginate('get_transit_gateway_prefix_list_references', request, EC2GetTransitGatewayPrefixListReferencesResponse)

    async def get_transit_gateway_route_table_associations(
        self,
        request: EC2GetTransitGatewayRouteTableAssociationsRequest,
    ) -> EC2GetTransitGatewayRouteTableAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_route_table_associations, request, EC2GetTransitGatewayRouteTableAssociationsResponse)

    async def get_transit_gateway_route_table_associations_paginated(
        self,
        request: EC2GetTransitGatewayRouteTableAssociationsRequest,
    ) -> list[EC2GetTransitGatewayRouteTableAssociationsResponse]:
        return await self._paginate('get_transit_gateway_route_table_associations', request, EC2GetTransitGatewayRouteTableAssociationsResponse)

    async def get_transit_gateway_route_table_propagations(
        self,
        request: EC2GetTransitGatewayRouteTablePropagationsRequest,
    ) -> EC2GetTransitGatewayRouteTablePropagationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_route_table_propagations, request, EC2GetTransitGatewayRouteTablePropagationsResponse)

    async def get_transit_gateway_route_table_propagations_paginated(
        self,
        request: EC2GetTransitGatewayRouteTablePropagationsRequest,
    ) -> list[EC2GetTransitGatewayRouteTablePropagationsResponse]:
        return await self._paginate('get_transit_gateway_route_table_propagations', request, EC2GetTransitGatewayRouteTablePropagationsResponse)

    async def get_verified_access_endpoint_policy(
        self,
        request: EC2GetVerifiedAccessEndpointPolicyRequest,
    ) -> EC2GetVerifiedAccessEndpointPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_verified_access_endpoint_policy, request, EC2GetVerifiedAccessEndpointPolicyResponse)

    async def get_verified_access_endpoint_targets(
        self,
        request: EC2GetVerifiedAccessEndpointTargetsRequest,
    ) -> EC2GetVerifiedAccessEndpointTargetsResponse:
        client = self._require_client()
        return await self._execute(client.get_verified_access_endpoint_targets, request, EC2GetVerifiedAccessEndpointTargetsResponse)

    async def get_verified_access_group_policy(
        self,
        request: EC2GetVerifiedAccessGroupPolicyRequest,
    ) -> EC2GetVerifiedAccessGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_verified_access_group_policy, request, EC2GetVerifiedAccessGroupPolicyResponse)

    async def get_vpc_resources_blocking_encryption_enforcement(
        self,
        request: EC2GetVpcResourcesBlockingEncryptionEnforcementRequest,
    ) -> EC2GetVpcResourcesBlockingEncryptionEnforcementResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_resources_blocking_encryption_enforcement, request, EC2GetVpcResourcesBlockingEncryptionEnforcementResponse)

    async def get_vpn_connection_device_sample_configuration(
        self,
        request: EC2GetVpnConnectionDeviceSampleConfigurationRequest,
    ) -> EC2GetVpnConnectionDeviceSampleConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_vpn_connection_device_sample_configuration, request, EC2GetVpnConnectionDeviceSampleConfigurationResponse)

    async def get_vpn_connection_device_types(
        self,
        request: EC2GetVpnConnectionDeviceTypesRequest | None = None,
    ) -> EC2GetVpnConnectionDeviceTypesResponse:
        client = self._require_client()
        return await self._execute(client.get_vpn_connection_device_types, request, EC2GetVpnConnectionDeviceTypesResponse)

    async def get_vpn_connection_device_types_paginated(
        self,
        request: EC2GetVpnConnectionDeviceTypesRequest | None = None,
    ) -> list[EC2GetVpnConnectionDeviceTypesResponse]:
        return await self._paginate('get_vpn_connection_device_types', request, EC2GetVpnConnectionDeviceTypesResponse)

    async def get_vpn_tunnel_replacement_status(
        self,
        request: EC2GetVpnTunnelReplacementStatusRequest,
    ) -> EC2GetVpnTunnelReplacementStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_vpn_tunnel_replacement_status, request, EC2GetVpnTunnelReplacementStatusResponse)

    async def import_client_vpn_client_certificate_revocation_list(
        self,
        request: EC2ImportClientVpnClientCertificateRevocationListRequest,
    ) -> EC2ImportClientVpnClientCertificateRevocationListResponse:
        client = self._require_client()
        return await self._execute(client.import_client_vpn_client_certificate_revocation_list, request, EC2ImportClientVpnClientCertificateRevocationListResponse)

    async def import_image(
        self,
        request: EC2ImportImageRequest | None = None,
    ) -> EC2ImportImageResponse:
        client = self._require_client()
        return await self._execute(client.import_image, request, EC2ImportImageResponse)

    async def import_instance(
        self,
        request: EC2ImportInstanceRequest,
    ) -> EC2ImportInstanceResponse:
        client = self._require_client()
        return await self._execute(client.import_instance, request, EC2ImportInstanceResponse)

    async def import_key_pair(
        self,
        request: EC2ImportKeyPairRequest,
    ) -> EC2ImportKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.import_key_pair, request, EC2ImportKeyPairResponse)

    async def import_snapshot(
        self,
        request: EC2ImportSnapshotRequest | None = None,
    ) -> EC2ImportSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.import_snapshot, request, EC2ImportSnapshotResponse)

    async def import_volume(
        self,
        request: EC2ImportVolumeRequest,
    ) -> EC2ImportVolumeResponse:
        client = self._require_client()
        return await self._execute(client.import_volume, request, EC2ImportVolumeResponse)

    async def list_images_in_recycle_bin(
        self,
        request: EC2ListImagesInRecycleBinRequest | None = None,
    ) -> EC2ListImagesInRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.list_images_in_recycle_bin, request, EC2ListImagesInRecycleBinResponse)

    async def list_images_in_recycle_bin_paginated(
        self,
        request: EC2ListImagesInRecycleBinRequest | None = None,
    ) -> list[EC2ListImagesInRecycleBinResponse]:
        return await self._paginate('list_images_in_recycle_bin', request, EC2ListImagesInRecycleBinResponse)

    async def list_snapshots_in_recycle_bin(
        self,
        request: EC2ListSnapshotsInRecycleBinRequest | None = None,
    ) -> EC2ListSnapshotsInRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.list_snapshots_in_recycle_bin, request, EC2ListSnapshotsInRecycleBinResponse)

    async def list_snapshots_in_recycle_bin_paginated(
        self,
        request: EC2ListSnapshotsInRecycleBinRequest | None = None,
    ) -> list[EC2ListSnapshotsInRecycleBinResponse]:
        return await self._paginate('list_snapshots_in_recycle_bin', request, EC2ListSnapshotsInRecycleBinResponse)

    async def list_volumes_in_recycle_bin(
        self,
        request: EC2ListVolumesInRecycleBinRequest | None = None,
    ) -> EC2ListVolumesInRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.list_volumes_in_recycle_bin, request, EC2ListVolumesInRecycleBinResponse)

    async def lock_snapshot(
        self,
        request: EC2LockSnapshotRequest,
    ) -> EC2LockSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.lock_snapshot, request, EC2LockSnapshotResponse)

    async def modify_account_vpc_encryption_control(
        self,
        request: EC2ModifyAccountVpcEncryptionControlRequest | None = None,
    ) -> EC2ModifyAccountVpcEncryptionControlResponse:
        client = self._require_client()
        return await self._execute(client.modify_account_vpc_encryption_control, request, EC2ModifyAccountVpcEncryptionControlResponse)

    async def modify_address_attribute(
        self,
        request: EC2ModifyAddressAttributeRequest,
    ) -> EC2ModifyAddressAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_address_attribute, request, EC2ModifyAddressAttributeResponse)

    async def modify_application_status_check(
        self,
        request: EC2ModifyApplicationStatusCheckRequest,
    ) -> EC2ModifyApplicationStatusCheckResponse:
        client = self._require_client()
        return await self._execute(client.modify_application_status_check, request, EC2ModifyApplicationStatusCheckResponse)

    async def modify_availability_zone_group(
        self,
        request: EC2ModifyAvailabilityZoneGroupRequest,
    ) -> EC2ModifyAvailabilityZoneGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_availability_zone_group, request, EC2ModifyAvailabilityZoneGroupResponse)

    async def modify_capacity_reservation(
        self,
        request: EC2ModifyCapacityReservationRequest,
    ) -> EC2ModifyCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.modify_capacity_reservation, request, EC2ModifyCapacityReservationResponse)

    async def modify_capacity_reservation_fleet(
        self,
        request: EC2ModifyCapacityReservationFleetRequest,
    ) -> EC2ModifyCapacityReservationFleetResponse:
        client = self._require_client()
        return await self._execute(client.modify_capacity_reservation_fleet, request, EC2ModifyCapacityReservationFleetResponse)

    async def modify_client_vpn_endpoint(
        self,
        request: EC2ModifyClientVpnEndpointRequest,
    ) -> EC2ModifyClientVpnEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_client_vpn_endpoint, request, EC2ModifyClientVpnEndpointResponse)

    async def modify_client_vpn_endpoint_authorization_policy(
        self,
        request: EC2ModifyClientVpnEndpointAuthorizationPolicyRequest,
    ) -> EC2ModifyClientVpnEndpointAuthorizationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.modify_client_vpn_endpoint_authorization_policy, request, EC2ModifyClientVpnEndpointAuthorizationPolicyResponse)

    async def modify_default_credit_specification(
        self,
        request: EC2ModifyDefaultCreditSpecificationRequest,
    ) -> EC2ModifyDefaultCreditSpecificationResponse:
        client = self._require_client()
        return await self._execute(client.modify_default_credit_specification, request, EC2ModifyDefaultCreditSpecificationResponse)

    async def modify_ebs_default_kms_key_id(
        self,
        request: EC2ModifyEbsDefaultKmsKeyIdRequest,
    ) -> EC2ModifyEbsDefaultKmsKeyIdResponse:
        client = self._require_client()
        return await self._execute(client.modify_ebs_default_kms_key_id, request, EC2ModifyEbsDefaultKmsKeyIdResponse)

    async def modify_fleet(
        self,
        request: EC2ModifyFleetRequest,
    ) -> EC2ModifyFleetResponse:
        client = self._require_client()
        return await self._execute(client.modify_fleet, request, EC2ModifyFleetResponse)

    async def modify_fpga_image_attribute(
        self,
        request: EC2ModifyFpgaImageAttributeRequest,
    ) -> EC2ModifyFpgaImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_fpga_image_attribute, request, EC2ModifyFpgaImageAttributeResponse)

    async def modify_hosts(
        self,
        request: EC2ModifyHostsRequest,
    ) -> EC2ModifyHostsResponse:
        client = self._require_client()
        return await self._execute(client.modify_hosts, request, EC2ModifyHostsResponse)

    async def modify_id_format(
        self,
        request: EC2ModifyIdFormatRequest,
    ) -> EC2ModifyIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.modify_id_format, request, EC2ModifyIdFormatResponse)

    async def modify_identity_id_format(
        self,
        request: EC2ModifyIdentityIdFormatRequest,
    ) -> EC2ModifyIdentityIdFormatResponse:
        client = self._require_client()
        return await self._execute(client.modify_identity_id_format, request, EC2ModifyIdentityIdFormatResponse)

    async def modify_image_attribute(
        self,
        request: EC2ModifyImageAttributeRequest,
    ) -> EC2ModifyImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_image_attribute, request, EC2ModifyImageAttributeResponse)

    async def modify_instance_attribute(
        self,
        request: EC2ModifyInstanceAttributeRequest,
    ) -> EC2ModifyInstanceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_attribute, request, EC2ModifyInstanceAttributeResponse)

    async def modify_instance_capacity_reservation_attributes(
        self,
        request: EC2ModifyInstanceCapacityReservationAttributesRequest,
    ) -> EC2ModifyInstanceCapacityReservationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_capacity_reservation_attributes, request, EC2ModifyInstanceCapacityReservationAttributesResponse)

    async def modify_instance_connect_endpoint(
        self,
        request: EC2ModifyInstanceConnectEndpointRequest,
    ) -> EC2ModifyInstanceConnectEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_connect_endpoint, request, EC2ModifyInstanceConnectEndpointResponse)

    async def modify_instance_cpu_options(
        self,
        request: EC2ModifyInstanceCpuOptionsRequest,
    ) -> EC2ModifyInstanceCpuOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_cpu_options, request, EC2ModifyInstanceCpuOptionsResponse)

    async def modify_instance_credit_specification(
        self,
        request: EC2ModifyInstanceCreditSpecificationRequest,
    ) -> EC2ModifyInstanceCreditSpecificationResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_credit_specification, request, EC2ModifyInstanceCreditSpecificationResponse)

    async def modify_instance_event_start_time(
        self,
        request: EC2ModifyInstanceEventStartTimeRequest,
    ) -> EC2ModifyInstanceEventStartTimeResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_event_start_time, request, EC2ModifyInstanceEventStartTimeResponse)

    async def modify_instance_event_window(
        self,
        request: EC2ModifyInstanceEventWindowRequest,
    ) -> EC2ModifyInstanceEventWindowResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_event_window, request, EC2ModifyInstanceEventWindowResponse)

    async def modify_instance_maintenance_options(
        self,
        request: EC2ModifyInstanceMaintenanceOptionsRequest,
    ) -> EC2ModifyInstanceMaintenanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_maintenance_options, request, EC2ModifyInstanceMaintenanceOptionsResponse)

    async def modify_instance_metadata_defaults(
        self,
        request: EC2ModifyInstanceMetadataDefaultsRequest | None = None,
    ) -> EC2ModifyInstanceMetadataDefaultsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_metadata_defaults, request, EC2ModifyInstanceMetadataDefaultsResponse)

    async def modify_instance_metadata_options(
        self,
        request: EC2ModifyInstanceMetadataOptionsRequest,
    ) -> EC2ModifyInstanceMetadataOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_metadata_options, request, EC2ModifyInstanceMetadataOptionsResponse)

    async def modify_instance_network_performance_options(
        self,
        request: EC2ModifyInstanceNetworkPerformanceOptionsRequest,
    ) -> EC2ModifyInstanceNetworkPerformanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_network_performance_options, request, EC2ModifyInstanceNetworkPerformanceOptionsResponse)

    async def modify_instance_placement(
        self,
        request: EC2ModifyInstancePlacementRequest,
    ) -> EC2ModifyInstancePlacementResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_placement, request, EC2ModifyInstancePlacementResponse)

    async def modify_ipam(
        self,
        request: EC2ModifyIpamRequest,
    ) -> EC2ModifyIpamResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam, request, EC2ModifyIpamResponse)

    async def modify_ipam_policy_allocation_rules(
        self,
        request: EC2ModifyIpamPolicyAllocationRulesRequest,
    ) -> EC2ModifyIpamPolicyAllocationRulesResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_policy_allocation_rules, request, EC2ModifyIpamPolicyAllocationRulesResponse)

    async def modify_ipam_pool(
        self,
        request: EC2ModifyIpamPoolRequest,
    ) -> EC2ModifyIpamPoolResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_pool, request, EC2ModifyIpamPoolResponse)

    async def modify_ipam_pool_allocation(
        self,
        request: EC2ModifyIpamPoolAllocationRequest,
    ) -> EC2ModifyIpamPoolAllocationResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_pool_allocation, request, EC2ModifyIpamPoolAllocationResponse)

    async def modify_ipam_prefix_list_resolver(
        self,
        request: EC2ModifyIpamPrefixListResolverRequest,
    ) -> EC2ModifyIpamPrefixListResolverResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_prefix_list_resolver, request, EC2ModifyIpamPrefixListResolverResponse)

    async def modify_ipam_prefix_list_resolver_target(
        self,
        request: EC2ModifyIpamPrefixListResolverTargetRequest,
    ) -> EC2ModifyIpamPrefixListResolverTargetResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_prefix_list_resolver_target, request, EC2ModifyIpamPrefixListResolverTargetResponse)

    async def modify_ipam_resource_cidr(
        self,
        request: EC2ModifyIpamResourceCidrRequest,
    ) -> EC2ModifyIpamResourceCidrResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_resource_cidr, request, EC2ModifyIpamResourceCidrResponse)

    async def modify_ipam_resource_discovery(
        self,
        request: EC2ModifyIpamResourceDiscoveryRequest,
    ) -> EC2ModifyIpamResourceDiscoveryResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_resource_discovery, request, EC2ModifyIpamResourceDiscoveryResponse)

    async def modify_ipam_routing_policy_registration(
        self,
        request: EC2ModifyIpamRoutingPolicyRegistrationRequest,
    ) -> EC2ModifyIpamRoutingPolicyRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_routing_policy_registration, request, EC2ModifyIpamRoutingPolicyRegistrationResponse)

    async def modify_ipam_scope(
        self,
        request: EC2ModifyIpamScopeRequest,
    ) -> EC2ModifyIpamScopeResponse:
        client = self._require_client()
        return await self._execute(client.modify_ipam_scope, request, EC2ModifyIpamScopeResponse)

    async def modify_launch_template(
        self,
        request: EC2ModifyLaunchTemplateRequest | None = None,
    ) -> EC2ModifyLaunchTemplateResponse:
        client = self._require_client()
        return await self._execute(client.modify_launch_template, request, EC2ModifyLaunchTemplateResponse)

    async def modify_local_gateway_route(
        self,
        request: EC2ModifyLocalGatewayRouteRequest,
    ) -> EC2ModifyLocalGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.modify_local_gateway_route, request, EC2ModifyLocalGatewayRouteResponse)

    async def modify_managed_prefix_list(
        self,
        request: EC2ModifyManagedPrefixListRequest,
    ) -> EC2ModifyManagedPrefixListResponse:
        client = self._require_client()
        return await self._execute(client.modify_managed_prefix_list, request, EC2ModifyManagedPrefixListResponse)

    async def modify_managed_resource_visibility(
        self,
        request: EC2ModifyManagedResourceVisibilityRequest,
    ) -> EC2ModifyManagedResourceVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.modify_managed_resource_visibility, request, EC2ModifyManagedResourceVisibilityResponse)

    async def modify_metric_category(
        self,
        request: EC2ModifyMetricCategoryRequest,
    ) -> EC2ModifyMetricCategoryResponse:
        client = self._require_client()
        return await self._execute(client.modify_metric_category, request, EC2ModifyMetricCategoryResponse)

    async def modify_network_interface_attribute(
        self,
        request: EC2ModifyNetworkInterfaceAttributeRequest,
    ) -> EC2ModifyNetworkInterfaceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_network_interface_attribute, request, EC2ModifyNetworkInterfaceAttributeResponse)

    async def modify_networking_flex_cost_allocation_policy(
        self,
        request: EC2ModifyNetworkingFlexCostAllocationPolicyRequest,
    ) -> EC2ModifyNetworkingFlexCostAllocationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.modify_networking_flex_cost_allocation_policy, request, EC2ModifyNetworkingFlexCostAllocationPolicyResponse)

    async def modify_private_dns_name_options(
        self,
        request: EC2ModifyPrivateDnsNameOptionsRequest,
    ) -> EC2ModifyPrivateDnsNameOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_private_dns_name_options, request, EC2ModifyPrivateDnsNameOptionsResponse)

    async def modify_public_ip_dns_name_options(
        self,
        request: EC2ModifyPublicIpDnsNameOptionsRequest,
    ) -> EC2ModifyPublicIpDnsNameOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_public_ip_dns_name_options, request, EC2ModifyPublicIpDnsNameOptionsResponse)

    async def modify_reserved_instances(
        self,
        request: EC2ModifyReservedInstancesRequest,
    ) -> EC2ModifyReservedInstancesResponse:
        client = self._require_client()
        return await self._execute(client.modify_reserved_instances, request, EC2ModifyReservedInstancesResponse)

    async def modify_route_server(
        self,
        request: EC2ModifyRouteServerRequest,
    ) -> EC2ModifyRouteServerResponse:
        client = self._require_client()
        return await self._execute(client.modify_route_server, request, EC2ModifyRouteServerResponse)

    async def modify_security_group_rules(
        self,
        request: EC2ModifySecurityGroupRulesRequest,
    ) -> EC2ModifySecurityGroupRulesResponse:
        client = self._require_client()
        return await self._execute(client.modify_security_group_rules, request, EC2ModifySecurityGroupRulesResponse)

    async def modify_snapshot_attribute(
        self,
        request: EC2ModifySnapshotAttributeRequest,
    ) -> EC2ModifySnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_snapshot_attribute, request, EC2ModifySnapshotAttributeResponse)

    async def modify_snapshot_tier(
        self,
        request: EC2ModifySnapshotTierRequest,
    ) -> EC2ModifySnapshotTierResponse:
        client = self._require_client()
        return await self._execute(client.modify_snapshot_tier, request, EC2ModifySnapshotTierResponse)

    async def modify_spot_fleet_request(
        self,
        request: EC2ModifySpotFleetRequestRequest,
    ) -> EC2ModifySpotFleetRequestResponse:
        client = self._require_client()
        return await self._execute(client.modify_spot_fleet_request, request, EC2ModifySpotFleetRequestResponse)

    async def modify_subnet_attribute(
        self,
        request: EC2ModifySubnetAttributeRequest,
    ) -> EC2ModifySubnetAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_subnet_attribute, request, EC2ModifySubnetAttributeResponse)

    async def modify_traffic_mirror_filter_network_services(
        self,
        request: EC2ModifyTrafficMirrorFilterNetworkServicesRequest,
    ) -> EC2ModifyTrafficMirrorFilterNetworkServicesResponse:
        client = self._require_client()
        return await self._execute(client.modify_traffic_mirror_filter_network_services, request, EC2ModifyTrafficMirrorFilterNetworkServicesResponse)

    async def modify_traffic_mirror_filter_rule(
        self,
        request: EC2ModifyTrafficMirrorFilterRuleRequest,
    ) -> EC2ModifyTrafficMirrorFilterRuleResponse:
        client = self._require_client()
        return await self._execute(client.modify_traffic_mirror_filter_rule, request, EC2ModifyTrafficMirrorFilterRuleResponse)

    async def modify_traffic_mirror_session(
        self,
        request: EC2ModifyTrafficMirrorSessionRequest,
    ) -> EC2ModifyTrafficMirrorSessionResponse:
        client = self._require_client()
        return await self._execute(client.modify_traffic_mirror_session, request, EC2ModifyTrafficMirrorSessionResponse)

    async def modify_transit_gateway(
        self,
        request: EC2ModifyTransitGatewayRequest,
    ) -> EC2ModifyTransitGatewayResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway, request, EC2ModifyTransitGatewayResponse)

    async def modify_transit_gateway_attachment_nat_configuration(
        self,
        request: EC2ModifyTransitGatewayAttachmentNatConfigurationRequest,
    ) -> EC2ModifyTransitGatewayAttachmentNatConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_attachment_nat_configuration, request, EC2ModifyTransitGatewayAttachmentNatConfigurationResponse)

    async def modify_transit_gateway_metering_policy(
        self,
        request: EC2ModifyTransitGatewayMeteringPolicyRequest,
    ) -> EC2ModifyTransitGatewayMeteringPolicyResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_metering_policy, request, EC2ModifyTransitGatewayMeteringPolicyResponse)

    async def modify_transit_gateway_network_function_attachment(
        self,
        request: EC2ModifyTransitGatewayNetworkFunctionAttachmentRequest,
    ) -> EC2ModifyTransitGatewayNetworkFunctionAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_network_function_attachment, request, EC2ModifyTransitGatewayNetworkFunctionAttachmentResponse)

    async def modify_transit_gateway_peering_attachment(
        self,
        request: EC2ModifyTransitGatewayPeeringAttachmentRequest,
    ) -> EC2ModifyTransitGatewayPeeringAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_peering_attachment, request, EC2ModifyTransitGatewayPeeringAttachmentResponse)

    async def modify_transit_gateway_policy_table_entry(
        self,
        request: EC2ModifyTransitGatewayPolicyTableEntryRequest,
    ) -> EC2ModifyTransitGatewayPolicyTableEntryResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_policy_table_entry, request, EC2ModifyTransitGatewayPolicyTableEntryResponse)

    async def modify_transit_gateway_prefix_list_reference(
        self,
        request: EC2ModifyTransitGatewayPrefixListReferenceRequest,
    ) -> EC2ModifyTransitGatewayPrefixListReferenceResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_prefix_list_reference, request, EC2ModifyTransitGatewayPrefixListReferenceResponse)

    async def modify_transit_gateway_vpc_attachment(
        self,
        request: EC2ModifyTransitGatewayVpcAttachmentRequest,
    ) -> EC2ModifyTransitGatewayVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.modify_transit_gateway_vpc_attachment, request, EC2ModifyTransitGatewayVpcAttachmentResponse)

    async def modify_verified_access_endpoint(
        self,
        request: EC2ModifyVerifiedAccessEndpointRequest,
    ) -> EC2ModifyVerifiedAccessEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_endpoint, request, EC2ModifyVerifiedAccessEndpointResponse)

    async def modify_verified_access_endpoint_policy(
        self,
        request: EC2ModifyVerifiedAccessEndpointPolicyRequest,
    ) -> EC2ModifyVerifiedAccessEndpointPolicyResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_endpoint_policy, request, EC2ModifyVerifiedAccessEndpointPolicyResponse)

    async def modify_verified_access_group(
        self,
        request: EC2ModifyVerifiedAccessGroupRequest,
    ) -> EC2ModifyVerifiedAccessGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_group, request, EC2ModifyVerifiedAccessGroupResponse)

    async def modify_verified_access_group_policy(
        self,
        request: EC2ModifyVerifiedAccessGroupPolicyRequest,
    ) -> EC2ModifyVerifiedAccessGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_group_policy, request, EC2ModifyVerifiedAccessGroupPolicyResponse)

    async def modify_verified_access_instance(
        self,
        request: EC2ModifyVerifiedAccessInstanceRequest,
    ) -> EC2ModifyVerifiedAccessInstanceResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_instance, request, EC2ModifyVerifiedAccessInstanceResponse)

    async def modify_verified_access_instance_logging_configuration(
        self,
        request: EC2ModifyVerifiedAccessInstanceLoggingConfigurationRequest,
    ) -> EC2ModifyVerifiedAccessInstanceLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_instance_logging_configuration, request, EC2ModifyVerifiedAccessInstanceLoggingConfigurationResponse)

    async def modify_verified_access_trust_provider(
        self,
        request: EC2ModifyVerifiedAccessTrustProviderRequest,
    ) -> EC2ModifyVerifiedAccessTrustProviderResponse:
        client = self._require_client()
        return await self._execute(client.modify_verified_access_trust_provider, request, EC2ModifyVerifiedAccessTrustProviderResponse)

    async def modify_volume(
        self,
        request: EC2ModifyVolumeRequest,
    ) -> EC2ModifyVolumeResponse:
        client = self._require_client()
        return await self._execute(client.modify_volume, request, EC2ModifyVolumeResponse)

    async def modify_volume_attribute(
        self,
        request: EC2ModifyVolumeAttributeRequest,
    ) -> EC2ModifyVolumeAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_volume_attribute, request, EC2ModifyVolumeAttributeResponse)

    async def modify_vpc_attribute(
        self,
        request: EC2ModifyVpcAttributeRequest,
    ) -> EC2ModifyVpcAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_attribute, request, EC2ModifyVpcAttributeResponse)

    async def modify_vpc_block_public_access_exclusion(
        self,
        request: EC2ModifyVpcBlockPublicAccessExclusionRequest,
    ) -> EC2ModifyVpcBlockPublicAccessExclusionResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_block_public_access_exclusion, request, EC2ModifyVpcBlockPublicAccessExclusionResponse)

    async def modify_vpc_block_public_access_options(
        self,
        request: EC2ModifyVpcBlockPublicAccessOptionsRequest,
    ) -> EC2ModifyVpcBlockPublicAccessOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_block_public_access_options, request, EC2ModifyVpcBlockPublicAccessOptionsResponse)

    async def modify_vpc_encryption_control(
        self,
        request: EC2ModifyVpcEncryptionControlRequest,
    ) -> EC2ModifyVpcEncryptionControlResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_encryption_control, request, EC2ModifyVpcEncryptionControlResponse)

    async def modify_vpc_endpoint(
        self,
        request: EC2ModifyVpcEndpointRequest,
    ) -> EC2ModifyVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint, request, EC2ModifyVpcEndpointResponse)

    async def modify_vpc_endpoint_connection_notification(
        self,
        request: EC2ModifyVpcEndpointConnectionNotificationRequest,
    ) -> EC2ModifyVpcEndpointConnectionNotificationResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint_connection_notification, request, EC2ModifyVpcEndpointConnectionNotificationResponse)

    async def modify_vpc_endpoint_payer_responsibility(
        self,
        request: EC2ModifyVpcEndpointPayerResponsibilityRequest,
    ) -> EC2ModifyVpcEndpointPayerResponsibilityResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint_payer_responsibility, request, EC2ModifyVpcEndpointPayerResponsibilityResponse)

    async def modify_vpc_endpoint_service_configuration(
        self,
        request: EC2ModifyVpcEndpointServiceConfigurationRequest,
    ) -> EC2ModifyVpcEndpointServiceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint_service_configuration, request, EC2ModifyVpcEndpointServiceConfigurationResponse)

    async def modify_vpc_endpoint_service_payer_responsibility(
        self,
        request: EC2ModifyVpcEndpointServicePayerResponsibilityRequest,
    ) -> EC2ModifyVpcEndpointServicePayerResponsibilityResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint_service_payer_responsibility, request, EC2ModifyVpcEndpointServicePayerResponsibilityResponse)

    async def modify_vpc_endpoint_service_permissions(
        self,
        request: EC2ModifyVpcEndpointServicePermissionsRequest,
    ) -> EC2ModifyVpcEndpointServicePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_endpoint_service_permissions, request, EC2ModifyVpcEndpointServicePermissionsResponse)

    async def modify_vpc_peering_connection_options(
        self,
        request: EC2ModifyVpcPeeringConnectionOptionsRequest,
    ) -> EC2ModifyVpcPeeringConnectionOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_peering_connection_options, request, EC2ModifyVpcPeeringConnectionOptionsResponse)

    async def modify_vpc_tenancy(
        self,
        request: EC2ModifyVpcTenancyRequest,
    ) -> EC2ModifyVpcTenancyResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpc_tenancy, request, EC2ModifyVpcTenancyResponse)

    async def modify_vpn_connection(
        self,
        request: EC2ModifyVpnConnectionRequest,
    ) -> EC2ModifyVpnConnectionResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpn_connection, request, EC2ModifyVpnConnectionResponse)

    async def modify_vpn_connection_options(
        self,
        request: EC2ModifyVpnConnectionOptionsRequest,
    ) -> EC2ModifyVpnConnectionOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpn_connection_options, request, EC2ModifyVpnConnectionOptionsResponse)

    async def modify_vpn_tunnel_certificate(
        self,
        request: EC2ModifyVpnTunnelCertificateRequest,
    ) -> EC2ModifyVpnTunnelCertificateResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpn_tunnel_certificate, request, EC2ModifyVpnTunnelCertificateResponse)

    async def modify_vpn_tunnel_options(
        self,
        request: EC2ModifyVpnTunnelOptionsRequest,
    ) -> EC2ModifyVpnTunnelOptionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_vpn_tunnel_options, request, EC2ModifyVpnTunnelOptionsResponse)

    async def monitor_instances(
        self,
        request: EC2MonitorInstancesRequest,
    ) -> EC2MonitorInstancesResponse:
        client = self._require_client()
        return await self._execute(client.monitor_instances, request, EC2MonitorInstancesResponse)

    async def move_address_to_vpc(
        self,
        request: EC2MoveAddressToVpcRequest,
    ) -> EC2MoveAddressToVpcResponse:
        client = self._require_client()
        return await self._execute(client.move_address_to_vpc, request, EC2MoveAddressToVpcResponse)

    async def move_byoip_cidr_to_ipam(
        self,
        request: EC2MoveByoipCidrToIpamRequest,
    ) -> EC2MoveByoipCidrToIpamResponse:
        client = self._require_client()
        return await self._execute(client.move_byoip_cidr_to_ipam, request, EC2MoveByoipCidrToIpamResponse)

    async def move_capacity_reservation_instances(
        self,
        request: EC2MoveCapacityReservationInstancesRequest,
    ) -> EC2MoveCapacityReservationInstancesResponse:
        client = self._require_client()
        return await self._execute(client.move_capacity_reservation_instances, request, EC2MoveCapacityReservationInstancesResponse)

    async def provision_byoip_cidr(
        self,
        request: EC2ProvisionByoipCidrRequest,
    ) -> EC2ProvisionByoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.provision_byoip_cidr, request, EC2ProvisionByoipCidrResponse)

    async def provision_ipam_byoasn(
        self,
        request: EC2ProvisionIpamByoasnRequest,
    ) -> EC2ProvisionIpamByoasnResponse:
        client = self._require_client()
        return await self._execute(client.provision_ipam_byoasn, request, EC2ProvisionIpamByoasnResponse)

    async def provision_ipam_pool_cidr(
        self,
        request: EC2ProvisionIpamPoolCidrRequest,
    ) -> EC2ProvisionIpamPoolCidrResponse:
        client = self._require_client()
        return await self._execute(client.provision_ipam_pool_cidr, request, EC2ProvisionIpamPoolCidrResponse)

    async def provision_public_ipv4_pool_cidr(
        self,
        request: EC2ProvisionPublicIpv4PoolCidrRequest,
    ) -> EC2ProvisionPublicIpv4PoolCidrResponse:
        client = self._require_client()
        return await self._execute(client.provision_public_ipv4_pool_cidr, request, EC2ProvisionPublicIpv4PoolCidrResponse)

    async def purchase_capacity_block(
        self,
        request: EC2PurchaseCapacityBlockRequest,
    ) -> EC2PurchaseCapacityBlockResponse:
        client = self._require_client()
        return await self._execute(client.purchase_capacity_block, request, EC2PurchaseCapacityBlockResponse)

    async def purchase_capacity_block_extension(
        self,
        request: EC2PurchaseCapacityBlockExtensionRequest,
    ) -> EC2PurchaseCapacityBlockExtensionResponse:
        client = self._require_client()
        return await self._execute(client.purchase_capacity_block_extension, request, EC2PurchaseCapacityBlockExtensionResponse)

    async def purchase_host_reservation(
        self,
        request: EC2PurchaseHostReservationRequest,
    ) -> EC2PurchaseHostReservationResponse:
        client = self._require_client()
        return await self._execute(client.purchase_host_reservation, request, EC2PurchaseHostReservationResponse)

    async def purchase_reserved_instances_offering(
        self,
        request: EC2PurchaseReservedInstancesOfferingRequest,
    ) -> EC2PurchaseReservedInstancesOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_instances_offering, request, EC2PurchaseReservedInstancesOfferingResponse)

    async def purchase_scheduled_instances(
        self,
        request: EC2PurchaseScheduledInstancesRequest,
    ) -> EC2PurchaseScheduledInstancesResponse:
        client = self._require_client()
        return await self._execute(client.purchase_scheduled_instances, request, EC2PurchaseScheduledInstancesResponse)

    async def register_image(
        self,
        request: EC2RegisterImageRequest,
    ) -> EC2RegisterImageResponse:
        client = self._require_client()
        return await self._execute(client.register_image, request, EC2RegisterImageResponse)

    async def register_instance_event_notification_attributes(
        self,
        request: EC2RegisterInstanceEventNotificationAttributesRequest,
    ) -> EC2RegisterInstanceEventNotificationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.register_instance_event_notification_attributes, request, EC2RegisterInstanceEventNotificationAttributesResponse)

    async def register_transit_gateway_multicast_group_members(
        self,
        request: EC2RegisterTransitGatewayMulticastGroupMembersRequest,
    ) -> EC2RegisterTransitGatewayMulticastGroupMembersResponse:
        client = self._require_client()
        return await self._execute(client.register_transit_gateway_multicast_group_members, request, EC2RegisterTransitGatewayMulticastGroupMembersResponse)

    async def register_transit_gateway_multicast_group_sources(
        self,
        request: EC2RegisterTransitGatewayMulticastGroupSourcesRequest,
    ) -> EC2RegisterTransitGatewayMulticastGroupSourcesResponse:
        client = self._require_client()
        return await self._execute(client.register_transit_gateway_multicast_group_sources, request, EC2RegisterTransitGatewayMulticastGroupSourcesResponse)

    async def reject_capacity_reservation_billing_ownership(
        self,
        request: EC2RejectCapacityReservationBillingOwnershipRequest,
    ) -> EC2RejectCapacityReservationBillingOwnershipResponse:
        client = self._require_client()
        return await self._execute(client.reject_capacity_reservation_billing_ownership, request, EC2RejectCapacityReservationBillingOwnershipResponse)

    async def reject_transit_gateway_client_vpn_attachment(
        self,
        request: EC2RejectTransitGatewayClientVpnAttachmentRequest,
    ) -> EC2RejectTransitGatewayClientVpnAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.reject_transit_gateway_client_vpn_attachment, request, EC2RejectTransitGatewayClientVpnAttachmentResponse)

    async def reject_transit_gateway_multicast_domain_associations(
        self,
        request: EC2RejectTransitGatewayMulticastDomainAssociationsRequest | None = None,
    ) -> EC2RejectTransitGatewayMulticastDomainAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.reject_transit_gateway_multicast_domain_associations, request, EC2RejectTransitGatewayMulticastDomainAssociationsResponse)

    async def reject_transit_gateway_peering_attachment(
        self,
        request: EC2RejectTransitGatewayPeeringAttachmentRequest,
    ) -> EC2RejectTransitGatewayPeeringAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.reject_transit_gateway_peering_attachment, request, EC2RejectTransitGatewayPeeringAttachmentResponse)

    async def reject_transit_gateway_vpc_attachment(
        self,
        request: EC2RejectTransitGatewayVpcAttachmentRequest,
    ) -> EC2RejectTransitGatewayVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.reject_transit_gateway_vpc_attachment, request, EC2RejectTransitGatewayVpcAttachmentResponse)

    async def reject_vpc_endpoint_connections(
        self,
        request: EC2RejectVpcEndpointConnectionsRequest,
    ) -> EC2RejectVpcEndpointConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.reject_vpc_endpoint_connections, request, EC2RejectVpcEndpointConnectionsResponse)

    async def reject_vpc_peering_connection(
        self,
        request: EC2RejectVpcPeeringConnectionRequest,
    ) -> EC2RejectVpcPeeringConnectionResponse:
        client = self._require_client()
        return await self._execute(client.reject_vpc_peering_connection, request, EC2RejectVpcPeeringConnectionResponse)

    async def release_address(
        self,
        request: EC2ReleaseAddressRequest | None = None,
    ) -> EC2ReleaseAddressResponse:
        client = self._require_client()
        return await self._execute(client.release_address, request, EC2ReleaseAddressResponse)

    async def release_hosts(
        self,
        request: EC2ReleaseHostsRequest,
    ) -> EC2ReleaseHostsResponse:
        client = self._require_client()
        return await self._execute(client.release_hosts, request, EC2ReleaseHostsResponse)

    async def release_ipam_pool_allocation(
        self,
        request: EC2ReleaseIpamPoolAllocationRequest,
    ) -> EC2ReleaseIpamPoolAllocationResponse:
        client = self._require_client()
        return await self._execute(client.release_ipam_pool_allocation, request, EC2ReleaseIpamPoolAllocationResponse)

    async def replace_iam_instance_profile_association(
        self,
        request: EC2ReplaceIamInstanceProfileAssociationRequest,
    ) -> EC2ReplaceIamInstanceProfileAssociationResponse:
        client = self._require_client()
        return await self._execute(client.replace_iam_instance_profile_association, request, EC2ReplaceIamInstanceProfileAssociationResponse)

    async def replace_image_criteria_in_allowed_images_settings(
        self,
        request: EC2ReplaceImageCriteriaInAllowedImagesSettingsRequest | None = None,
    ) -> EC2ReplaceImageCriteriaInAllowedImagesSettingsResponse:
        client = self._require_client()
        return await self._execute(client.replace_image_criteria_in_allowed_images_settings, request, EC2ReplaceImageCriteriaInAllowedImagesSettingsResponse)

    async def replace_image_instance_type_specification(
        self,
        request: EC2ReplaceImageInstanceTypeSpecificationRequest,
    ) -> EC2ReplaceImageInstanceTypeSpecificationResponse:
        client = self._require_client()
        return await self._execute(client.replace_image_instance_type_specification, request, EC2ReplaceImageInstanceTypeSpecificationResponse)

    async def replace_network_acl_association(
        self,
        request: EC2ReplaceNetworkAclAssociationRequest,
    ) -> EC2ReplaceNetworkAclAssociationResponse:
        client = self._require_client()
        return await self._execute(client.replace_network_acl_association, request, EC2ReplaceNetworkAclAssociationResponse)

    async def replace_network_acl_entry(
        self,
        request: EC2ReplaceNetworkAclEntryRequest,
    ) -> EC2ReplaceNetworkAclEntryResponse:
        client = self._require_client()
        return await self._execute(client.replace_network_acl_entry, request, EC2ReplaceNetworkAclEntryResponse)

    async def replace_route(
        self,
        request: EC2ReplaceRouteRequest,
    ) -> EC2ReplaceRouteResponse:
        client = self._require_client()
        return await self._execute(client.replace_route, request, EC2ReplaceRouteResponse)

    async def replace_route_table_association(
        self,
        request: EC2ReplaceRouteTableAssociationRequest,
    ) -> EC2ReplaceRouteTableAssociationResponse:
        client = self._require_client()
        return await self._execute(client.replace_route_table_association, request, EC2ReplaceRouteTableAssociationResponse)

    async def replace_transit_gateway_route(
        self,
        request: EC2ReplaceTransitGatewayRouteRequest,
    ) -> EC2ReplaceTransitGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.replace_transit_gateway_route, request, EC2ReplaceTransitGatewayRouteResponse)

    async def replace_vpn_tunnel(
        self,
        request: EC2ReplaceVpnTunnelRequest,
    ) -> EC2ReplaceVpnTunnelResponse:
        client = self._require_client()
        return await self._execute(client.replace_vpn_tunnel, request, EC2ReplaceVpnTunnelResponse)

    async def report_instance_status(
        self,
        request: EC2ReportInstanceStatusRequest,
    ) -> EC2ReportInstanceStatusResponse:
        client = self._require_client()
        return await self._execute(client.report_instance_status, request, EC2ReportInstanceStatusResponse)

    async def request_spot_fleet(
        self,
        request: EC2RequestSpotFleetRequest,
    ) -> EC2RequestSpotFleetResponse:
        client = self._require_client()
        return await self._execute(client.request_spot_fleet, request, EC2RequestSpotFleetResponse)

    async def request_spot_instances(
        self,
        request: EC2RequestSpotInstancesRequest | None = None,
    ) -> EC2RequestSpotInstancesResponse:
        client = self._require_client()
        return await self._execute(client.request_spot_instances, request, EC2RequestSpotInstancesResponse)

    async def reset_address_attribute(
        self,
        request: EC2ResetAddressAttributeRequest,
    ) -> EC2ResetAddressAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_address_attribute, request, EC2ResetAddressAttributeResponse)

    async def reset_ebs_default_kms_key_id(
        self,
        request: EC2ResetEbsDefaultKmsKeyIdRequest | None = None,
    ) -> EC2ResetEbsDefaultKmsKeyIdResponse:
        client = self._require_client()
        return await self._execute(client.reset_ebs_default_kms_key_id, request, EC2ResetEbsDefaultKmsKeyIdResponse)

    async def reset_fpga_image_attribute(
        self,
        request: EC2ResetFpgaImageAttributeRequest,
    ) -> EC2ResetFpgaImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_fpga_image_attribute, request, EC2ResetFpgaImageAttributeResponse)

    async def reset_image_attribute(
        self,
        request: EC2ResetImageAttributeRequest,
    ) -> EC2ResetImageAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_image_attribute, request, EC2ResetImageAttributeResponse)

    async def reset_instance_attribute(
        self,
        request: EC2ResetInstanceAttributeRequest,
    ) -> EC2ResetInstanceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_instance_attribute, request, EC2ResetInstanceAttributeResponse)

    async def reset_network_interface_attribute(
        self,
        request: EC2ResetNetworkInterfaceAttributeRequest,
    ) -> EC2ResetNetworkInterfaceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_network_interface_attribute, request, EC2ResetNetworkInterfaceAttributeResponse)

    async def reset_snapshot_attribute(
        self,
        request: EC2ResetSnapshotAttributeRequest,
    ) -> EC2ResetSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.reset_snapshot_attribute, request, EC2ResetSnapshotAttributeResponse)

    async def restore_address_to_classic(
        self,
        request: EC2RestoreAddressToClassicRequest,
    ) -> EC2RestoreAddressToClassicResponse:
        client = self._require_client()
        return await self._execute(client.restore_address_to_classic, request, EC2RestoreAddressToClassicResponse)

    async def restore_image_from_recycle_bin(
        self,
        request: EC2RestoreImageFromRecycleBinRequest,
    ) -> EC2RestoreImageFromRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.restore_image_from_recycle_bin, request, EC2RestoreImageFromRecycleBinResponse)

    async def restore_managed_prefix_list_version(
        self,
        request: EC2RestoreManagedPrefixListVersionRequest,
    ) -> EC2RestoreManagedPrefixListVersionResponse:
        client = self._require_client()
        return await self._execute(client.restore_managed_prefix_list_version, request, EC2RestoreManagedPrefixListVersionResponse)

    async def restore_snapshot_from_recycle_bin(
        self,
        request: EC2RestoreSnapshotFromRecycleBinRequest,
    ) -> EC2RestoreSnapshotFromRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.restore_snapshot_from_recycle_bin, request, EC2RestoreSnapshotFromRecycleBinResponse)

    async def restore_snapshot_tier(
        self,
        request: EC2RestoreSnapshotTierRequest,
    ) -> EC2RestoreSnapshotTierResponse:
        client = self._require_client()
        return await self._execute(client.restore_snapshot_tier, request, EC2RestoreSnapshotTierResponse)

    async def restore_volume_from_recycle_bin(
        self,
        request: EC2RestoreVolumeFromRecycleBinRequest,
    ) -> EC2RestoreVolumeFromRecycleBinResponse:
        client = self._require_client()
        return await self._execute(client.restore_volume_from_recycle_bin, request, EC2RestoreVolumeFromRecycleBinResponse)

    async def revoke_client_vpn_ingress(
        self,
        request: EC2RevokeClientVpnIngressRequest,
    ) -> EC2RevokeClientVpnIngressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_client_vpn_ingress, request, EC2RevokeClientVpnIngressResponse)

    async def revoke_security_group_egress(
        self,
        request: EC2RevokeSecurityGroupEgressRequest,
    ) -> EC2RevokeSecurityGroupEgressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_security_group_egress, request, EC2RevokeSecurityGroupEgressResponse)

    async def revoke_security_group_ingress(
        self,
        request: EC2RevokeSecurityGroupIngressRequest | None = None,
    ) -> EC2RevokeSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_security_group_ingress, request, EC2RevokeSecurityGroupIngressResponse)

    async def run_scheduled_instances(
        self,
        request: EC2RunScheduledInstancesRequest,
    ) -> EC2RunScheduledInstancesResponse:
        client = self._require_client()
        return await self._execute(client.run_scheduled_instances, request, EC2RunScheduledInstancesResponse)

    async def search_local_gateway_routes(
        self,
        request: EC2SearchLocalGatewayRoutesRequest,
    ) -> EC2SearchLocalGatewayRoutesResponse:
        client = self._require_client()
        return await self._execute(client.search_local_gateway_routes, request, EC2SearchLocalGatewayRoutesResponse)

    async def search_local_gateway_routes_paginated(
        self,
        request: EC2SearchLocalGatewayRoutesRequest,
    ) -> list[EC2SearchLocalGatewayRoutesResponse]:
        return await self._paginate('search_local_gateway_routes', request, EC2SearchLocalGatewayRoutesResponse)

    async def search_transit_gateway_multicast_groups(
        self,
        request: EC2SearchTransitGatewayMulticastGroupsRequest,
    ) -> EC2SearchTransitGatewayMulticastGroupsResponse:
        client = self._require_client()
        return await self._execute(client.search_transit_gateway_multicast_groups, request, EC2SearchTransitGatewayMulticastGroupsResponse)

    async def search_transit_gateway_multicast_groups_paginated(
        self,
        request: EC2SearchTransitGatewayMulticastGroupsRequest,
    ) -> list[EC2SearchTransitGatewayMulticastGroupsResponse]:
        return await self._paginate('search_transit_gateway_multicast_groups', request, EC2SearchTransitGatewayMulticastGroupsResponse)

    async def search_transit_gateway_routes(
        self,
        request: EC2SearchTransitGatewayRoutesRequest,
    ) -> EC2SearchTransitGatewayRoutesResponse:
        client = self._require_client()
        return await self._execute(client.search_transit_gateway_routes, request, EC2SearchTransitGatewayRoutesResponse)

    async def search_transit_gateway_routes_paginated(
        self,
        request: EC2SearchTransitGatewayRoutesRequest,
    ) -> list[EC2SearchTransitGatewayRoutesResponse]:
        return await self._paginate('search_transit_gateway_routes', request, EC2SearchTransitGatewayRoutesResponse)

    async def send_diagnostic_interrupt(
        self,
        request: EC2SendDiagnosticInterruptRequest,
    ) -> EC2SendDiagnosticInterruptResponse:
        client = self._require_client()
        return await self._execute(client.send_diagnostic_interrupt, request, EC2SendDiagnosticInterruptResponse)

    async def start_declarative_policies_report(
        self,
        request: EC2StartDeclarativePoliciesReportRequest,
    ) -> EC2StartDeclarativePoliciesReportResponse:
        client = self._require_client()
        return await self._execute(client.start_declarative_policies_report, request, EC2StartDeclarativePoliciesReportResponse)

    async def start_network_insights_access_scope_analysis(
        self,
        request: EC2StartNetworkInsightsAccessScopeAnalysisRequest,
    ) -> EC2StartNetworkInsightsAccessScopeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_network_insights_access_scope_analysis, request, EC2StartNetworkInsightsAccessScopeAnalysisResponse)

    async def start_network_insights_analysis(
        self,
        request: EC2StartNetworkInsightsAnalysisRequest,
    ) -> EC2StartNetworkInsightsAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_network_insights_analysis, request, EC2StartNetworkInsightsAnalysisResponse)

    async def start_vpc_endpoint_service_private_dns_verification(
        self,
        request: EC2StartVpcEndpointServicePrivateDnsVerificationRequest,
    ) -> EC2StartVpcEndpointServicePrivateDnsVerificationResponse:
        client = self._require_client()
        return await self._execute(client.start_vpc_endpoint_service_private_dns_verification, request, EC2StartVpcEndpointServicePrivateDnsVerificationResponse)

    async def terminate_client_vpn_connections(
        self,
        request: EC2TerminateClientVpnConnectionsRequest,
    ) -> EC2TerminateClientVpnConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.terminate_client_vpn_connections, request, EC2TerminateClientVpnConnectionsResponse)

    async def unassign_ipv6_addresses(
        self,
        request: EC2UnassignIpv6AddressesRequest,
    ) -> EC2UnassignIpv6AddressesResponse:
        client = self._require_client()
        return await self._execute(client.unassign_ipv6_addresses, request, EC2UnassignIpv6AddressesResponse)

    async def unassign_private_ip_addresses(
        self,
        request: EC2UnassignPrivateIpAddressesRequest,
    ) -> EC2UnassignPrivateIpAddressesResponse:
        client = self._require_client()
        return await self._execute(client.unassign_private_ip_addresses, request, EC2UnassignPrivateIpAddressesResponse)

    async def unassign_private_nat_gateway_address(
        self,
        request: EC2UnassignPrivateNatGatewayAddressRequest,
    ) -> EC2UnassignPrivateNatGatewayAddressResponse:
        client = self._require_client()
        return await self._execute(client.unassign_private_nat_gateway_address, request, EC2UnassignPrivateNatGatewayAddressResponse)

    async def unlock_snapshot(
        self,
        request: EC2UnlockSnapshotRequest,
    ) -> EC2UnlockSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.unlock_snapshot, request, EC2UnlockSnapshotResponse)

    async def unmonitor_instances(
        self,
        request: EC2UnmonitorInstancesRequest,
    ) -> EC2UnmonitorInstancesResponse:
        client = self._require_client()
        return await self._execute(client.unmonitor_instances, request, EC2UnmonitorInstancesResponse)

    async def update_capacity_manager_monitored_tag_keys(
        self,
        request: EC2UpdateCapacityManagerMonitoredTagKeysRequest | None = None,
    ) -> EC2UpdateCapacityManagerMonitoredTagKeysResponse:
        client = self._require_client()
        return await self._execute(client.update_capacity_manager_monitored_tag_keys, request, EC2UpdateCapacityManagerMonitoredTagKeysResponse)

    async def update_capacity_manager_organizations_access(
        self,
        request: EC2UpdateCapacityManagerOrganizationsAccessRequest,
    ) -> EC2UpdateCapacityManagerOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.update_capacity_manager_organizations_access, request, EC2UpdateCapacityManagerOrganizationsAccessResponse)

    async def update_interruptible_capacity_reservation_allocation(
        self,
        request: EC2UpdateInterruptibleCapacityReservationAllocationRequest,
    ) -> EC2UpdateInterruptibleCapacityReservationAllocationResponse:
        client = self._require_client()
        return await self._execute(client.update_interruptible_capacity_reservation_allocation, request, EC2UpdateInterruptibleCapacityReservationAllocationResponse)

    async def update_security_group_rule_descriptions_egress(
        self,
        request: EC2UpdateSecurityGroupRuleDescriptionsEgressRequest | None = None,
    ) -> EC2UpdateSecurityGroupRuleDescriptionsEgressResponse:
        client = self._require_client()
        return await self._execute(client.update_security_group_rule_descriptions_egress, request, EC2UpdateSecurityGroupRuleDescriptionsEgressResponse)

    async def update_security_group_rule_descriptions_ingress(
        self,
        request: EC2UpdateSecurityGroupRuleDescriptionsIngressRequest | None = None,
    ) -> EC2UpdateSecurityGroupRuleDescriptionsIngressResponse:
        client = self._require_client()
        return await self._execute(client.update_security_group_rule_descriptions_ingress, request, EC2UpdateSecurityGroupRuleDescriptionsIngressResponse)

    async def validate_security_group_quotas_for_interface(
        self,
        request: EC2ValidateSecurityGroupQuotasForInterfaceRequest,
    ) -> EC2ValidateSecurityGroupQuotasForInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.validate_security_group_quotas_for_interface, request, EC2ValidateSecurityGroupQuotasForInterfaceResponse)

    async def withdraw_byoip_cidr(
        self,
        request: EC2WithdrawByoipCidrRequest,
    ) -> EC2WithdrawByoipCidrResponse:
        client = self._require_client()
        return await self._execute(client.withdraw_byoip_cidr, request, EC2WithdrawByoipCidrResponse)


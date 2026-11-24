from werkflow_aws.models.direct_connect import (
    DirectConnectAcceptDirectConnectGatewayAssociationProposalRequest,
    DirectConnectAcceptDirectConnectGatewayAssociationProposalResponse,
    DirectConnectAllocateConnectionOnInterconnectRequest,
    DirectConnectAllocateConnectionOnInterconnectResponse,
    DirectConnectAllocateHostedConnectionRequest,
    DirectConnectAllocateHostedConnectionResponse,
    DirectConnectAllocatePrivateVirtualInterfaceRequest,
    DirectConnectAllocatePrivateVirtualInterfaceResponse,
    DirectConnectAllocatePublicVirtualInterfaceRequest,
    DirectConnectAllocatePublicVirtualInterfaceResponse,
    DirectConnectAllocateTransitVirtualInterfaceRequest,
    DirectConnectAllocateTransitVirtualInterfaceResponse,
    DirectConnectAssociateConnectionWithLagRequest,
    DirectConnectAssociateConnectionWithLagResponse,
    DirectConnectAssociateConnectionsToResiliencyGroupRequest,
    DirectConnectAssociateConnectionsToResiliencyGroupResponse,
    DirectConnectAssociateHostedConnectionRequest,
    DirectConnectAssociateHostedConnectionResponse,
    DirectConnectAssociateMacSecKeyRequest,
    DirectConnectAssociateMacSecKeyResponse,
    DirectConnectAssociateVirtualInterfaceRequest,
    DirectConnectAssociateVirtualInterfaceResponse,
    DirectConnectConfirmConnectionRequest,
    DirectConnectConfirmConnectionResponse,
    DirectConnectConfirmCustomerAgreementRequest,
    DirectConnectConfirmCustomerAgreementResponse,
    DirectConnectConfirmPrivateVirtualInterfaceRequest,
    DirectConnectConfirmPrivateVirtualInterfaceResponse,
    DirectConnectConfirmPublicVirtualInterfaceRequest,
    DirectConnectConfirmPublicVirtualInterfaceResponse,
    DirectConnectConfirmTransitVirtualInterfaceRequest,
    DirectConnectConfirmTransitVirtualInterfaceResponse,
    DirectConnectCreateBGPPeerRequest,
    DirectConnectCreateBGPPeerResponse,
    DirectConnectCreateConnectionRequest,
    DirectConnectCreateConnectionResponse,
    DirectConnectCreateDirectConnectGatewayAssociationProposalRequest,
    DirectConnectCreateDirectConnectGatewayAssociationProposalResponse,
    DirectConnectCreateDirectConnectGatewayAssociationRequest,
    DirectConnectCreateDirectConnectGatewayAssociationResponse,
    DirectConnectCreateDirectConnectGatewayRequest,
    DirectConnectCreateDirectConnectGatewayResponse,
    DirectConnectCreateInterconnectRequest,
    DirectConnectCreateInterconnectResponse,
    DirectConnectCreateLagRequest,
    DirectConnectCreateLagResponse,
    DirectConnectCreatePrivateVirtualInterfaceRequest,
    DirectConnectCreatePrivateVirtualInterfaceResponse,
    DirectConnectCreatePublicVirtualInterfaceRequest,
    DirectConnectCreatePublicVirtualInterfaceResponse,
    DirectConnectCreateResiliencyGroupRequest,
    DirectConnectCreateResiliencyGroupResponse,
    DirectConnectCreateTransitVirtualInterfaceRequest,
    DirectConnectCreateTransitVirtualInterfaceResponse,
    DirectConnectDeleteBGPPeerRequest,
    DirectConnectDeleteBGPPeerResponse,
    DirectConnectDeleteConnectionRequest,
    DirectConnectDeleteConnectionResponse,
    DirectConnectDeleteDirectConnectGatewayAssociationProposalRequest,
    DirectConnectDeleteDirectConnectGatewayAssociationProposalResponse,
    DirectConnectDeleteDirectConnectGatewayAssociationRequest,
    DirectConnectDeleteDirectConnectGatewayAssociationResponse,
    DirectConnectDeleteDirectConnectGatewayRequest,
    DirectConnectDeleteDirectConnectGatewayResponse,
    DirectConnectDeleteInterconnectRequest,
    DirectConnectDeleteInterconnectResponse,
    DirectConnectDeleteLagRequest,
    DirectConnectDeleteLagResponse,
    DirectConnectDeleteResiliencyGroupRequest,
    DirectConnectDeleteResiliencyGroupResponse,
    DirectConnectDeleteVirtualInterfaceRequest,
    DirectConnectDeleteVirtualInterfaceResponse,
    DirectConnectDescribeConnectionLoaRequest,
    DirectConnectDescribeConnectionLoaResponse,
    DirectConnectDescribeConnectionsOnInterconnectRequest,
    DirectConnectDescribeConnectionsOnInterconnectResponse,
    DirectConnectDescribeConnectionsRequest,
    DirectConnectDescribeConnectionsResponse,
    DirectConnectDescribeCustomerMetadataRequest,
    DirectConnectDescribeCustomerMetadataResponse,
    DirectConnectDescribeDirectConnectGatewayAssociationProposalsRequest,
    DirectConnectDescribeDirectConnectGatewayAssociationProposalsResponse,
    DirectConnectDescribeDirectConnectGatewayAssociationsRequest,
    DirectConnectDescribeDirectConnectGatewayAssociationsResponse,
    DirectConnectDescribeDirectConnectGatewayAttachmentsRequest,
    DirectConnectDescribeDirectConnectGatewayAttachmentsResponse,
    DirectConnectDescribeDirectConnectGatewaysRequest,
    DirectConnectDescribeDirectConnectGatewaysResponse,
    DirectConnectDescribeHostedConnectionsRequest,
    DirectConnectDescribeHostedConnectionsResponse,
    DirectConnectDescribeInterconnectLoaRequest,
    DirectConnectDescribeInterconnectLoaResponse,
    DirectConnectDescribeInterconnectsRequest,
    DirectConnectDescribeInterconnectsResponse,
    DirectConnectDescribeLagsRequest,
    DirectConnectDescribeLagsResponse,
    DirectConnectDescribeLoaRequest,
    DirectConnectDescribeLoaResponse,
    DirectConnectDescribeLocationsRequest,
    DirectConnectDescribeLocationsResponse,
    DirectConnectDescribeRouterConfigurationRequest,
    DirectConnectDescribeRouterConfigurationResponse,
    DirectConnectDescribeTagsRequest,
    DirectConnectDescribeTagsResponse,
    DirectConnectDescribeVirtualGatewaysRequest,
    DirectConnectDescribeVirtualGatewaysResponse,
    DirectConnectDescribeVirtualInterfacesRequest,
    DirectConnectDescribeVirtualInterfacesResponse,
    DirectConnectDisassociateConnectionFromLagRequest,
    DirectConnectDisassociateConnectionFromLagResponse,
    DirectConnectDisassociateConnectionsFromResiliencyGroupRequest,
    DirectConnectDisassociateConnectionsFromResiliencyGroupResponse,
    DirectConnectDisassociateMacSecKeyRequest,
    DirectConnectDisassociateMacSecKeyResponse,
    DirectConnectGetResiliencyGroupRequest,
    DirectConnectGetResiliencyGroupResponse,
    DirectConnectListResiliencyGroupAssociationsRequest,
    DirectConnectListResiliencyGroupAssociationsResponse,
    DirectConnectListResiliencyGroupsRequest,
    DirectConnectListResiliencyGroupsResponse,
    DirectConnectListVirtualInterfaceRoutesRequest,
    DirectConnectListVirtualInterfaceRoutesResponse,
    DirectConnectListVirtualInterfaceTestHistoryRequest,
    DirectConnectListVirtualInterfaceTestHistoryResponse,
    DirectConnectStartBgpFailoverTestRequest,
    DirectConnectStartBgpFailoverTestResponse,
    DirectConnectStopBgpFailoverTestRequest,
    DirectConnectStopBgpFailoverTestResponse,
    DirectConnectTagResourceRequest,
    DirectConnectTagResourceResponse,
    DirectConnectUntagResourceRequest,
    DirectConnectUntagResourceResponse,
    DirectConnectUpdateConnectionRequest,
    DirectConnectUpdateConnectionResponse,
    DirectConnectUpdateConnectionsBillingModeRequest,
    DirectConnectUpdateConnectionsBillingModeResponse,
    DirectConnectUpdateDirectConnectGatewayAssociationRequest,
    DirectConnectUpdateDirectConnectGatewayAssociationResponse,
    DirectConnectUpdateDirectConnectGatewayRequest,
    DirectConnectUpdateDirectConnectGatewayResponse,
    DirectConnectUpdateLagRequest,
    DirectConnectUpdateLagResponse,
    DirectConnectUpdateResiliencyGroupRequest,
    DirectConnectUpdateResiliencyGroupResponse,
    DirectConnectUpdateVirtualInterfaceAttributesRequest,
    DirectConnectUpdateVirtualInterfaceAttributesResponse,
)
from werkflow_aws.types.direct_connect_client import DirectConnectClient
from .base import AWSBaseService


class AWSDirectConnect(AWSBaseService[DirectConnectClient]):
    service_name = 'direct-connect'
    boto3_service_name = 'directconnect'

    def __init__(self) -> None:
        super().__init__(service_name='direct-connect', boto3_service_name='directconnect')

    async def accept_direct_connect_gateway_association_proposal(
        self,
        request: DirectConnectAcceptDirectConnectGatewayAssociationProposalRequest,
    ) -> DirectConnectAcceptDirectConnectGatewayAssociationProposalResponse:
        client = self._require_client()
        return await self._execute(client.accept_direct_connect_gateway_association_proposal, request, DirectConnectAcceptDirectConnectGatewayAssociationProposalResponse)

    async def allocate_connection_on_interconnect(
        self,
        request: DirectConnectAllocateConnectionOnInterconnectRequest,
    ) -> DirectConnectAllocateConnectionOnInterconnectResponse:
        client = self._require_client()
        return await self._execute(client.allocate_connection_on_interconnect, request, DirectConnectAllocateConnectionOnInterconnectResponse)

    async def allocate_hosted_connection(
        self,
        request: DirectConnectAllocateHostedConnectionRequest,
    ) -> DirectConnectAllocateHostedConnectionResponse:
        client = self._require_client()
        return await self._execute(client.allocate_hosted_connection, request, DirectConnectAllocateHostedConnectionResponse)

    async def allocate_private_virtual_interface(
        self,
        request: DirectConnectAllocatePrivateVirtualInterfaceRequest,
    ) -> DirectConnectAllocatePrivateVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.allocate_private_virtual_interface, request, DirectConnectAllocatePrivateVirtualInterfaceResponse)

    async def allocate_public_virtual_interface(
        self,
        request: DirectConnectAllocatePublicVirtualInterfaceRequest,
    ) -> DirectConnectAllocatePublicVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.allocate_public_virtual_interface, request, DirectConnectAllocatePublicVirtualInterfaceResponse)

    async def allocate_transit_virtual_interface(
        self,
        request: DirectConnectAllocateTransitVirtualInterfaceRequest,
    ) -> DirectConnectAllocateTransitVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.allocate_transit_virtual_interface, request, DirectConnectAllocateTransitVirtualInterfaceResponse)

    async def associate_connection_with_lag(
        self,
        request: DirectConnectAssociateConnectionWithLagRequest,
    ) -> DirectConnectAssociateConnectionWithLagResponse:
        client = self._require_client()
        return await self._execute(client.associate_connection_with_lag, request, DirectConnectAssociateConnectionWithLagResponse)

    async def associate_connections_to_resiliency_group(
        self,
        request: DirectConnectAssociateConnectionsToResiliencyGroupRequest,
    ) -> DirectConnectAssociateConnectionsToResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.associate_connections_to_resiliency_group, request, DirectConnectAssociateConnectionsToResiliencyGroupResponse)

    async def associate_hosted_connection(
        self,
        request: DirectConnectAssociateHostedConnectionRequest,
    ) -> DirectConnectAssociateHostedConnectionResponse:
        client = self._require_client()
        return await self._execute(client.associate_hosted_connection, request, DirectConnectAssociateHostedConnectionResponse)

    async def associate_mac_sec_key(
        self,
        request: DirectConnectAssociateMacSecKeyRequest,
    ) -> DirectConnectAssociateMacSecKeyResponse:
        client = self._require_client()
        return await self._execute(client.associate_mac_sec_key, request, DirectConnectAssociateMacSecKeyResponse)

    async def associate_virtual_interface(
        self,
        request: DirectConnectAssociateVirtualInterfaceRequest,
    ) -> DirectConnectAssociateVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.associate_virtual_interface, request, DirectConnectAssociateVirtualInterfaceResponse)

    async def confirm_connection(
        self,
        request: DirectConnectConfirmConnectionRequest,
    ) -> DirectConnectConfirmConnectionResponse:
        client = self._require_client()
        return await self._execute(client.confirm_connection, request, DirectConnectConfirmConnectionResponse)

    async def confirm_customer_agreement(
        self,
        request: DirectConnectConfirmCustomerAgreementRequest | None = None,
    ) -> DirectConnectConfirmCustomerAgreementResponse:
        client = self._require_client()
        return await self._execute(client.confirm_customer_agreement, request, DirectConnectConfirmCustomerAgreementResponse)

    async def confirm_private_virtual_interface(
        self,
        request: DirectConnectConfirmPrivateVirtualInterfaceRequest,
    ) -> DirectConnectConfirmPrivateVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.confirm_private_virtual_interface, request, DirectConnectConfirmPrivateVirtualInterfaceResponse)

    async def confirm_public_virtual_interface(
        self,
        request: DirectConnectConfirmPublicVirtualInterfaceRequest,
    ) -> DirectConnectConfirmPublicVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.confirm_public_virtual_interface, request, DirectConnectConfirmPublicVirtualInterfaceResponse)

    async def confirm_transit_virtual_interface(
        self,
        request: DirectConnectConfirmTransitVirtualInterfaceRequest,
    ) -> DirectConnectConfirmTransitVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.confirm_transit_virtual_interface, request, DirectConnectConfirmTransitVirtualInterfaceResponse)

    async def create_bgp_peer(
        self,
        request: DirectConnectCreateBGPPeerRequest | None = None,
    ) -> DirectConnectCreateBGPPeerResponse:
        client = self._require_client()
        return await self._execute(client.create_bgp_peer, request, DirectConnectCreateBGPPeerResponse)

    async def create_connection(
        self,
        request: DirectConnectCreateConnectionRequest,
    ) -> DirectConnectCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, DirectConnectCreateConnectionResponse)

    async def create_direct_connect_gateway(
        self,
        request: DirectConnectCreateDirectConnectGatewayRequest,
    ) -> DirectConnectCreateDirectConnectGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_direct_connect_gateway, request, DirectConnectCreateDirectConnectGatewayResponse)

    async def create_direct_connect_gateway_association(
        self,
        request: DirectConnectCreateDirectConnectGatewayAssociationRequest,
    ) -> DirectConnectCreateDirectConnectGatewayAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_direct_connect_gateway_association, request, DirectConnectCreateDirectConnectGatewayAssociationResponse)

    async def create_direct_connect_gateway_association_proposal(
        self,
        request: DirectConnectCreateDirectConnectGatewayAssociationProposalRequest,
    ) -> DirectConnectCreateDirectConnectGatewayAssociationProposalResponse:
        client = self._require_client()
        return await self._execute(client.create_direct_connect_gateway_association_proposal, request, DirectConnectCreateDirectConnectGatewayAssociationProposalResponse)

    async def create_interconnect(
        self,
        request: DirectConnectCreateInterconnectRequest,
    ) -> DirectConnectCreateInterconnectResponse:
        client = self._require_client()
        return await self._execute(client.create_interconnect, request, DirectConnectCreateInterconnectResponse)

    async def create_lag(
        self,
        request: DirectConnectCreateLagRequest,
    ) -> DirectConnectCreateLagResponse:
        client = self._require_client()
        return await self._execute(client.create_lag, request, DirectConnectCreateLagResponse)

    async def create_private_virtual_interface(
        self,
        request: DirectConnectCreatePrivateVirtualInterfaceRequest,
    ) -> DirectConnectCreatePrivateVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.create_private_virtual_interface, request, DirectConnectCreatePrivateVirtualInterfaceResponse)

    async def create_public_virtual_interface(
        self,
        request: DirectConnectCreatePublicVirtualInterfaceRequest,
    ) -> DirectConnectCreatePublicVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.create_public_virtual_interface, request, DirectConnectCreatePublicVirtualInterfaceResponse)

    async def create_resiliency_group(
        self,
        request: DirectConnectCreateResiliencyGroupRequest,
    ) -> DirectConnectCreateResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_resiliency_group, request, DirectConnectCreateResiliencyGroupResponse)

    async def create_transit_virtual_interface(
        self,
        request: DirectConnectCreateTransitVirtualInterfaceRequest,
    ) -> DirectConnectCreateTransitVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_virtual_interface, request, DirectConnectCreateTransitVirtualInterfaceResponse)

    async def delete_bgp_peer(
        self,
        request: DirectConnectDeleteBGPPeerRequest | None = None,
    ) -> DirectConnectDeleteBGPPeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_bgp_peer, request, DirectConnectDeleteBGPPeerResponse)

    async def delete_connection(
        self,
        request: DirectConnectDeleteConnectionRequest,
    ) -> DirectConnectDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, DirectConnectDeleteConnectionResponse)

    async def delete_direct_connect_gateway(
        self,
        request: DirectConnectDeleteDirectConnectGatewayRequest,
    ) -> DirectConnectDeleteDirectConnectGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_direct_connect_gateway, request, DirectConnectDeleteDirectConnectGatewayResponse)

    async def delete_direct_connect_gateway_association(
        self,
        request: DirectConnectDeleteDirectConnectGatewayAssociationRequest | None = None,
    ) -> DirectConnectDeleteDirectConnectGatewayAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_direct_connect_gateway_association, request, DirectConnectDeleteDirectConnectGatewayAssociationResponse)

    async def delete_direct_connect_gateway_association_proposal(
        self,
        request: DirectConnectDeleteDirectConnectGatewayAssociationProposalRequest,
    ) -> DirectConnectDeleteDirectConnectGatewayAssociationProposalResponse:
        client = self._require_client()
        return await self._execute(client.delete_direct_connect_gateway_association_proposal, request, DirectConnectDeleteDirectConnectGatewayAssociationProposalResponse)

    async def delete_interconnect(
        self,
        request: DirectConnectDeleteInterconnectRequest,
    ) -> DirectConnectDeleteInterconnectResponse:
        client = self._require_client()
        return await self._execute(client.delete_interconnect, request, DirectConnectDeleteInterconnectResponse)

    async def delete_lag(
        self,
        request: DirectConnectDeleteLagRequest,
    ) -> DirectConnectDeleteLagResponse:
        client = self._require_client()
        return await self._execute(client.delete_lag, request, DirectConnectDeleteLagResponse)

    async def delete_resiliency_group(
        self,
        request: DirectConnectDeleteResiliencyGroupRequest,
    ) -> DirectConnectDeleteResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_resiliency_group, request, DirectConnectDeleteResiliencyGroupResponse)

    async def delete_virtual_interface(
        self,
        request: DirectConnectDeleteVirtualInterfaceRequest,
    ) -> DirectConnectDeleteVirtualInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_virtual_interface, request, DirectConnectDeleteVirtualInterfaceResponse)

    async def describe_connection_loa(
        self,
        request: DirectConnectDescribeConnectionLoaRequest,
    ) -> DirectConnectDescribeConnectionLoaResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection_loa, request, DirectConnectDescribeConnectionLoaResponse)

    async def describe_connections(
        self,
        request: DirectConnectDescribeConnectionsRequest | None = None,
    ) -> DirectConnectDescribeConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_connections, request, DirectConnectDescribeConnectionsResponse)

    async def describe_connections_on_interconnect(
        self,
        request: DirectConnectDescribeConnectionsOnInterconnectRequest,
    ) -> DirectConnectDescribeConnectionsOnInterconnectResponse:
        client = self._require_client()
        return await self._execute(client.describe_connections_on_interconnect, request, DirectConnectDescribeConnectionsOnInterconnectResponse)

    async def describe_customer_metadata(
        self,
        request: DirectConnectDescribeCustomerMetadataRequest | None = None,
    ) -> DirectConnectDescribeCustomerMetadataResponse:
        client = self._require_client()
        return await self._execute(client.describe_customer_metadata, request, DirectConnectDescribeCustomerMetadataResponse)

    async def describe_direct_connect_gateway_association_proposals(
        self,
        request: DirectConnectDescribeDirectConnectGatewayAssociationProposalsRequest | None = None,
    ) -> DirectConnectDescribeDirectConnectGatewayAssociationProposalsResponse:
        client = self._require_client()
        return await self._execute(client.describe_direct_connect_gateway_association_proposals, request, DirectConnectDescribeDirectConnectGatewayAssociationProposalsResponse)

    async def describe_direct_connect_gateway_associations(
        self,
        request: DirectConnectDescribeDirectConnectGatewayAssociationsRequest | None = None,
    ) -> DirectConnectDescribeDirectConnectGatewayAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_direct_connect_gateway_associations, request, DirectConnectDescribeDirectConnectGatewayAssociationsResponse)

    async def describe_direct_connect_gateway_associations_paginated(
        self,
        request: DirectConnectDescribeDirectConnectGatewayAssociationsRequest | None = None,
    ) -> list[DirectConnectDescribeDirectConnectGatewayAssociationsResponse]:
        return await self._paginate('describe_direct_connect_gateway_associations', request, DirectConnectDescribeDirectConnectGatewayAssociationsResponse)

    async def describe_direct_connect_gateway_attachments(
        self,
        request: DirectConnectDescribeDirectConnectGatewayAttachmentsRequest | None = None,
    ) -> DirectConnectDescribeDirectConnectGatewayAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_direct_connect_gateway_attachments, request, DirectConnectDescribeDirectConnectGatewayAttachmentsResponse)

    async def describe_direct_connect_gateway_attachments_paginated(
        self,
        request: DirectConnectDescribeDirectConnectGatewayAttachmentsRequest | None = None,
    ) -> list[DirectConnectDescribeDirectConnectGatewayAttachmentsResponse]:
        return await self._paginate('describe_direct_connect_gateway_attachments', request, DirectConnectDescribeDirectConnectGatewayAttachmentsResponse)

    async def describe_direct_connect_gateways(
        self,
        request: DirectConnectDescribeDirectConnectGatewaysRequest | None = None,
    ) -> DirectConnectDescribeDirectConnectGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_direct_connect_gateways, request, DirectConnectDescribeDirectConnectGatewaysResponse)

    async def describe_direct_connect_gateways_paginated(
        self,
        request: DirectConnectDescribeDirectConnectGatewaysRequest | None = None,
    ) -> list[DirectConnectDescribeDirectConnectGatewaysResponse]:
        return await self._paginate('describe_direct_connect_gateways', request, DirectConnectDescribeDirectConnectGatewaysResponse)

    async def describe_hosted_connections(
        self,
        request: DirectConnectDescribeHostedConnectionsRequest,
    ) -> DirectConnectDescribeHostedConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_hosted_connections, request, DirectConnectDescribeHostedConnectionsResponse)

    async def describe_interconnect_loa(
        self,
        request: DirectConnectDescribeInterconnectLoaRequest,
    ) -> DirectConnectDescribeInterconnectLoaResponse:
        client = self._require_client()
        return await self._execute(client.describe_interconnect_loa, request, DirectConnectDescribeInterconnectLoaResponse)

    async def describe_interconnects(
        self,
        request: DirectConnectDescribeInterconnectsRequest | None = None,
    ) -> DirectConnectDescribeInterconnectsResponse:
        client = self._require_client()
        return await self._execute(client.describe_interconnects, request, DirectConnectDescribeInterconnectsResponse)

    async def describe_lags(
        self,
        request: DirectConnectDescribeLagsRequest | None = None,
    ) -> DirectConnectDescribeLagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_lags, request, DirectConnectDescribeLagsResponse)

    async def describe_loa(
        self,
        request: DirectConnectDescribeLoaRequest,
    ) -> DirectConnectDescribeLoaResponse:
        client = self._require_client()
        return await self._execute(client.describe_loa, request, DirectConnectDescribeLoaResponse)

    async def describe_locations(
        self,
        request: DirectConnectDescribeLocationsRequest | None = None,
    ) -> DirectConnectDescribeLocationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_locations, request, DirectConnectDescribeLocationsResponse)

    async def describe_router_configuration(
        self,
        request: DirectConnectDescribeRouterConfigurationRequest,
    ) -> DirectConnectDescribeRouterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_router_configuration, request, DirectConnectDescribeRouterConfigurationResponse)

    async def describe_tags(
        self,
        request: DirectConnectDescribeTagsRequest,
    ) -> DirectConnectDescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, DirectConnectDescribeTagsResponse)

    async def describe_virtual_gateways(
        self,
        request: DirectConnectDescribeVirtualGatewaysRequest | None = None,
    ) -> DirectConnectDescribeVirtualGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.describe_virtual_gateways, request, DirectConnectDescribeVirtualGatewaysResponse)

    async def describe_virtual_interfaces(
        self,
        request: DirectConnectDescribeVirtualInterfacesRequest | None = None,
    ) -> DirectConnectDescribeVirtualInterfacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_virtual_interfaces, request, DirectConnectDescribeVirtualInterfacesResponse)

    async def disassociate_connection_from_lag(
        self,
        request: DirectConnectDisassociateConnectionFromLagRequest,
    ) -> DirectConnectDisassociateConnectionFromLagResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_connection_from_lag, request, DirectConnectDisassociateConnectionFromLagResponse)

    async def disassociate_connections_from_resiliency_group(
        self,
        request: DirectConnectDisassociateConnectionsFromResiliencyGroupRequest,
    ) -> DirectConnectDisassociateConnectionsFromResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_connections_from_resiliency_group, request, DirectConnectDisassociateConnectionsFromResiliencyGroupResponse)

    async def disassociate_mac_sec_key(
        self,
        request: DirectConnectDisassociateMacSecKeyRequest,
    ) -> DirectConnectDisassociateMacSecKeyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_mac_sec_key, request, DirectConnectDisassociateMacSecKeyResponse)

    async def get_resiliency_group(
        self,
        request: DirectConnectGetResiliencyGroupRequest,
    ) -> DirectConnectGetResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_resiliency_group, request, DirectConnectGetResiliencyGroupResponse)

    async def list_resiliency_group_associations(
        self,
        request: DirectConnectListResiliencyGroupAssociationsRequest,
    ) -> DirectConnectListResiliencyGroupAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_resiliency_group_associations, request, DirectConnectListResiliencyGroupAssociationsResponse)

    async def list_resiliency_groups(
        self,
        request: DirectConnectListResiliencyGroupsRequest | None = None,
    ) -> DirectConnectListResiliencyGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_resiliency_groups, request, DirectConnectListResiliencyGroupsResponse)

    async def list_virtual_interface_routes(
        self,
        request: DirectConnectListVirtualInterfaceRoutesRequest | None = None,
    ) -> DirectConnectListVirtualInterfaceRoutesResponse:
        client = self._require_client()
        return await self._execute(client.list_virtual_interface_routes, request, DirectConnectListVirtualInterfaceRoutesResponse)

    async def list_virtual_interface_test_history(
        self,
        request: DirectConnectListVirtualInterfaceTestHistoryRequest | None = None,
    ) -> DirectConnectListVirtualInterfaceTestHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_virtual_interface_test_history, request, DirectConnectListVirtualInterfaceTestHistoryResponse)

    async def start_bgp_failover_test(
        self,
        request: DirectConnectStartBgpFailoverTestRequest,
    ) -> DirectConnectStartBgpFailoverTestResponse:
        client = self._require_client()
        return await self._execute(client.start_bgp_failover_test, request, DirectConnectStartBgpFailoverTestResponse)

    async def stop_bgp_failover_test(
        self,
        request: DirectConnectStopBgpFailoverTestRequest,
    ) -> DirectConnectStopBgpFailoverTestResponse:
        client = self._require_client()
        return await self._execute(client.stop_bgp_failover_test, request, DirectConnectStopBgpFailoverTestResponse)

    async def tag_resource(
        self,
        request: DirectConnectTagResourceRequest,
    ) -> DirectConnectTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, DirectConnectTagResourceResponse)

    async def untag_resource(
        self,
        request: DirectConnectUntagResourceRequest,
    ) -> DirectConnectUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, DirectConnectUntagResourceResponse)

    async def update_connection(
        self,
        request: DirectConnectUpdateConnectionRequest,
    ) -> DirectConnectUpdateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection, request, DirectConnectUpdateConnectionResponse)

    async def update_connections_billing_mode(
        self,
        request: DirectConnectUpdateConnectionsBillingModeRequest,
    ) -> DirectConnectUpdateConnectionsBillingModeResponse:
        client = self._require_client()
        return await self._execute(client.update_connections_billing_mode, request, DirectConnectUpdateConnectionsBillingModeResponse)

    async def update_direct_connect_gateway(
        self,
        request: DirectConnectUpdateDirectConnectGatewayRequest,
    ) -> DirectConnectUpdateDirectConnectGatewayResponse:
        client = self._require_client()
        return await self._execute(client.update_direct_connect_gateway, request, DirectConnectUpdateDirectConnectGatewayResponse)

    async def update_direct_connect_gateway_association(
        self,
        request: DirectConnectUpdateDirectConnectGatewayAssociationRequest | None = None,
    ) -> DirectConnectUpdateDirectConnectGatewayAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_direct_connect_gateway_association, request, DirectConnectUpdateDirectConnectGatewayAssociationResponse)

    async def update_lag(
        self,
        request: DirectConnectUpdateLagRequest,
    ) -> DirectConnectUpdateLagResponse:
        client = self._require_client()
        return await self._execute(client.update_lag, request, DirectConnectUpdateLagResponse)

    async def update_resiliency_group(
        self,
        request: DirectConnectUpdateResiliencyGroupRequest,
    ) -> DirectConnectUpdateResiliencyGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_resiliency_group, request, DirectConnectUpdateResiliencyGroupResponse)

    async def update_virtual_interface_attributes(
        self,
        request: DirectConnectUpdateVirtualInterfaceAttributesRequest,
    ) -> DirectConnectUpdateVirtualInterfaceAttributesResponse:
        client = self._require_client()
        return await self._execute(client.update_virtual_interface_attributes, request, DirectConnectUpdateVirtualInterfaceAttributesResponse)

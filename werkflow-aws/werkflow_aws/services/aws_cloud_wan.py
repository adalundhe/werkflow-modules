from werkflow_aws.models.cloud_wan import (
    NetworkManagerAcceptAttachmentRequest,
    NetworkManagerAcceptAttachmentResponse,
    NetworkManagerAssociateConnectPeerRequest,
    NetworkManagerAssociateConnectPeerResponse,
    NetworkManagerAssociateContextStoreRequest,
    NetworkManagerAssociateContextStoreResponse,
    NetworkManagerAssociateCustomerGatewayRequest,
    NetworkManagerAssociateCustomerGatewayResponse,
    NetworkManagerAssociateLinkRequest,
    NetworkManagerAssociateLinkResponse,
    NetworkManagerAssociateTransitGatewayConnectPeerRequest,
    NetworkManagerAssociateTransitGatewayConnectPeerResponse,
    NetworkManagerCreateConnectAttachmentRequest,
    NetworkManagerCreateConnectAttachmentResponse,
    NetworkManagerCreateConnectPeerRequest,
    NetworkManagerCreateConnectPeerResponse,
    NetworkManagerCreateConnectionRequest,
    NetworkManagerCreateConnectionResponse,
    NetworkManagerCreateContextStoreRequest,
    NetworkManagerCreateContextStoreResponse,
    NetworkManagerCreateCoreNetworkPrefixListAssociationRequest,
    NetworkManagerCreateCoreNetworkPrefixListAssociationResponse,
    NetworkManagerCreateCoreNetworkRequest,
    NetworkManagerCreateCoreNetworkResponse,
    NetworkManagerCreateDeviceRequest,
    NetworkManagerCreateDeviceResponse,
    NetworkManagerCreateDirectConnectGatewayAttachmentRequest,
    NetworkManagerCreateDirectConnectGatewayAttachmentResponse,
    NetworkManagerCreateGlobalNetworkRequest,
    NetworkManagerCreateGlobalNetworkResponse,
    NetworkManagerCreateLinkRequest,
    NetworkManagerCreateLinkResponse,
    NetworkManagerCreateSiteRequest,
    NetworkManagerCreateSiteResponse,
    NetworkManagerCreateSiteToSiteVpnAttachmentRequest,
    NetworkManagerCreateSiteToSiteVpnAttachmentResponse,
    NetworkManagerCreateTransitGatewayPeeringRequest,
    NetworkManagerCreateTransitGatewayPeeringResponse,
    NetworkManagerCreateTransitGatewayRouteTableAttachmentRequest,
    NetworkManagerCreateTransitGatewayRouteTableAttachmentResponse,
    NetworkManagerCreateVpcAttachmentRequest,
    NetworkManagerCreateVpcAttachmentResponse,
    NetworkManagerDeleteAttachmentRequest,
    NetworkManagerDeleteAttachmentResponse,
    NetworkManagerDeleteConnectPeerRequest,
    NetworkManagerDeleteConnectPeerResponse,
    NetworkManagerDeleteConnectionRequest,
    NetworkManagerDeleteConnectionResponse,
    NetworkManagerDeleteContextStoreRequest,
    NetworkManagerDeleteContextStoreResponse,
    NetworkManagerDeleteCoreNetworkPolicyVersionRequest,
    NetworkManagerDeleteCoreNetworkPolicyVersionResponse,
    NetworkManagerDeleteCoreNetworkPrefixListAssociationRequest,
    NetworkManagerDeleteCoreNetworkPrefixListAssociationResponse,
    NetworkManagerDeleteCoreNetworkRequest,
    NetworkManagerDeleteCoreNetworkResponse,
    NetworkManagerDeleteDeviceRequest,
    NetworkManagerDeleteDeviceResponse,
    NetworkManagerDeleteGlobalNetworkRequest,
    NetworkManagerDeleteGlobalNetworkResponse,
    NetworkManagerDeleteLinkRequest,
    NetworkManagerDeleteLinkResponse,
    NetworkManagerDeletePeeringRequest,
    NetworkManagerDeletePeeringResponse,
    NetworkManagerDeleteResourcePolicyRequest,
    NetworkManagerDeleteResourcePolicyResponse,
    NetworkManagerDeleteSiteRequest,
    NetworkManagerDeleteSiteResponse,
    NetworkManagerDeregisterTransitGatewayRequest,
    NetworkManagerDeregisterTransitGatewayResponse,
    NetworkManagerDescribeGlobalNetworksRequest,
    NetworkManagerDescribeGlobalNetworksResponse,
    NetworkManagerDisassociateConnectPeerRequest,
    NetworkManagerDisassociateConnectPeerResponse,
    NetworkManagerDisassociateContextStoreRequest,
    NetworkManagerDisassociateContextStoreResponse,
    NetworkManagerDisassociateCustomerGatewayRequest,
    NetworkManagerDisassociateCustomerGatewayResponse,
    NetworkManagerDisassociateLinkRequest,
    NetworkManagerDisassociateLinkResponse,
    NetworkManagerDisassociateTransitGatewayConnectPeerRequest,
    NetworkManagerDisassociateTransitGatewayConnectPeerResponse,
    NetworkManagerExecuteCoreNetworkChangeSetRequest,
    NetworkManagerExecuteCoreNetworkChangeSetResponse,
    NetworkManagerGetConnectAttachmentRequest,
    NetworkManagerGetConnectAttachmentResponse,
    NetworkManagerGetConnectPeerAssociationsRequest,
    NetworkManagerGetConnectPeerAssociationsResponse,
    NetworkManagerGetConnectPeerRequest,
    NetworkManagerGetConnectPeerResponse,
    NetworkManagerGetConnectionsRequest,
    NetworkManagerGetConnectionsResponse,
    NetworkManagerGetContextStoreAssociationRequest,
    NetworkManagerGetContextStoreAssociationResponse,
    NetworkManagerGetContextStoreRequest,
    NetworkManagerGetContextStoreResponse,
    NetworkManagerGetContextVersionRequest,
    NetworkManagerGetContextVersionResponse,
    NetworkManagerGetCoreNetworkChangeEventsRequest,
    NetworkManagerGetCoreNetworkChangeEventsResponse,
    NetworkManagerGetCoreNetworkChangeSetRequest,
    NetworkManagerGetCoreNetworkChangeSetResponse,
    NetworkManagerGetCoreNetworkPolicyRequest,
    NetworkManagerGetCoreNetworkPolicyResponse,
    NetworkManagerGetCoreNetworkRequest,
    NetworkManagerGetCoreNetworkResponse,
    NetworkManagerGetCustomerGatewayAssociationsRequest,
    NetworkManagerGetCustomerGatewayAssociationsResponse,
    NetworkManagerGetDevicesRequest,
    NetworkManagerGetDevicesResponse,
    NetworkManagerGetDirectConnectGatewayAttachmentRequest,
    NetworkManagerGetDirectConnectGatewayAttachmentResponse,
    NetworkManagerGetLinkAssociationsRequest,
    NetworkManagerGetLinkAssociationsResponse,
    NetworkManagerGetLinksRequest,
    NetworkManagerGetLinksResponse,
    NetworkManagerGetNetworkResourceCountsRequest,
    NetworkManagerGetNetworkResourceCountsResponse,
    NetworkManagerGetNetworkResourceRelationshipsRequest,
    NetworkManagerGetNetworkResourceRelationshipsResponse,
    NetworkManagerGetNetworkResourcesRequest,
    NetworkManagerGetNetworkResourcesResponse,
    NetworkManagerGetNetworkRoutesRequest,
    NetworkManagerGetNetworkRoutesResponse,
    NetworkManagerGetNetworkTelemetryRequest,
    NetworkManagerGetNetworkTelemetryResponse,
    NetworkManagerGetResourcePolicyRequest,
    NetworkManagerGetResourcePolicyResponse,
    NetworkManagerGetRouteAnalysisRequest,
    NetworkManagerGetRouteAnalysisResponse,
    NetworkManagerGetSiteToSiteVpnAttachmentRequest,
    NetworkManagerGetSiteToSiteVpnAttachmentResponse,
    NetworkManagerGetSitesRequest,
    NetworkManagerGetSitesResponse,
    NetworkManagerGetTransitGatewayConnectPeerAssociationsRequest,
    NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse,
    NetworkManagerGetTransitGatewayPeeringRequest,
    NetworkManagerGetTransitGatewayPeeringResponse,
    NetworkManagerGetTransitGatewayRegistrationsRequest,
    NetworkManagerGetTransitGatewayRegistrationsResponse,
    NetworkManagerGetTransitGatewayRouteTableAttachmentRequest,
    NetworkManagerGetTransitGatewayRouteTableAttachmentResponse,
    NetworkManagerGetVpcAttachmentRequest,
    NetworkManagerGetVpcAttachmentResponse,
    NetworkManagerListAttachmentNatConfigurationsRequest,
    NetworkManagerListAttachmentNatConfigurationsResponse,
    NetworkManagerListAttachmentRoutingPolicyAssociationsRequest,
    NetworkManagerListAttachmentRoutingPolicyAssociationsResponse,
    NetworkManagerListAttachmentsRequest,
    NetworkManagerListAttachmentsResponse,
    NetworkManagerListConnectPeersRequest,
    NetworkManagerListConnectPeersResponse,
    NetworkManagerListContextChangesRequest,
    NetworkManagerListContextChangesResponse,
    NetworkManagerListContextStoreAssociationsRequest,
    NetworkManagerListContextStoreAssociationsResponse,
    NetworkManagerListContextStoresRequest,
    NetworkManagerListContextStoresResponse,
    NetworkManagerListContextsRequest,
    NetworkManagerListContextsResponse,
    NetworkManagerListCoreNetworkPolicyVersionsRequest,
    NetworkManagerListCoreNetworkPolicyVersionsResponse,
    NetworkManagerListCoreNetworkPrefixListAssociationsRequest,
    NetworkManagerListCoreNetworkPrefixListAssociationsResponse,
    NetworkManagerListCoreNetworkRoutingInformationRequest,
    NetworkManagerListCoreNetworkRoutingInformationResponse,
    NetworkManagerListCoreNetworksRequest,
    NetworkManagerListCoreNetworksResponse,
    NetworkManagerListOrganizationServiceAccessStatusRequest,
    NetworkManagerListOrganizationServiceAccessStatusResponse,
    NetworkManagerListPeeringsRequest,
    NetworkManagerListPeeringsResponse,
    NetworkManagerListTagsForResourceRequest,
    NetworkManagerListTagsForResourceResponse,
    NetworkManagerPutAttachmentRoutingPolicyLabelRequest,
    NetworkManagerPutAttachmentRoutingPolicyLabelResponse,
    NetworkManagerPutCoreNetworkPolicyRequest,
    NetworkManagerPutCoreNetworkPolicyResponse,
    NetworkManagerPutResourcePolicyRequest,
    NetworkManagerPutResourcePolicyResponse,
    NetworkManagerRegisterTransitGatewayRequest,
    NetworkManagerRegisterTransitGatewayResponse,
    NetworkManagerRejectAttachmentRequest,
    NetworkManagerRejectAttachmentResponse,
    NetworkManagerRemoveAttachmentRoutingPolicyLabelRequest,
    NetworkManagerRemoveAttachmentRoutingPolicyLabelResponse,
    NetworkManagerRestoreCoreNetworkPolicyVersionRequest,
    NetworkManagerRestoreCoreNetworkPolicyVersionResponse,
    NetworkManagerStartOrganizationServiceAccessUpdateRequest,
    NetworkManagerStartOrganizationServiceAccessUpdateResponse,
    NetworkManagerStartRouteAnalysisRequest,
    NetworkManagerStartRouteAnalysisResponse,
    NetworkManagerTagResourceRequest,
    NetworkManagerTagResourceResponse,
    NetworkManagerUntagResourceRequest,
    NetworkManagerUntagResourceResponse,
    NetworkManagerUpdateAttachmentNatConfigurationRequest,
    NetworkManagerUpdateAttachmentNatConfigurationResponse,
    NetworkManagerUpdateConnectionRequest,
    NetworkManagerUpdateConnectionResponse,
    NetworkManagerUpdateContextStoreRequest,
    NetworkManagerUpdateContextStoreResponse,
    NetworkManagerUpdateCoreNetworkRequest,
    NetworkManagerUpdateCoreNetworkResponse,
    NetworkManagerUpdateDeviceRequest,
    NetworkManagerUpdateDeviceResponse,
    NetworkManagerUpdateDirectConnectGatewayAttachmentRequest,
    NetworkManagerUpdateDirectConnectGatewayAttachmentResponse,
    NetworkManagerUpdateGlobalNetworkRequest,
    NetworkManagerUpdateGlobalNetworkResponse,
    NetworkManagerUpdateLinkRequest,
    NetworkManagerUpdateLinkResponse,
    NetworkManagerUpdateNetworkResourceMetadataRequest,
    NetworkManagerUpdateNetworkResourceMetadataResponse,
    NetworkManagerUpdateSiteRequest,
    NetworkManagerUpdateSiteResponse,
    NetworkManagerUpdateVpcAttachmentRequest,
    NetworkManagerUpdateVpcAttachmentResponse,
)
from werkflow_aws.types.cloud_wan_client import NetworkManagerClient
from .base import AWSBaseService


class AWSNetworkManager(AWSBaseService[NetworkManagerClient]):
    service_name = 'cloud-wan'
    boto3_service_name = 'networkmanager'

    def __init__(self) -> None:
        super().__init__(service_name='cloud-wan', boto3_service_name='networkmanager')

    async def accept_attachment(
        self,
        request: NetworkManagerAcceptAttachmentRequest,
    ) -> NetworkManagerAcceptAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.accept_attachment, request, NetworkManagerAcceptAttachmentResponse)

    async def associate_connect_peer(
        self,
        request: NetworkManagerAssociateConnectPeerRequest,
    ) -> NetworkManagerAssociateConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.associate_connect_peer, request, NetworkManagerAssociateConnectPeerResponse)

    async def associate_context_store(
        self,
        request: NetworkManagerAssociateContextStoreRequest,
    ) -> NetworkManagerAssociateContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.associate_context_store, request, NetworkManagerAssociateContextStoreResponse)

    async def associate_customer_gateway(
        self,
        request: NetworkManagerAssociateCustomerGatewayRequest,
    ) -> NetworkManagerAssociateCustomerGatewayResponse:
        client = self._require_client()
        return await self._execute(client.associate_customer_gateway, request, NetworkManagerAssociateCustomerGatewayResponse)

    async def associate_link(
        self,
        request: NetworkManagerAssociateLinkRequest,
    ) -> NetworkManagerAssociateLinkResponse:
        client = self._require_client()
        return await self._execute(client.associate_link, request, NetworkManagerAssociateLinkResponse)

    async def associate_transit_gateway_connect_peer(
        self,
        request: NetworkManagerAssociateTransitGatewayConnectPeerRequest,
    ) -> NetworkManagerAssociateTransitGatewayConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.associate_transit_gateway_connect_peer, request, NetworkManagerAssociateTransitGatewayConnectPeerResponse)

    async def create_connect_attachment(
        self,
        request: NetworkManagerCreateConnectAttachmentRequest,
    ) -> NetworkManagerCreateConnectAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_connect_attachment, request, NetworkManagerCreateConnectAttachmentResponse)

    async def create_connect_peer(
        self,
        request: NetworkManagerCreateConnectPeerRequest,
    ) -> NetworkManagerCreateConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.create_connect_peer, request, NetworkManagerCreateConnectPeerResponse)

    async def create_connection(
        self,
        request: NetworkManagerCreateConnectionRequest,
    ) -> NetworkManagerCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, NetworkManagerCreateConnectionResponse)

    async def create_context_store(
        self,
        request: NetworkManagerCreateContextStoreRequest,
    ) -> NetworkManagerCreateContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_context_store, request, NetworkManagerCreateContextStoreResponse)

    async def create_core_network(
        self,
        request: NetworkManagerCreateCoreNetworkRequest,
    ) -> NetworkManagerCreateCoreNetworkResponse:
        client = self._require_client()
        return await self._execute(client.create_core_network, request, NetworkManagerCreateCoreNetworkResponse)

    async def create_core_network_prefix_list_association(
        self,
        request: NetworkManagerCreateCoreNetworkPrefixListAssociationRequest,
    ) -> NetworkManagerCreateCoreNetworkPrefixListAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_core_network_prefix_list_association, request, NetworkManagerCreateCoreNetworkPrefixListAssociationResponse)

    async def create_device(
        self,
        request: NetworkManagerCreateDeviceRequest,
    ) -> NetworkManagerCreateDeviceResponse:
        client = self._require_client()
        return await self._execute(client.create_device, request, NetworkManagerCreateDeviceResponse)

    async def create_direct_connect_gateway_attachment(
        self,
        request: NetworkManagerCreateDirectConnectGatewayAttachmentRequest,
    ) -> NetworkManagerCreateDirectConnectGatewayAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_direct_connect_gateway_attachment, request, NetworkManagerCreateDirectConnectGatewayAttachmentResponse)

    async def create_global_network(
        self,
        request: NetworkManagerCreateGlobalNetworkRequest | None = None,
    ) -> NetworkManagerCreateGlobalNetworkResponse:
        client = self._require_client()
        return await self._execute(client.create_global_network, request, NetworkManagerCreateGlobalNetworkResponse)

    async def create_link(
        self,
        request: NetworkManagerCreateLinkRequest,
    ) -> NetworkManagerCreateLinkResponse:
        client = self._require_client()
        return await self._execute(client.create_link, request, NetworkManagerCreateLinkResponse)

    async def create_site(
        self,
        request: NetworkManagerCreateSiteRequest,
    ) -> NetworkManagerCreateSiteResponse:
        client = self._require_client()
        return await self._execute(client.create_site, request, NetworkManagerCreateSiteResponse)

    async def create_site_to_site_vpn_attachment(
        self,
        request: NetworkManagerCreateSiteToSiteVpnAttachmentRequest,
    ) -> NetworkManagerCreateSiteToSiteVpnAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_site_to_site_vpn_attachment, request, NetworkManagerCreateSiteToSiteVpnAttachmentResponse)

    async def create_transit_gateway_peering(
        self,
        request: NetworkManagerCreateTransitGatewayPeeringRequest,
    ) -> NetworkManagerCreateTransitGatewayPeeringResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_peering, request, NetworkManagerCreateTransitGatewayPeeringResponse)

    async def create_transit_gateway_route_table_attachment(
        self,
        request: NetworkManagerCreateTransitGatewayRouteTableAttachmentRequest,
    ) -> NetworkManagerCreateTransitGatewayRouteTableAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_transit_gateway_route_table_attachment, request, NetworkManagerCreateTransitGatewayRouteTableAttachmentResponse)

    async def create_vpc_attachment(
        self,
        request: NetworkManagerCreateVpcAttachmentRequest,
    ) -> NetworkManagerCreateVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_attachment, request, NetworkManagerCreateVpcAttachmentResponse)

    async def delete_attachment(
        self,
        request: NetworkManagerDeleteAttachmentRequest,
    ) -> NetworkManagerDeleteAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_attachment, request, NetworkManagerDeleteAttachmentResponse)

    async def delete_connect_peer(
        self,
        request: NetworkManagerDeleteConnectPeerRequest,
    ) -> NetworkManagerDeleteConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_connect_peer, request, NetworkManagerDeleteConnectPeerResponse)

    async def delete_connection(
        self,
        request: NetworkManagerDeleteConnectionRequest,
    ) -> NetworkManagerDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, NetworkManagerDeleteConnectionResponse)

    async def delete_context_store(
        self,
        request: NetworkManagerDeleteContextStoreRequest,
    ) -> NetworkManagerDeleteContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_context_store, request, NetworkManagerDeleteContextStoreResponse)

    async def delete_core_network(
        self,
        request: NetworkManagerDeleteCoreNetworkRequest,
    ) -> NetworkManagerDeleteCoreNetworkResponse:
        client = self._require_client()
        return await self._execute(client.delete_core_network, request, NetworkManagerDeleteCoreNetworkResponse)

    async def delete_core_network_policy_version(
        self,
        request: NetworkManagerDeleteCoreNetworkPolicyVersionRequest,
    ) -> NetworkManagerDeleteCoreNetworkPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_core_network_policy_version, request, NetworkManagerDeleteCoreNetworkPolicyVersionResponse)

    async def delete_core_network_prefix_list_association(
        self,
        request: NetworkManagerDeleteCoreNetworkPrefixListAssociationRequest,
    ) -> NetworkManagerDeleteCoreNetworkPrefixListAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_core_network_prefix_list_association, request, NetworkManagerDeleteCoreNetworkPrefixListAssociationResponse)

    async def delete_device(
        self,
        request: NetworkManagerDeleteDeviceRequest,
    ) -> NetworkManagerDeleteDeviceResponse:
        client = self._require_client()
        return await self._execute(client.delete_device, request, NetworkManagerDeleteDeviceResponse)

    async def delete_global_network(
        self,
        request: NetworkManagerDeleteGlobalNetworkRequest,
    ) -> NetworkManagerDeleteGlobalNetworkResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_network, request, NetworkManagerDeleteGlobalNetworkResponse)

    async def delete_link(
        self,
        request: NetworkManagerDeleteLinkRequest,
    ) -> NetworkManagerDeleteLinkResponse:
        client = self._require_client()
        return await self._execute(client.delete_link, request, NetworkManagerDeleteLinkResponse)

    async def delete_peering(
        self,
        request: NetworkManagerDeletePeeringRequest,
    ) -> NetworkManagerDeletePeeringResponse:
        client = self._require_client()
        return await self._execute(client.delete_peering, request, NetworkManagerDeletePeeringResponse)

    async def delete_resource_policy(
        self,
        request: NetworkManagerDeleteResourcePolicyRequest,
    ) -> NetworkManagerDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, NetworkManagerDeleteResourcePolicyResponse)

    async def delete_site(
        self,
        request: NetworkManagerDeleteSiteRequest,
    ) -> NetworkManagerDeleteSiteResponse:
        client = self._require_client()
        return await self._execute(client.delete_site, request, NetworkManagerDeleteSiteResponse)

    async def deregister_transit_gateway(
        self,
        request: NetworkManagerDeregisterTransitGatewayRequest,
    ) -> NetworkManagerDeregisterTransitGatewayResponse:
        client = self._require_client()
        return await self._execute(client.deregister_transit_gateway, request, NetworkManagerDeregisterTransitGatewayResponse)

    async def describe_global_networks(
        self,
        request: NetworkManagerDescribeGlobalNetworksRequest | None = None,
    ) -> NetworkManagerDescribeGlobalNetworksResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_networks, request, NetworkManagerDescribeGlobalNetworksResponse)

    async def describe_global_networks_paginated(
        self,
        request: NetworkManagerDescribeGlobalNetworksRequest | None = None,
    ) -> list[NetworkManagerDescribeGlobalNetworksResponse]:
        return await self._paginate('describe_global_networks', request, NetworkManagerDescribeGlobalNetworksResponse)

    async def disassociate_connect_peer(
        self,
        request: NetworkManagerDisassociateConnectPeerRequest,
    ) -> NetworkManagerDisassociateConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_connect_peer, request, NetworkManagerDisassociateConnectPeerResponse)

    async def disassociate_context_store(
        self,
        request: NetworkManagerDisassociateContextStoreRequest,
    ) -> NetworkManagerDisassociateContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_context_store, request, NetworkManagerDisassociateContextStoreResponse)

    async def disassociate_customer_gateway(
        self,
        request: NetworkManagerDisassociateCustomerGatewayRequest,
    ) -> NetworkManagerDisassociateCustomerGatewayResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_customer_gateway, request, NetworkManagerDisassociateCustomerGatewayResponse)

    async def disassociate_link(
        self,
        request: NetworkManagerDisassociateLinkRequest,
    ) -> NetworkManagerDisassociateLinkResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_link, request, NetworkManagerDisassociateLinkResponse)

    async def disassociate_transit_gateway_connect_peer(
        self,
        request: NetworkManagerDisassociateTransitGatewayConnectPeerRequest,
    ) -> NetworkManagerDisassociateTransitGatewayConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_transit_gateway_connect_peer, request, NetworkManagerDisassociateTransitGatewayConnectPeerResponse)

    async def execute_core_network_change_set(
        self,
        request: NetworkManagerExecuteCoreNetworkChangeSetRequest,
    ) -> NetworkManagerExecuteCoreNetworkChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.execute_core_network_change_set, request, NetworkManagerExecuteCoreNetworkChangeSetResponse)

    async def get_connect_attachment(
        self,
        request: NetworkManagerGetConnectAttachmentRequest,
    ) -> NetworkManagerGetConnectAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.get_connect_attachment, request, NetworkManagerGetConnectAttachmentResponse)

    async def get_connect_peer(
        self,
        request: NetworkManagerGetConnectPeerRequest,
    ) -> NetworkManagerGetConnectPeerResponse:
        client = self._require_client()
        return await self._execute(client.get_connect_peer, request, NetworkManagerGetConnectPeerResponse)

    async def get_connect_peer_associations(
        self,
        request: NetworkManagerGetConnectPeerAssociationsRequest,
    ) -> NetworkManagerGetConnectPeerAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_connect_peer_associations, request, NetworkManagerGetConnectPeerAssociationsResponse)

    async def get_connect_peer_associations_paginated(
        self,
        request: NetworkManagerGetConnectPeerAssociationsRequest,
    ) -> list[NetworkManagerGetConnectPeerAssociationsResponse]:
        return await self._paginate('get_connect_peer_associations', request, NetworkManagerGetConnectPeerAssociationsResponse)

    async def get_connections(
        self,
        request: NetworkManagerGetConnectionsRequest,
    ) -> NetworkManagerGetConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.get_connections, request, NetworkManagerGetConnectionsResponse)

    async def get_connections_paginated(
        self,
        request: NetworkManagerGetConnectionsRequest,
    ) -> list[NetworkManagerGetConnectionsResponse]:
        return await self._paginate('get_connections', request, NetworkManagerGetConnectionsResponse)

    async def get_context_store(
        self,
        request: NetworkManagerGetContextStoreRequest,
    ) -> NetworkManagerGetContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.get_context_store, request, NetworkManagerGetContextStoreResponse)

    async def get_context_store_association(
        self,
        request: NetworkManagerGetContextStoreAssociationRequest,
    ) -> NetworkManagerGetContextStoreAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_context_store_association, request, NetworkManagerGetContextStoreAssociationResponse)

    async def get_context_version(
        self,
        request: NetworkManagerGetContextVersionRequest,
    ) -> NetworkManagerGetContextVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_context_version, request, NetworkManagerGetContextVersionResponse)

    async def get_core_network(
        self,
        request: NetworkManagerGetCoreNetworkRequest,
    ) -> NetworkManagerGetCoreNetworkResponse:
        client = self._require_client()
        return await self._execute(client.get_core_network, request, NetworkManagerGetCoreNetworkResponse)

    async def get_core_network_change_events(
        self,
        request: NetworkManagerGetCoreNetworkChangeEventsRequest,
    ) -> NetworkManagerGetCoreNetworkChangeEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_core_network_change_events, request, NetworkManagerGetCoreNetworkChangeEventsResponse)

    async def get_core_network_change_events_paginated(
        self,
        request: NetworkManagerGetCoreNetworkChangeEventsRequest,
    ) -> list[NetworkManagerGetCoreNetworkChangeEventsResponse]:
        return await self._paginate('get_core_network_change_events', request, NetworkManagerGetCoreNetworkChangeEventsResponse)

    async def get_core_network_change_set(
        self,
        request: NetworkManagerGetCoreNetworkChangeSetRequest,
    ) -> NetworkManagerGetCoreNetworkChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.get_core_network_change_set, request, NetworkManagerGetCoreNetworkChangeSetResponse)

    async def get_core_network_change_set_paginated(
        self,
        request: NetworkManagerGetCoreNetworkChangeSetRequest,
    ) -> list[NetworkManagerGetCoreNetworkChangeSetResponse]:
        return await self._paginate('get_core_network_change_set', request, NetworkManagerGetCoreNetworkChangeSetResponse)

    async def get_core_network_policy(
        self,
        request: NetworkManagerGetCoreNetworkPolicyRequest,
    ) -> NetworkManagerGetCoreNetworkPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_core_network_policy, request, NetworkManagerGetCoreNetworkPolicyResponse)

    async def get_customer_gateway_associations(
        self,
        request: NetworkManagerGetCustomerGatewayAssociationsRequest,
    ) -> NetworkManagerGetCustomerGatewayAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_customer_gateway_associations, request, NetworkManagerGetCustomerGatewayAssociationsResponse)

    async def get_customer_gateway_associations_paginated(
        self,
        request: NetworkManagerGetCustomerGatewayAssociationsRequest,
    ) -> list[NetworkManagerGetCustomerGatewayAssociationsResponse]:
        return await self._paginate('get_customer_gateway_associations', request, NetworkManagerGetCustomerGatewayAssociationsResponse)

    async def get_devices(
        self,
        request: NetworkManagerGetDevicesRequest,
    ) -> NetworkManagerGetDevicesResponse:
        client = self._require_client()
        return await self._execute(client.get_devices, request, NetworkManagerGetDevicesResponse)

    async def get_devices_paginated(
        self,
        request: NetworkManagerGetDevicesRequest,
    ) -> list[NetworkManagerGetDevicesResponse]:
        return await self._paginate('get_devices', request, NetworkManagerGetDevicesResponse)

    async def get_direct_connect_gateway_attachment(
        self,
        request: NetworkManagerGetDirectConnectGatewayAttachmentRequest,
    ) -> NetworkManagerGetDirectConnectGatewayAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.get_direct_connect_gateway_attachment, request, NetworkManagerGetDirectConnectGatewayAttachmentResponse)

    async def get_link_associations(
        self,
        request: NetworkManagerGetLinkAssociationsRequest,
    ) -> NetworkManagerGetLinkAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_link_associations, request, NetworkManagerGetLinkAssociationsResponse)

    async def get_link_associations_paginated(
        self,
        request: NetworkManagerGetLinkAssociationsRequest,
    ) -> list[NetworkManagerGetLinkAssociationsResponse]:
        return await self._paginate('get_link_associations', request, NetworkManagerGetLinkAssociationsResponse)

    async def get_links(
        self,
        request: NetworkManagerGetLinksRequest,
    ) -> NetworkManagerGetLinksResponse:
        client = self._require_client()
        return await self._execute(client.get_links, request, NetworkManagerGetLinksResponse)

    async def get_links_paginated(
        self,
        request: NetworkManagerGetLinksRequest,
    ) -> list[NetworkManagerGetLinksResponse]:
        return await self._paginate('get_links', request, NetworkManagerGetLinksResponse)

    async def get_network_resource_counts(
        self,
        request: NetworkManagerGetNetworkResourceCountsRequest,
    ) -> NetworkManagerGetNetworkResourceCountsResponse:
        client = self._require_client()
        return await self._execute(client.get_network_resource_counts, request, NetworkManagerGetNetworkResourceCountsResponse)

    async def get_network_resource_counts_paginated(
        self,
        request: NetworkManagerGetNetworkResourceCountsRequest,
    ) -> list[NetworkManagerGetNetworkResourceCountsResponse]:
        return await self._paginate('get_network_resource_counts', request, NetworkManagerGetNetworkResourceCountsResponse)

    async def get_network_resource_relationships(
        self,
        request: NetworkManagerGetNetworkResourceRelationshipsRequest,
    ) -> NetworkManagerGetNetworkResourceRelationshipsResponse:
        client = self._require_client()
        return await self._execute(client.get_network_resource_relationships, request, NetworkManagerGetNetworkResourceRelationshipsResponse)

    async def get_network_resource_relationships_paginated(
        self,
        request: NetworkManagerGetNetworkResourceRelationshipsRequest,
    ) -> list[NetworkManagerGetNetworkResourceRelationshipsResponse]:
        return await self._paginate('get_network_resource_relationships', request, NetworkManagerGetNetworkResourceRelationshipsResponse)

    async def get_network_resources(
        self,
        request: NetworkManagerGetNetworkResourcesRequest,
    ) -> NetworkManagerGetNetworkResourcesResponse:
        client = self._require_client()
        return await self._execute(client.get_network_resources, request, NetworkManagerGetNetworkResourcesResponse)

    async def get_network_resources_paginated(
        self,
        request: NetworkManagerGetNetworkResourcesRequest,
    ) -> list[NetworkManagerGetNetworkResourcesResponse]:
        return await self._paginate('get_network_resources', request, NetworkManagerGetNetworkResourcesResponse)

    async def get_network_routes(
        self,
        request: NetworkManagerGetNetworkRoutesRequest,
    ) -> NetworkManagerGetNetworkRoutesResponse:
        client = self._require_client()
        return await self._execute(client.get_network_routes, request, NetworkManagerGetNetworkRoutesResponse)

    async def get_network_routes_paginated(
        self,
        request: NetworkManagerGetNetworkRoutesRequest,
    ) -> list[NetworkManagerGetNetworkRoutesResponse]:
        return await self._paginate('get_network_routes', request, NetworkManagerGetNetworkRoutesResponse)

    async def get_network_telemetry(
        self,
        request: NetworkManagerGetNetworkTelemetryRequest,
    ) -> NetworkManagerGetNetworkTelemetryResponse:
        client = self._require_client()
        return await self._execute(client.get_network_telemetry, request, NetworkManagerGetNetworkTelemetryResponse)

    async def get_network_telemetry_paginated(
        self,
        request: NetworkManagerGetNetworkTelemetryRequest,
    ) -> list[NetworkManagerGetNetworkTelemetryResponse]:
        return await self._paginate('get_network_telemetry', request, NetworkManagerGetNetworkTelemetryResponse)

    async def get_resource_policy(
        self,
        request: NetworkManagerGetResourcePolicyRequest,
    ) -> NetworkManagerGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, NetworkManagerGetResourcePolicyResponse)

    async def get_route_analysis(
        self,
        request: NetworkManagerGetRouteAnalysisRequest,
    ) -> NetworkManagerGetRouteAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_route_analysis, request, NetworkManagerGetRouteAnalysisResponse)

    async def get_site_to_site_vpn_attachment(
        self,
        request: NetworkManagerGetSiteToSiteVpnAttachmentRequest,
    ) -> NetworkManagerGetSiteToSiteVpnAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.get_site_to_site_vpn_attachment, request, NetworkManagerGetSiteToSiteVpnAttachmentResponse)

    async def get_sites(
        self,
        request: NetworkManagerGetSitesRequest,
    ) -> NetworkManagerGetSitesResponse:
        client = self._require_client()
        return await self._execute(client.get_sites, request, NetworkManagerGetSitesResponse)

    async def get_sites_paginated(
        self,
        request: NetworkManagerGetSitesRequest,
    ) -> list[NetworkManagerGetSitesResponse]:
        return await self._paginate('get_sites', request, NetworkManagerGetSitesResponse)

    async def get_transit_gateway_connect_peer_associations(
        self,
        request: NetworkManagerGetTransitGatewayConnectPeerAssociationsRequest,
    ) -> NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_connect_peer_associations, request, NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse)

    async def get_transit_gateway_connect_peer_associations_paginated(
        self,
        request: NetworkManagerGetTransitGatewayConnectPeerAssociationsRequest,
    ) -> list[NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse]:
        return await self._paginate('get_transit_gateway_connect_peer_associations', request, NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse)

    async def get_transit_gateway_peering(
        self,
        request: NetworkManagerGetTransitGatewayPeeringRequest,
    ) -> NetworkManagerGetTransitGatewayPeeringResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_peering, request, NetworkManagerGetTransitGatewayPeeringResponse)

    async def get_transit_gateway_registrations(
        self,
        request: NetworkManagerGetTransitGatewayRegistrationsRequest,
    ) -> NetworkManagerGetTransitGatewayRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_registrations, request, NetworkManagerGetTransitGatewayRegistrationsResponse)

    async def get_transit_gateway_registrations_paginated(
        self,
        request: NetworkManagerGetTransitGatewayRegistrationsRequest,
    ) -> list[NetworkManagerGetTransitGatewayRegistrationsResponse]:
        return await self._paginate('get_transit_gateway_registrations', request, NetworkManagerGetTransitGatewayRegistrationsResponse)

    async def get_transit_gateway_route_table_attachment(
        self,
        request: NetworkManagerGetTransitGatewayRouteTableAttachmentRequest,
    ) -> NetworkManagerGetTransitGatewayRouteTableAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.get_transit_gateway_route_table_attachment, request, NetworkManagerGetTransitGatewayRouteTableAttachmentResponse)

    async def get_vpc_attachment(
        self,
        request: NetworkManagerGetVpcAttachmentRequest,
    ) -> NetworkManagerGetVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_attachment, request, NetworkManagerGetVpcAttachmentResponse)

    async def list_attachment_nat_configurations(
        self,
        request: NetworkManagerListAttachmentNatConfigurationsRequest | None = None,
    ) -> NetworkManagerListAttachmentNatConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_attachment_nat_configurations, request, NetworkManagerListAttachmentNatConfigurationsResponse)

    async def list_attachment_nat_configurations_paginated(
        self,
        request: NetworkManagerListAttachmentNatConfigurationsRequest | None = None,
    ) -> list[NetworkManagerListAttachmentNatConfigurationsResponse]:
        return await self._paginate('list_attachment_nat_configurations', request, NetworkManagerListAttachmentNatConfigurationsResponse)

    async def list_attachment_routing_policy_associations(
        self,
        request: NetworkManagerListAttachmentRoutingPolicyAssociationsRequest,
    ) -> NetworkManagerListAttachmentRoutingPolicyAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_attachment_routing_policy_associations, request, NetworkManagerListAttachmentRoutingPolicyAssociationsResponse)

    async def list_attachment_routing_policy_associations_paginated(
        self,
        request: NetworkManagerListAttachmentRoutingPolicyAssociationsRequest,
    ) -> list[NetworkManagerListAttachmentRoutingPolicyAssociationsResponse]:
        return await self._paginate('list_attachment_routing_policy_associations', request, NetworkManagerListAttachmentRoutingPolicyAssociationsResponse)

    async def list_attachments(
        self,
        request: NetworkManagerListAttachmentsRequest | None = None,
    ) -> NetworkManagerListAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_attachments, request, NetworkManagerListAttachmentsResponse)

    async def list_attachments_paginated(
        self,
        request: NetworkManagerListAttachmentsRequest | None = None,
    ) -> list[NetworkManagerListAttachmentsResponse]:
        return await self._paginate('list_attachments', request, NetworkManagerListAttachmentsResponse)

    async def list_connect_peers(
        self,
        request: NetworkManagerListConnectPeersRequest | None = None,
    ) -> NetworkManagerListConnectPeersResponse:
        client = self._require_client()
        return await self._execute(client.list_connect_peers, request, NetworkManagerListConnectPeersResponse)

    async def list_connect_peers_paginated(
        self,
        request: NetworkManagerListConnectPeersRequest | None = None,
    ) -> list[NetworkManagerListConnectPeersResponse]:
        return await self._paginate('list_connect_peers', request, NetworkManagerListConnectPeersResponse)

    async def list_context_changes(
        self,
        request: NetworkManagerListContextChangesRequest,
    ) -> NetworkManagerListContextChangesResponse:
        client = self._require_client()
        return await self._execute(client.list_context_changes, request, NetworkManagerListContextChangesResponse)

    async def list_context_changes_paginated(
        self,
        request: NetworkManagerListContextChangesRequest,
    ) -> list[NetworkManagerListContextChangesResponse]:
        return await self._paginate('list_context_changes', request, NetworkManagerListContextChangesResponse)

    async def list_context_store_associations(
        self,
        request: NetworkManagerListContextStoreAssociationsRequest,
    ) -> NetworkManagerListContextStoreAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_context_store_associations, request, NetworkManagerListContextStoreAssociationsResponse)

    async def list_context_store_associations_paginated(
        self,
        request: NetworkManagerListContextStoreAssociationsRequest,
    ) -> list[NetworkManagerListContextStoreAssociationsResponse]:
        return await self._paginate('list_context_store_associations', request, NetworkManagerListContextStoreAssociationsResponse)

    async def list_context_stores(
        self,
        request: NetworkManagerListContextStoresRequest | None = None,
    ) -> NetworkManagerListContextStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_context_stores, request, NetworkManagerListContextStoresResponse)

    async def list_context_stores_paginated(
        self,
        request: NetworkManagerListContextStoresRequest | None = None,
    ) -> list[NetworkManagerListContextStoresResponse]:
        return await self._paginate('list_context_stores', request, NetworkManagerListContextStoresResponse)

    async def list_contexts(
        self,
        request: NetworkManagerListContextsRequest,
    ) -> NetworkManagerListContextsResponse:
        client = self._require_client()
        return await self._execute(client.list_contexts, request, NetworkManagerListContextsResponse)

    async def list_contexts_paginated(
        self,
        request: NetworkManagerListContextsRequest,
    ) -> list[NetworkManagerListContextsResponse]:
        return await self._paginate('list_contexts', request, NetworkManagerListContextsResponse)

    async def list_core_network_policy_versions(
        self,
        request: NetworkManagerListCoreNetworkPolicyVersionsRequest,
    ) -> NetworkManagerListCoreNetworkPolicyVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_core_network_policy_versions, request, NetworkManagerListCoreNetworkPolicyVersionsResponse)

    async def list_core_network_policy_versions_paginated(
        self,
        request: NetworkManagerListCoreNetworkPolicyVersionsRequest,
    ) -> list[NetworkManagerListCoreNetworkPolicyVersionsResponse]:
        return await self._paginate('list_core_network_policy_versions', request, NetworkManagerListCoreNetworkPolicyVersionsResponse)

    async def list_core_network_prefix_list_associations(
        self,
        request: NetworkManagerListCoreNetworkPrefixListAssociationsRequest,
    ) -> NetworkManagerListCoreNetworkPrefixListAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_core_network_prefix_list_associations, request, NetworkManagerListCoreNetworkPrefixListAssociationsResponse)

    async def list_core_network_prefix_list_associations_paginated(
        self,
        request: NetworkManagerListCoreNetworkPrefixListAssociationsRequest,
    ) -> list[NetworkManagerListCoreNetworkPrefixListAssociationsResponse]:
        return await self._paginate('list_core_network_prefix_list_associations', request, NetworkManagerListCoreNetworkPrefixListAssociationsResponse)

    async def list_core_network_routing_information(
        self,
        request: NetworkManagerListCoreNetworkRoutingInformationRequest,
    ) -> NetworkManagerListCoreNetworkRoutingInformationResponse:
        client = self._require_client()
        return await self._execute(client.list_core_network_routing_information, request, NetworkManagerListCoreNetworkRoutingInformationResponse)

    async def list_core_network_routing_information_paginated(
        self,
        request: NetworkManagerListCoreNetworkRoutingInformationRequest,
    ) -> list[NetworkManagerListCoreNetworkRoutingInformationResponse]:
        return await self._paginate('list_core_network_routing_information', request, NetworkManagerListCoreNetworkRoutingInformationResponse)

    async def list_core_networks(
        self,
        request: NetworkManagerListCoreNetworksRequest | None = None,
    ) -> NetworkManagerListCoreNetworksResponse:
        client = self._require_client()
        return await self._execute(client.list_core_networks, request, NetworkManagerListCoreNetworksResponse)

    async def list_core_networks_paginated(
        self,
        request: NetworkManagerListCoreNetworksRequest | None = None,
    ) -> list[NetworkManagerListCoreNetworksResponse]:
        return await self._paginate('list_core_networks', request, NetworkManagerListCoreNetworksResponse)

    async def list_organization_service_access_status(
        self,
        request: NetworkManagerListOrganizationServiceAccessStatusRequest | None = None,
    ) -> NetworkManagerListOrganizationServiceAccessStatusResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_service_access_status, request, NetworkManagerListOrganizationServiceAccessStatusResponse)

    async def list_peerings(
        self,
        request: NetworkManagerListPeeringsRequest | None = None,
    ) -> NetworkManagerListPeeringsResponse:
        client = self._require_client()
        return await self._execute(client.list_peerings, request, NetworkManagerListPeeringsResponse)

    async def list_peerings_paginated(
        self,
        request: NetworkManagerListPeeringsRequest | None = None,
    ) -> list[NetworkManagerListPeeringsResponse]:
        return await self._paginate('list_peerings', request, NetworkManagerListPeeringsResponse)

    async def list_tags_for_resource(
        self,
        request: NetworkManagerListTagsForResourceRequest,
    ) -> NetworkManagerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, NetworkManagerListTagsForResourceResponse)

    async def put_attachment_routing_policy_label(
        self,
        request: NetworkManagerPutAttachmentRoutingPolicyLabelRequest,
    ) -> NetworkManagerPutAttachmentRoutingPolicyLabelResponse:
        client = self._require_client()
        return await self._execute(client.put_attachment_routing_policy_label, request, NetworkManagerPutAttachmentRoutingPolicyLabelResponse)

    async def put_core_network_policy(
        self,
        request: NetworkManagerPutCoreNetworkPolicyRequest,
    ) -> NetworkManagerPutCoreNetworkPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_core_network_policy, request, NetworkManagerPutCoreNetworkPolicyResponse)

    async def put_resource_policy(
        self,
        request: NetworkManagerPutResourcePolicyRequest,
    ) -> NetworkManagerPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, NetworkManagerPutResourcePolicyResponse)

    async def register_transit_gateway(
        self,
        request: NetworkManagerRegisterTransitGatewayRequest,
    ) -> NetworkManagerRegisterTransitGatewayResponse:
        client = self._require_client()
        return await self._execute(client.register_transit_gateway, request, NetworkManagerRegisterTransitGatewayResponse)

    async def reject_attachment(
        self,
        request: NetworkManagerRejectAttachmentRequest,
    ) -> NetworkManagerRejectAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.reject_attachment, request, NetworkManagerRejectAttachmentResponse)

    async def remove_attachment_routing_policy_label(
        self,
        request: NetworkManagerRemoveAttachmentRoutingPolicyLabelRequest,
    ) -> NetworkManagerRemoveAttachmentRoutingPolicyLabelResponse:
        client = self._require_client()
        return await self._execute(client.remove_attachment_routing_policy_label, request, NetworkManagerRemoveAttachmentRoutingPolicyLabelResponse)

    async def restore_core_network_policy_version(
        self,
        request: NetworkManagerRestoreCoreNetworkPolicyVersionRequest,
    ) -> NetworkManagerRestoreCoreNetworkPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.restore_core_network_policy_version, request, NetworkManagerRestoreCoreNetworkPolicyVersionResponse)

    async def start_organization_service_access_update(
        self,
        request: NetworkManagerStartOrganizationServiceAccessUpdateRequest,
    ) -> NetworkManagerStartOrganizationServiceAccessUpdateResponse:
        client = self._require_client()
        return await self._execute(client.start_organization_service_access_update, request, NetworkManagerStartOrganizationServiceAccessUpdateResponse)

    async def start_route_analysis(
        self,
        request: NetworkManagerStartRouteAnalysisRequest,
    ) -> NetworkManagerStartRouteAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_route_analysis, request, NetworkManagerStartRouteAnalysisResponse)

    async def tag_resource(
        self,
        request: NetworkManagerTagResourceRequest,
    ) -> NetworkManagerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, NetworkManagerTagResourceResponse)

    async def untag_resource(
        self,
        request: NetworkManagerUntagResourceRequest,
    ) -> NetworkManagerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, NetworkManagerUntagResourceResponse)

    async def update_attachment_nat_configuration(
        self,
        request: NetworkManagerUpdateAttachmentNatConfigurationRequest,
    ) -> NetworkManagerUpdateAttachmentNatConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_attachment_nat_configuration, request, NetworkManagerUpdateAttachmentNatConfigurationResponse)

    async def update_connection(
        self,
        request: NetworkManagerUpdateConnectionRequest,
    ) -> NetworkManagerUpdateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection, request, NetworkManagerUpdateConnectionResponse)

    async def update_context_store(
        self,
        request: NetworkManagerUpdateContextStoreRequest,
    ) -> NetworkManagerUpdateContextStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_context_store, request, NetworkManagerUpdateContextStoreResponse)

    async def update_core_network(
        self,
        request: NetworkManagerUpdateCoreNetworkRequest,
    ) -> NetworkManagerUpdateCoreNetworkResponse:
        client = self._require_client()
        return await self._execute(client.update_core_network, request, NetworkManagerUpdateCoreNetworkResponse)

    async def update_device(
        self,
        request: NetworkManagerUpdateDeviceRequest,
    ) -> NetworkManagerUpdateDeviceResponse:
        client = self._require_client()
        return await self._execute(client.update_device, request, NetworkManagerUpdateDeviceResponse)

    async def update_direct_connect_gateway_attachment(
        self,
        request: NetworkManagerUpdateDirectConnectGatewayAttachmentRequest,
    ) -> NetworkManagerUpdateDirectConnectGatewayAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.update_direct_connect_gateway_attachment, request, NetworkManagerUpdateDirectConnectGatewayAttachmentResponse)

    async def update_global_network(
        self,
        request: NetworkManagerUpdateGlobalNetworkRequest,
    ) -> NetworkManagerUpdateGlobalNetworkResponse:
        client = self._require_client()
        return await self._execute(client.update_global_network, request, NetworkManagerUpdateGlobalNetworkResponse)

    async def update_link(
        self,
        request: NetworkManagerUpdateLinkRequest,
    ) -> NetworkManagerUpdateLinkResponse:
        client = self._require_client()
        return await self._execute(client.update_link, request, NetworkManagerUpdateLinkResponse)

    async def update_network_resource_metadata(
        self,
        request: NetworkManagerUpdateNetworkResourceMetadataRequest,
    ) -> NetworkManagerUpdateNetworkResourceMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_network_resource_metadata, request, NetworkManagerUpdateNetworkResourceMetadataResponse)

    async def update_site(
        self,
        request: NetworkManagerUpdateSiteRequest,
    ) -> NetworkManagerUpdateSiteResponse:
        client = self._require_client()
        return await self._execute(client.update_site, request, NetworkManagerUpdateSiteResponse)

    async def update_vpc_attachment(
        self,
        request: NetworkManagerUpdateVpcAttachmentRequest,
    ) -> NetworkManagerUpdateVpcAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_attachment, request, NetworkManagerUpdateVpcAttachmentResponse)

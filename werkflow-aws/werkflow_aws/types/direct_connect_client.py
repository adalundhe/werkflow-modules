from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class DirectConnectClient(ABC):

    @abstractmethod
    def accept_direct_connect_gateway_association_proposal(
        self,
        *,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_connection_on_interconnect(
        self,
        *,
        bandwidth: str,
        connectionName: str,
        ownerAccount: str,
        interconnectId: str,
        vlan: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_hosted_connection(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_private_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_public_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_transit_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_connection_with_lag(
        self,
        *,
        connectionId: str,
        lagId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_connections_to_resiliency_group(
        self,
        *,
        connectionIdentifiers: list[str],
        resiliencyGroupId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_hosted_connection(
        self,
        *,
        connectionId: str,
        parentConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_mac_sec_key(
        self,
        *,
        connectionId: str,
        secretARN: str | None = None,
        ckn: str | None = None,
        cak: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
        connectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_connection(
        self,
        *,
        connectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_customer_agreement(
        self,
        *,
        agreementName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_private_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
        virtualGatewayId: str | None = None,
        directConnectGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_public_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_transit_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
        directConnectGatewayId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bgp_peer(
        self,
        *,
        virtualInterfaceId: str | None = None,
        newBGPPeer: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        providerName: str | None = None,
        requestMACSec: bool | None = None,
        billingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_direct_connect_gateway(
        self,
        *,
        directConnectGatewayName: str,
        tags: list[dict[str, Any]] | None = None,
        amazonSideAsn: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_direct_connect_gateway_association(
        self,
        *,
        directConnectGatewayId: str,
        gatewayId: str | None = None,
        addAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
        virtualGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_direct_connect_gateway_association_proposal(
        self,
        *,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
        removeAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_interconnect(
        self,
        *,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        providerName: str | None = None,
        requestMACSec: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lag(
        self,
        *,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        childConnectionTags: list[dict[str, Any]] | None = None,
        providerName: str | None = None,
        requestMACSec: bool | None = None,
        billingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_private_virtual_interface(
        self,
        *,
        connectionId: str,
        newPrivateVirtualInterface: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_public_virtual_interface(
        self,
        *,
        connectionId: str,
        newPublicVirtualInterface: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resiliency_group(
        self,
        *,
        resiliencyGroupName: str,
        intendedResiliencyModel: str,
        clientToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_virtual_interface(
        self,
        *,
        connectionId: str,
        newTransitVirtualInterface: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bgp_peer(
        self,
        *,
        virtualInterfaceId: str | None = None,
        asn: int | None = None,
        asnLong: int | None = None,
        customerAddress: str | None = None,
        bgpPeerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        connectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_direct_connect_gateway(
        self,
        *,
        directConnectGatewayId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_direct_connect_gateway_association(
        self,
        *,
        associationId: str | None = None,
        directConnectGatewayId: str | None = None,
        virtualGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_direct_connect_gateway_association_proposal(
        self,
        *,
        proposalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_interconnect(
        self,
        *,
        interconnectId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lag(
        self,
        *,
        lagId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resiliency_group(
        self,
        *,
        resiliencyGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection_loa(
        self,
        *,
        connectionId: str,
        providerName: str | None = None,
        loaContentType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connections(
        self,
        *,
        connectionId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connections_on_interconnect(
        self,
        *,
        interconnectId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_customer_metadata(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_direct_connect_gateway_association_proposals(
        self,
        *,
        directConnectGatewayId: str | None = None,
        proposalId: str | None = None,
        associatedGatewayId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_direct_connect_gateway_associations(
        self,
        *,
        associationId: str | None = None,
        associatedGatewayId: str | None = None,
        directConnectGatewayId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        virtualGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_direct_connect_gateway_attachments(
        self,
        *,
        directConnectGatewayId: str | None = None,
        virtualInterfaceId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_direct_connect_gateways(
        self,
        *,
        directConnectGatewayId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hosted_connections(
        self,
        *,
        connectionId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_interconnect_loa(
        self,
        *,
        interconnectId: str,
        providerName: str | None = None,
        loaContentType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_interconnects(
        self,
        *,
        interconnectId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lags(
        self,
        *,
        lagId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_loa(
        self,
        *,
        connectionId: str,
        providerName: str | None = None,
        loaContentType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_locations(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_router_configuration(
        self,
        *,
        virtualInterfaceId: str,
        routerTypeIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        resourceArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_virtual_gateways(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_virtual_interfaces(
        self,
        *,
        connectionId: str | None = None,
        virtualInterfaceId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_connection_from_lag(
        self,
        *,
        connectionId: str,
        lagId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_connections_from_resiliency_group(
        self,
        *,
        connectionIdentifiers: list[str],
        resiliencyGroupId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_mac_sec_key(
        self,
        *,
        connectionId: str,
        secretARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resiliency_group(
        self,
        *,
        resiliencyGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resiliency_group_associations(
        self,
        *,
        resiliencyGroupId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resiliency_groups(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_virtual_interface_routes(
        self,
        *,
        virtualInterfaceId: str | None = None,
        filters: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_virtual_interface_test_history(
        self,
        *,
        testId: str | None = None,
        virtualInterfaceId: str | None = None,
        bgpPeers: list[str] | None = None,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_bgp_failover_test(
        self,
        *,
        virtualInterfaceId: str,
        bgpPeers: list[str] | None = None,
        testDurationInMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_bgp_failover_test(
        self,
        *,
        virtualInterfaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection(
        self,
        *,
        connectionId: str,
        connectionName: str | None = None,
        encryptionMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connections_billing_mode(
        self,
        *,
        connectionIds: list[str],
        billingMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_direct_connect_gateway(
        self,
        *,
        directConnectGatewayId: str,
        newDirectConnectGatewayName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_direct_connect_gateway_association(
        self,
        *,
        associationId: str | None = None,
        addAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
        removeAllowedPrefixesToDirectConnectGateway: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lag(
        self,
        *,
        lagId: str,
        lagName: str | None = None,
        minimumLinks: int | None = None,
        encryptionMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resiliency_group(
        self,
        *,
        resiliencyGroupId: str,
        resiliencyGroupName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_virtual_interface_attributes(
        self,
        *,
        virtualInterfaceId: str,
        mtu: int | None = None,
        enableSiteLink: bool | None = None,
        virtualInterfaceName: str | None = None,
        prefixPoolAllocatedCountIpv4: int | None = None,
        prefixPoolAllocatedCountIpv6: int | None = None,
        rateLimit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

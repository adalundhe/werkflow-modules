from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class NetworkManagerClient(ABC):

    @abstractmethod
    def accept_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_connect_peer(
        self,
        *,
        GlobalNetworkId: str,
        ConnectPeerId: str,
        DeviceId: str,
        LinkId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_context_store(
        self,
        *,
        ContextStoreId: str,
        TransitGatewayArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_customer_gateway(
        self,
        *,
        CustomerGatewayArn: str,
        GlobalNetworkId: str,
        DeviceId: str,
        LinkId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_link(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        LinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_transit_gateway_connect_peer(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArn: str,
        DeviceId: str,
        LinkId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connect_attachment(
        self,
        *,
        CoreNetworkId: str,
        EdgeLocation: str,
        TransportAttachmentId: str,
        Options: dict[str, Any],
        RoutingPolicyLabel: str | None = None,
        NatGatewaySupport: str | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connect_peer(
        self,
        *,
        ConnectAttachmentId: str,
        PeerAddress: str,
        CoreNetworkAddress: str | None = None,
        BgpOptions: dict[str, Any] | None = None,
        InsideCidrBlocks: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        SubnetArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        ConnectedDeviceId: str,
        LinkId: str | None = None,
        ConnectedLinkId: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_context_store(
        self,
        *,
        GlobalNetworkId: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_core_network(
        self,
        *,
        GlobalNetworkId: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        PolicyDocument: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_core_network_prefix_list_association(
        self,
        *,
        CoreNetworkId: str,
        PrefixListArn: str,
        PrefixListAlias: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_device(
        self,
        *,
        GlobalNetworkId: str,
        AWSLocation: dict[str, Any] | None = None,
        Description: str | None = None,
        Type: str | None = None,
        Vendor: str | None = None,
        Model: str | None = None,
        SerialNumber: str | None = None,
        Location: dict[str, Any] | None = None,
        SiteId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_direct_connect_gateway_attachment(
        self,
        *,
        CoreNetworkId: str,
        DirectConnectGatewayArn: str,
        EdgeLocations: list[str],
        RoutingPolicyLabel: str | None = None,
        NatGatewaySupport: str | None = None,
        NatSystemRouteSupport: bool | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_global_network(
        self,
        *,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_link(
        self,
        *,
        GlobalNetworkId: str,
        Bandwidth: dict[str, Any],
        SiteId: str,
        Description: str | None = None,
        Type: str | None = None,
        Provider: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_site(
        self,
        *,
        GlobalNetworkId: str,
        Description: str | None = None,
        Location: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_site_to_site_vpn_attachment(
        self,
        *,
        CoreNetworkId: str,
        VpnConnectionArn: str,
        RoutingPolicyLabel: str | None = None,
        NatGatewaySupport: str | None = None,
        NatSystemRouteSupport: bool | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_peering(
        self,
        *,
        CoreNetworkId: str,
        TransitGatewayArn: str,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_route_table_attachment(
        self,
        *,
        PeeringId: str,
        TransitGatewayRouteTableArn: str,
        RoutingPolicyLabel: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_attachment(
        self,
        *,
        CoreNetworkId: str,
        VpcArn: str,
        SubnetArns: list[str],
        Options: dict[str, Any] | None = None,
        RoutingPolicyLabel: str | None = None,
        NatGatewaySupport: str | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connect_peer(
        self,
        *,
        ConnectPeerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_context_store(
        self,
        *,
        ContextStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_core_network(
        self,
        *,
        CoreNetworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_core_network_policy_version(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_core_network_prefix_list_association(
        self,
        *,
        CoreNetworkId: str,
        PrefixListArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_device(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_global_network(
        self,
        *,
        GlobalNetworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_link(
        self,
        *,
        GlobalNetworkId: str,
        LinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_peering(
        self,
        *,
        PeeringId: str,
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
    def delete_site(
        self,
        *,
        GlobalNetworkId: str,
        SiteId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_transit_gateway(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_networks(
        self,
        *,
        GlobalNetworkIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_connect_peer(
        self,
        *,
        GlobalNetworkId: str,
        ConnectPeerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_context_store(
        self,
        *,
        ContextStoreId: str,
        TransitGatewayArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_customer_gateway(
        self,
        *,
        GlobalNetworkId: str,
        CustomerGatewayArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_link(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        LinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_transit_gateway_connect_peer(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_core_network_change_set(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connect_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connect_peer(
        self,
        *,
        ConnectPeerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connect_peer_associations(
        self,
        *,
        GlobalNetworkId: str,
        ConnectPeerIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connections(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionIds: list[str] | None = None,
        DeviceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_context_store(
        self,
        *,
        ContextStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_context_store_association(
        self,
        *,
        ContextStoreId: str,
        TransitGatewayArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_context_version(
        self,
        *,
        ContextStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_core_network(
        self,
        *,
        CoreNetworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_core_network_change_events(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_core_network_change_set(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_core_network_policy(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int | None = None,
        Alias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_customer_gateway_associations(
        self,
        *,
        GlobalNetworkId: str,
        CustomerGatewayArns: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_devices(
        self,
        *,
        GlobalNetworkId: str,
        DeviceIds: list[str] | None = None,
        SiteId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_direct_connect_gateway_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_link_associations(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str | None = None,
        LinkId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_links(
        self,
        *,
        GlobalNetworkId: str,
        LinkIds: list[str] | None = None,
        SiteId: str | None = None,
        Type: str | None = None,
        Provider: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_resource_counts(
        self,
        *,
        GlobalNetworkId: str,
        ResourceType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_resource_relationships(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str | None = None,
        RegisteredGatewayArn: str | None = None,
        AwsRegion: str | None = None,
        AccountId: str | None = None,
        ResourceType: str | None = None,
        ResourceArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_resources(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str | None = None,
        RegisteredGatewayArn: str | None = None,
        AwsRegion: str | None = None,
        AccountId: str | None = None,
        ResourceType: str | None = None,
        ResourceArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_routes(
        self,
        *,
        GlobalNetworkId: str,
        RouteTableIdentifier: dict[str, Any],
        ExactCidrMatches: list[str] | None = None,
        LongestPrefixMatches: list[str] | None = None,
        SubnetOfMatches: list[str] | None = None,
        SupernetOfMatches: list[str] | None = None,
        PrefixListIds: list[str] | None = None,
        States: list[str] | None = None,
        Types: list[str] | None = None,
        DestinationFilters: dict[str, list[str]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_telemetry(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str | None = None,
        RegisteredGatewayArn: str | None = None,
        AwsRegion: str | None = None,
        AccountId: str | None = None,
        ResourceType: str | None = None,
        ResourceArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
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
    def get_route_analysis(
        self,
        *,
        GlobalNetworkId: str,
        RouteAnalysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_site_to_site_vpn_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sites(
        self,
        *,
        GlobalNetworkId: str,
        SiteIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_connect_peer_associations(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArns: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_peering(
        self,
        *,
        PeeringId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_registrations(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArns: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_route_table_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attachment_nat_configurations(
        self,
        *,
        CoreNetworkId: str | None = None,
        AttachmentId: str | None = None,
        Filters: dict[str, list[str]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attachment_routing_policy_associations(
        self,
        *,
        CoreNetworkId: str,
        AttachmentId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attachments(
        self,
        *,
        CoreNetworkId: str | None = None,
        AttachmentType: str | None = None,
        EdgeLocation: str | None = None,
        State: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connect_peers(
        self,
        *,
        CoreNetworkId: str | None = None,
        ConnectAttachmentId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_context_changes(
        self,
        *,
        ContextStoreId: str,
        FromVersionId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_context_store_associations(
        self,
        *,
        ContextStoreId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_context_stores(
        self,
        *,
        GlobalNetworkId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contexts(
        self,
        *,
        ContextStoreId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_core_network_policy_versions(
        self,
        *,
        CoreNetworkId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_core_network_prefix_list_associations(
        self,
        *,
        CoreNetworkId: str,
        PrefixListArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_core_network_routing_information(
        self,
        *,
        CoreNetworkId: str,
        SegmentName: str,
        EdgeLocation: str,
        NextHopFilters: dict[str, list[str]] | None = None,
        ExactPrefixMatches: list[str] | None = None,
        LongestPrefixMatches: list[str] | None = None,
        SubnetOfMatches: list[str] | None = None,
        SupernetOfMatches: list[str] | None = None,
        LocalPreferenceMatches: list[str] | None = None,
        ExactAsPathMatches: list[str] | None = None,
        MedMatches: list[str] | None = None,
        CommunityMatches: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_core_networks(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_service_access_status(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_peerings(
        self,
        *,
        CoreNetworkId: str | None = None,
        PeeringType: str | None = None,
        EdgeLocation: str | None = None,
        State: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_attachment_routing_policy_label(
        self,
        *,
        CoreNetworkId: str,
        AttachmentId: str,
        RoutingPolicyLabel: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_core_network_policy(
        self,
        *,
        CoreNetworkId: str,
        PolicyDocument: str,
        Description: str | None = None,
        LatestVersionId: int | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        PolicyDocument: str,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_transit_gateway(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_attachment(
        self,
        *,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_attachment_routing_policy_label(
        self,
        *,
        CoreNetworkId: str,
        AttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_core_network_policy_version(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_organization_service_access_update(
        self,
        *,
        Action: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_route_analysis(
        self,
        *,
        GlobalNetworkId: str,
        Source: dict[str, Any],
        Destination: dict[str, Any],
        IncludeReturnPath: bool | None = None,
        UseMiddleboxes: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_attachment_nat_configuration(
        self,
        *,
        AttachmentId: str,
        NatGatewaySupport: str | None = None,
        NatSystemRouteSupport: bool | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionId: str,
        LinkId: str | None = None,
        ConnectedLinkId: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_context_store(
        self,
        *,
        ContextStoreId: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_core_network(
        self,
        *,
        CoreNetworkId: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        AWSLocation: dict[str, Any] | None = None,
        Description: str | None = None,
        Type: str | None = None,
        Vendor: str | None = None,
        Model: str | None = None,
        SerialNumber: str | None = None,
        Location: dict[str, Any] | None = None,
        SiteId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_direct_connect_gateway_attachment(
        self,
        *,
        AttachmentId: str,
        EdgeLocations: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_global_network(
        self,
        *,
        GlobalNetworkId: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_link(
        self,
        *,
        GlobalNetworkId: str,
        LinkId: str,
        Description: str | None = None,
        Type: str | None = None,
        Bandwidth: dict[str, Any] | None = None,
        Provider: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_network_resource_metadata(
        self,
        *,
        GlobalNetworkId: str,
        ResourceArn: str,
        Metadata: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_site(
        self,
        *,
        GlobalNetworkId: str,
        SiteId: str,
        Description: str | None = None,
        Location: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_attachment(
        self,
        *,
        AttachmentId: str,
        AddSubnetArns: list[str] | None = None,
        RemoveSubnetArns: list[str] | None = None,
        Options: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .direct_connect_bgp_peer import DirectConnectBGPPeer
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix
from .direct_connect_tag import DirectConnectTag


class DirectConnectAssociateVirtualInterfaceResponse(BaseModel):
    ownerAccount: StrictStr | None = None
    virtualInterfaceId: StrictStr | None = None
    location: StrictStr | None = None
    connectionId: StrictStr | None = None
    virtualInterfaceType: StrictStr | None = None
    virtualInterfaceName: StrictStr | None = None
    vlan: StrictInt | None = None
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    amazonSideAsn: StrictInt | None = None
    authKey: StrictStr | None = None
    amazonAddress: StrictStr | None = None
    customerAddress: StrictStr | None = None
    addressFamily: StrictStr | None = None
    virtualInterfaceState: StrictStr | None = None
    customerRouterConfig: StrictStr | None = None
    mtu: StrictInt | None = None
    jumboFrameCapable: StrictBool | None = None
    virtualGatewayId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
    routeFilterPrefixes: list[DirectConnectRouteFilterPrefix] | None = None
    bgpPeers: list[DirectConnectBGPPeer] | None = None
    region: StrictStr | None = None
    awsDeviceV2: StrictStr | None = None
    awsLogicalDeviceId: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    siteLinkEnabled: StrictBool | None = None
    prefixPoolAllocatedCountIpv4: StrictInt | None = None
    prefixPoolAllocatedCountIpv6: StrictInt | None = None
    rateLimit: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

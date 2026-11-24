from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_vpn_tunnel_options_specification import EC2VpnTunnelOptionsSpecification


class EC2VpnConnectionOptionsSpecification(BaseModel):
    EnableAcceleration: StrictBool | None = None
    TunnelInsideIpVersion: Literal['ipv4', 'ipv6'] | None = None
    TunnelOptions: list[EC2VpnTunnelOptionsSpecification] | None = None
    LocalIpv4NetworkCidr: StrictStr | None = None
    RemoteIpv4NetworkCidr: StrictStr | None = None
    LocalIpv6NetworkCidr: StrictStr | None = None
    RemoteIpv6NetworkCidr: StrictStr | None = None
    OutsideIpAddressType: StrictStr | None = None
    TransportTransitGatewayAttachmentId: StrictStr | None = None
    TunnelBandwidth: Literal['standard', 'large'] | None = None
    StaticRoutesOnly: StrictBool | None = None

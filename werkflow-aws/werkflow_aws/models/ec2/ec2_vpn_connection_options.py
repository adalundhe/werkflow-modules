from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tunnel_option import EC2TunnelOption


class EC2VpnConnectionOptions(BaseModel):
    EnableAcceleration: StrictBool | None = None
    StaticRoutesOnly: StrictBool | None = None
    LocalIpv4NetworkCidr: StrictStr | None = None
    RemoteIpv4NetworkCidr: StrictStr | None = None
    LocalIpv6NetworkCidr: StrictStr | None = None
    RemoteIpv6NetworkCidr: StrictStr | None = None
    OutsideIpAddressType: StrictStr | None = None
    TransportTransitGatewayAttachmentId: StrictStr | None = None
    TunnelInsideIpVersion: StrictStr | None = None
    TunnelOptions: list[EC2TunnelOption] | None = None
    TunnelBandwidth: StrictStr | None = None

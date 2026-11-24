from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_route_status import EC2ClientVpnRouteStatus


class EC2ClientVpnRoute(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    DestinationCidr: StrictStr | None = None
    TargetSubnet: StrictStr | None = None
    Type: StrictStr | None = None
    Origin: StrictStr | None = None
    Status: EC2ClientVpnRouteStatus | None = None
    Description: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None

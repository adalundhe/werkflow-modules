from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_vgw_telemetry import EC2VgwTelemetry
from .ec2_vpn_connection_options import EC2VpnConnectionOptions
from .ec2_vpn_static_route import EC2VpnStaticRoute


class EC2VpnConnection(BaseModel):
    Category: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    VpnConcentratorId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    CoreNetworkAttachmentArn: StrictStr | None = None
    GatewayAssociationState: StrictStr | None = None
    Options: EC2VpnConnectionOptions | None = None
    Routes: list[EC2VpnStaticRoute] | None = None
    Tags: list[EC2TagModel] | None = None
    VgwTelemetry: list[EC2VgwTelemetry] | None = None
    PreSharedKeyArn: StrictStr | None = None
    VpnConnectionId: StrictStr | None = None
    State: StrictStr | None = None
    CustomerGatewayConfiguration: StrictStr | None = None
    Type: StrictStr | None = None
    CustomerGatewayId: StrictStr | None = None
    VpnGatewayId: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateRouteRequest(BaseModel):
    RouteTableId: StrictStr
    DestinationPrefixListId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    LocalGatewayId: StrictStr | None = None
    CarrierGatewayId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    OdbNetworkArn: StrictStr | None = None
    DryRun: StrictBool | None = None
    DestinationCidrBlock: StrictStr | None = None
    GatewayId: StrictStr | None = None
    DestinationIpv6CidrBlock: StrictStr | None = None
    EgressOnlyInternetGatewayId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    NatGatewayId: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AnalysisRouteTableRoute(BaseModel):
    DestinationCidr: StrictStr | None = None
    DestinationPrefixListId: StrictStr | None = None
    EgressOnlyInternetGatewayId: StrictStr | None = None
    GatewayId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    NatGatewayId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    Origin: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    State: StrictStr | None = None
    CarrierGatewayId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    LocalGatewayId: StrictStr | None = None

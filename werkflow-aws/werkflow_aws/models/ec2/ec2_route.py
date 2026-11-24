from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_igw_firewall import EC2IgwFirewall


class EC2Route(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    DestinationIpv6CidrBlock: StrictStr | None = None
    DestinationPrefixListId: StrictStr | None = None
    EgressOnlyInternetGatewayId: StrictStr | None = None
    GatewayId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    InstanceOwnerId: StrictStr | None = None
    NatGatewayId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    LocalGatewayId: StrictStr | None = None
    CarrierGatewayId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    Origin: StrictStr | None = None
    State: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    OdbNetworkArn: StrictStr | None = None
    IpAddress: StrictStr | None = None
    IgwFirewall: EC2IgwFirewall | None = None

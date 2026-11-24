from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_dns_options_specification import EC2DnsOptionsSpecification
from .ec2_subnet_configuration import EC2SubnetConfiguration


class EC2ModifyVpcEndpointRequest(BaseModel):
    VpcEndpointId: StrictStr
    DryRun: StrictBool | None = None
    ResetPolicy: StrictBool | None = None
    PolicyDocument: StrictStr | None = None
    AddRouteTableIds: list[StrictStr] | None = None
    RemoveRouteTableIds: list[StrictStr] | None = None
    AddSubnetIds: list[StrictStr] | None = None
    RemoveSubnetIds: list[StrictStr] | None = None
    AddSecurityGroupIds: list[StrictStr] | None = None
    RemoveSecurityGroupIds: list[StrictStr] | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'ipv6'] | None = None
    DnsOptions: EC2DnsOptionsSpecification | None = None
    PrivateDnsEnabled: StrictBool | None = None
    SubnetConfigurations: list[EC2SubnetConfiguration] | None = None

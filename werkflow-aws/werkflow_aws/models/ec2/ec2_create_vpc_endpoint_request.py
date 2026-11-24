from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_dns_options_specification import EC2DnsOptionsSpecification
from .ec2_subnet_configuration import EC2SubnetConfiguration
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateVpcEndpointRequest(BaseModel):
    VpcId: StrictStr
    DryRun: StrictBool | None = None
    VpcEndpointType: Literal['Interface', 'Gateway', 'GatewayLoadBalancer', 'Resource', 'ServiceNetwork', 'Tunnel'] | None = None
    ServiceName: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'ipv6'] | None = None
    DnsOptions: EC2DnsOptionsSpecification | None = None
    ClientToken: StrictStr | None = None
    PrivateDnsEnabled: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    SubnetConfigurations: list[EC2SubnetConfiguration] | None = None
    ServiceNetworkArn: StrictStr | None = None
    ResourceConfigurationArn: StrictStr | None = None
    ServiceRegion: StrictStr | None = None

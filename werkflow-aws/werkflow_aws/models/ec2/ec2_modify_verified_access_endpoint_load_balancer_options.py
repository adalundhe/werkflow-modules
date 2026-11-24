from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_modify_verified_access_endpoint_port_range import EC2ModifyVerifiedAccessEndpointPortRange


class EC2ModifyVerifiedAccessEndpointLoadBalancerOptions(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    Protocol: Literal['http', 'https', 'tcp'] | None = None
    Port: StrictInt | None = None
    PortRanges: list[EC2ModifyVerifiedAccessEndpointPortRange] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_verified_access_endpoint_port_range import EC2VerifiedAccessEndpointPortRange


class EC2VerifiedAccessEndpointLoadBalancerOptions(BaseModel):
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
    LoadBalancerArn: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    PortRanges: list[EC2VerifiedAccessEndpointPortRange] | None = None

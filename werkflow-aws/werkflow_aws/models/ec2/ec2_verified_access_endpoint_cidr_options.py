from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_endpoint_port_range import EC2VerifiedAccessEndpointPortRange


class EC2VerifiedAccessEndpointCidrOptions(BaseModel):
    Cidr: StrictStr | None = None
    PortRanges: list[EC2VerifiedAccessEndpointPortRange] | None = None
    Protocol: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None

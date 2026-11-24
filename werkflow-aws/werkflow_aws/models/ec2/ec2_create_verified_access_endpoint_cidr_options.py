from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ec2_create_verified_access_endpoint_port_range import EC2CreateVerifiedAccessEndpointPortRange


class EC2CreateVerifiedAccessEndpointCidrOptions(BaseModel):
    Protocol: Literal['http', 'https', 'tcp'] | None = None
    SubnetIds: list[StrictStr] | None = None
    Cidr: StrictStr | None = None
    PortRanges: list[EC2CreateVerifiedAccessEndpointPortRange] | None = None

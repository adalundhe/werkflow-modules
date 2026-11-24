from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_create_verified_access_endpoint_port_range import EC2CreateVerifiedAccessEndpointPortRange


class EC2CreateVerifiedAccessEndpointEniOptions(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
    Protocol: Literal['http', 'https', 'tcp'] | None = None
    Port: StrictInt | None = None
    PortRanges: list[EC2CreateVerifiedAccessEndpointPortRange] | None = None

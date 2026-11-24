from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_verified_access_endpoint_port_range import EC2VerifiedAccessEndpointPortRange


class EC2VerifiedAccessEndpointEniOptions(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
    PortRanges: list[EC2VerifiedAccessEndpointPortRange] | None = None

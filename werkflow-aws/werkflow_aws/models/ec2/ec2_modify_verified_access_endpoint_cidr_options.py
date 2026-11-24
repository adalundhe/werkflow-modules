from __future__ import annotations
from pydantic import BaseModel
from .ec2_modify_verified_access_endpoint_port_range import EC2ModifyVerifiedAccessEndpointPortRange


class EC2ModifyVerifiedAccessEndpointCidrOptions(BaseModel):
    PortRanges: list[EC2ModifyVerifiedAccessEndpointPortRange] | None = None

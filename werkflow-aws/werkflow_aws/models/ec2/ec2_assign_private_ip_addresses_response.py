from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_assigned_private_ip_address import EC2AssignedPrivateIpAddress
from .ec2_ipv4_prefix_specification import EC2Ipv4PrefixSpecification


class EC2AssignPrivateIpAddressesResponse(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
    AssignedPrivateIpAddresses: list[EC2AssignedPrivateIpAddress] | None = None
    AssignedIpv4Prefixes: list[EC2Ipv4PrefixSpecification] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_discovered_public_address import EC2IpamDiscoveredPublicAddress


class EC2GetIpamDiscoveredPublicAddressesResponse(BaseModel):
    IpamDiscoveredPublicAddresses: list[EC2IpamDiscoveredPublicAddress] | None = None
    OldestSampleTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

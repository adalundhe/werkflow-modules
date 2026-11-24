from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_front_ipam_cidr_config import CloudFrontIpamCidrConfig


class CloudFrontUpdateAnycastIpListRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
    IpAddressType: Literal['ipv4', 'ipv6', 'dualstack'] | None = None
    IpamCidrConfigs: list[CloudFrontIpamCidrConfig] | None = None

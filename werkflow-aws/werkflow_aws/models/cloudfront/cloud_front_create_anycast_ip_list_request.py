from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_ipam_cidr_config import CloudFrontIpamCidrConfig
from .cloud_front_tags import CloudFrontTags


class CloudFrontCreateAnycastIpListRequest(BaseModel):
    Name: StrictStr
    IpCount: StrictInt
    Tags: CloudFrontTags | None = None
    IpAddressType: Literal['ipv4', 'ipv6', 'dualstack'] | None = None
    IpamCidrConfigs: list[CloudFrontIpamCidrConfig] | None = None

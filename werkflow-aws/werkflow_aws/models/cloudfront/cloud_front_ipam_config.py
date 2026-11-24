from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_ipam_cidr_config import CloudFrontIpamCidrConfig


class CloudFrontIpamConfig(BaseModel):
    Quantity: StrictInt | None = None
    IpamCidrConfigs: list[CloudFrontIpamCidrConfig] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_dns_configuration import CloudFrontDnsConfiguration


class CloudFrontVerifyDnsConfigurationResponse(BaseModel):
    DnsConfigurationList: list[CloudFrontDnsConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None

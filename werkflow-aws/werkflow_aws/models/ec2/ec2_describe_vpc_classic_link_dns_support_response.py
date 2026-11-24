from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_classic_link_dns_support import EC2ClassicLinkDnsSupport


class EC2DescribeVpcClassicLinkDnsSupportResponse(BaseModel):
    NextToken: StrictStr | None = None
    Vpcs: list[EC2ClassicLinkDnsSupport] | None = None
    ResponseMetadata: dict[str, Any] | None = None

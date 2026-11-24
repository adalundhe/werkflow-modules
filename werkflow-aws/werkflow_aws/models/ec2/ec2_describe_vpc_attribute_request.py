from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeVpcAttributeRequest(BaseModel):
    Attribute: Literal['enableDnsSupport', 'enableDnsHostnames', 'enableNetworkAddressUsageMetrics']
    VpcId: StrictStr
    DryRun: StrictBool | None = None

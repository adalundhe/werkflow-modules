from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue


class EC2DescribeVpcAttributeResponse(BaseModel):
    EnableDnsHostnames: EC2AttributeBooleanValue | None = None
    EnableDnsSupport: EC2AttributeBooleanValue | None = None
    EnableNetworkAddressUsageMetrics: EC2AttributeBooleanValue | None = None
    VpcId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

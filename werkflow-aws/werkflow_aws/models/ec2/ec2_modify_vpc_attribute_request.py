from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue


class EC2ModifyVpcAttributeRequest(BaseModel):
    VpcId: StrictStr
    EnableDnsHostnames: EC2AttributeBooleanValue | None = None
    EnableDnsSupport: EC2AttributeBooleanValue | None = None
    EnableNetworkAddressUsageMetrics: EC2AttributeBooleanValue | None = None

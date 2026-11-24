from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_type_info import EC2InstanceTypeInfo


class EC2DescribeInstanceTypesResponse(BaseModel):
    InstanceTypes: list[EC2InstanceTypeInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

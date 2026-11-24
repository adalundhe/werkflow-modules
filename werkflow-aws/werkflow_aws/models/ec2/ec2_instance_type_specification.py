from __future__ import annotations
from pydantic import BaseModel
from .ec2_instance_type_item import EC2InstanceTypeItem


class EC2InstanceTypeSpecification(BaseModel):
    SupportedInstanceTypes: list[EC2InstanceTypeItem] | None = None
    UnsupportedInstanceTypes: list[EC2InstanceTypeItem] | None = None

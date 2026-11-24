from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_type_specification_request import EC2InstanceTypeSpecificationRequest


class EC2ReplaceImageInstanceTypeSpecificationRequest(BaseModel):
    ImageId: StrictStr
    InstanceTypeSpecification: EC2InstanceTypeSpecificationRequest | None = None
    DryRun: StrictBool | None = None

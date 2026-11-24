from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification import EC2TagSpecification


class EC2CreateSecurityGroupRequest(BaseModel):
    Description: StrictStr
    GroupName: StrictStr
    VpcId: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecification] | None = None
    DryRun: StrictBool | None = None

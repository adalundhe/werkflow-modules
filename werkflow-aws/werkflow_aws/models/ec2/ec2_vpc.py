from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag import EC2Tag


class EC2Vpc(BaseModel):
    VpcId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    State: StrictStr | None = None
    DhcpOptionsId: StrictStr | None = None
    InstanceTenancy: StrictStr | None = None
    IsDefault: StrictBool | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2Tag] | None = None

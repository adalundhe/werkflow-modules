from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2SecurityGroupForVpc(BaseModel):
    Description: StrictStr | None = None
    GroupName: StrictStr | None = None
    OwnerId: StrictStr | None = None
    GroupId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    PrimaryVpcId: StrictStr | None = None

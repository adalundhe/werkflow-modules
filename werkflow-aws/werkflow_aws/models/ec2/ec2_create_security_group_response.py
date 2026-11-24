from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag import EC2Tag


class EC2CreateSecurityGroupResponse(BaseModel):
    GroupId: StrictStr | None = None
    Tags: list[EC2Tag] | None = None
    SecurityGroupArn: StrictStr | None = None

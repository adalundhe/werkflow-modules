from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Any
from .ec2_tag import EC2Tag


class EC2SecurityGroup(BaseModel):
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    Description: StrictStr | None = None
    VpcId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    IpPermissions: list[dict[str, Any]] | None = None
    IpPermissionsEgress: list[dict[str, Any]] | None = None
    Tags: list[EC2Tag] | None = None

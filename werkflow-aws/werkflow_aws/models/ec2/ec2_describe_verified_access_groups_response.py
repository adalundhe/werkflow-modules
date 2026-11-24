from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_group import EC2VerifiedAccessGroup


class EC2DescribeVerifiedAccessGroupsResponse(BaseModel):
    VerifiedAccessGroups: list[EC2VerifiedAccessGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

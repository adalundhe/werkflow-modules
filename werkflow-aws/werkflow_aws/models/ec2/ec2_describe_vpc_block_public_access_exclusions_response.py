from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_block_public_access_exclusion import EC2VpcBlockPublicAccessExclusion


class EC2DescribeVpcBlockPublicAccessExclusionsResponse(BaseModel):
    VpcBlockPublicAccessExclusions: list[EC2VpcBlockPublicAccessExclusion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_block_public_access_options import EC2VpcBlockPublicAccessOptions


class EC2DescribeVpcBlockPublicAccessOptionsResponse(BaseModel):
    VpcBlockPublicAccessOptions: EC2VpcBlockPublicAccessOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None

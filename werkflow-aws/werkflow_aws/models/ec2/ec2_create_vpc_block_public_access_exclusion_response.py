from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_block_public_access_exclusion import EC2VpcBlockPublicAccessExclusion


class EC2CreateVpcBlockPublicAccessExclusionResponse(BaseModel):
    VpcBlockPublicAccessExclusion: EC2VpcBlockPublicAccessExclusion | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_instance import EC2VerifiedAccessInstance


class EC2DescribeVerifiedAccessInstancesResponse(BaseModel):
    VerifiedAccessInstances: list[EC2VerifiedAccessInstance] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

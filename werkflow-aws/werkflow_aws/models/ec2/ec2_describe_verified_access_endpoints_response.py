from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_endpoint import EC2VerifiedAccessEndpoint


class EC2DescribeVerifiedAccessEndpointsResponse(BaseModel):
    VerifiedAccessEndpoints: list[EC2VerifiedAccessEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

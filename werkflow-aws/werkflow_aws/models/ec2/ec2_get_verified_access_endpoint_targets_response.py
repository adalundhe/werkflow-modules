from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_endpoint_target import EC2VerifiedAccessEndpointTarget


class EC2GetVerifiedAccessEndpointTargetsResponse(BaseModel):
    VerifiedAccessEndpointTargets: list[EC2VerifiedAccessEndpointTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

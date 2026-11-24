from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_verified_access_endpoint import EC2VerifiedAccessEndpoint


class EC2CreateVerifiedAccessEndpointResponse(BaseModel):
    VerifiedAccessEndpoint: EC2VerifiedAccessEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None

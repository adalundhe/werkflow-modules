from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_endpoint import EC2VpcEndpoint


class EC2CreateVpcEndpointResponse(BaseModel):
    VpcEndpoint: EC2VpcEndpoint | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

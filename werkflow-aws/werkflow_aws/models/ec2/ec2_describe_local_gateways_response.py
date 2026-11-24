from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_local_gateway import EC2LocalGateway


class EC2DescribeLocalGatewaysResponse(BaseModel):
    LocalGateways: list[EC2LocalGateway] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

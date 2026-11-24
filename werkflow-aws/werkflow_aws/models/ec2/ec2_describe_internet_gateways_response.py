from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_internet_gateway import EC2InternetGateway


class EC2DescribeInternetGatewaysResponse(BaseModel):
    InternetGateways: list[EC2InternetGateway] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

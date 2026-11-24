from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_customer_gateway import EC2CustomerGateway


class EC2DescribeCustomerGatewaysResponse(BaseModel):
    CustomerGateways: list[EC2CustomerGateway] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_internet_gateway import EC2InternetGateway


class EC2CreateInternetGatewayResponse(BaseModel):
    InternetGateway: EC2InternetGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None

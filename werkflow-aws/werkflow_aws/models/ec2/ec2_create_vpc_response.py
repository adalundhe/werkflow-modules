from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_model import EC2VpcModel


class EC2CreateVpcResponse(BaseModel):
    Vpc: EC2VpcModel | None = None
    ResponseMetadata: dict[str, Any] | None = None

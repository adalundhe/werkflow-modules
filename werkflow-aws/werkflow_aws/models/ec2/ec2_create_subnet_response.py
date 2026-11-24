from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_subnet_model import EC2SubnetModel


class EC2CreateSubnetResponse(BaseModel):
    Subnet: EC2SubnetModel | None = None
    ResponseMetadata: dict[str, Any] | None = None

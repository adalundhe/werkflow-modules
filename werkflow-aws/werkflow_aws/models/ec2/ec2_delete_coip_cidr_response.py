from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_coip_cidr import EC2CoipCidr


class EC2DeleteCoipCidrResponse(BaseModel):
    CoipCidr: EC2CoipCidr | None = None
    ResponseMetadata: dict[str, Any] | None = None

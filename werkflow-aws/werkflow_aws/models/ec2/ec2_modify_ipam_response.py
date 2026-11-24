from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam import EC2Ipam


class EC2ModifyIpamResponse(BaseModel):
    Ipam: EC2Ipam | None = None
    ResponseMetadata: dict[str, Any] | None = None

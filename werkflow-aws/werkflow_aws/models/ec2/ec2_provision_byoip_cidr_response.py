from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_byoip_cidr import EC2ByoipCidr


class EC2ProvisionByoipCidrResponse(BaseModel):
    ByoipCidr: EC2ByoipCidr | None = None
    ResponseMetadata: dict[str, Any] | None = None

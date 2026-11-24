from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_byoasn import EC2Byoasn


class EC2ProvisionIpamByoasnResponse(BaseModel):
    Byoasn: EC2Byoasn | None = None
    ResponseMetadata: dict[str, Any] | None = None

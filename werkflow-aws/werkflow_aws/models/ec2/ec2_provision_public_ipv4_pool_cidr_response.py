from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_public_ipv4_pool_range import EC2PublicIpv4PoolRange


class EC2ProvisionPublicIpv4PoolCidrResponse(BaseModel):
    PoolId: StrictStr | None = None
    PoolAddressRange: EC2PublicIpv4PoolRange | None = None
    ResponseMetadata: dict[str, Any] | None = None

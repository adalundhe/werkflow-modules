from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2DeprovisionPublicIpv4PoolCidrResponse(BaseModel):
    PoolId: StrictStr | None = None
    DeprovisionedAddresses: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None

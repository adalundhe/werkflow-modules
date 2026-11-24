from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2CreatePublicIpv4PoolResponse(BaseModel):
    PoolId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

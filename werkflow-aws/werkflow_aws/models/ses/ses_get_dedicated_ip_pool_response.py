from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_dedicated_ip_pool import SESDedicatedIpPool


class SESGetDedicatedIpPoolResponse(BaseModel):
    DedicatedIpPool: SESDedicatedIpPool | None = None
    ResponseMetadata: dict[str, Any] | None = None

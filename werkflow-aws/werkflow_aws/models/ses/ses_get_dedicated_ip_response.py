from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_dedicated_ip import SESDedicatedIp


class SESGetDedicatedIpResponse(BaseModel):
    DedicatedIp: SESDedicatedIp | None = None
    ResponseMetadata: dict[str, Any] | None = None

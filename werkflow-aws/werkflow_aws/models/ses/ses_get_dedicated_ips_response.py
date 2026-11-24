from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_dedicated_ip import SESDedicatedIp


class SESGetDedicatedIpsResponse(BaseModel):
    DedicatedIps: list[SESDedicatedIp] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

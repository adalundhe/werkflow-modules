from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2EnableIpamPolicyResponse(BaseModel):
    IpamPolicyId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

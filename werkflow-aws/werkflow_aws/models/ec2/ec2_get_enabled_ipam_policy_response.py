from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetEnabledIpamPolicyResponse(BaseModel):
    IpamPolicyEnabled: StrictBool | None = None
    IpamPolicyId: StrictStr | None = None
    ManagedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

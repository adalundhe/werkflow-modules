from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ELBv2SetSecurityGroupsResponse(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsGetContactReachabilityStatusRequest(BaseModel):
    domainName: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsResendContactReachabilityEmailRequest(BaseModel):
    domainName: StrictStr | None = None

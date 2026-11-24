from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsCheckDomainTransferabilityRequest(BaseModel):
    DomainName: StrictStr
    AuthCode: StrictStr | None = None

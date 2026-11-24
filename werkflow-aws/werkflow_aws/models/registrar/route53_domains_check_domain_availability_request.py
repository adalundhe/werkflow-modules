from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsCheckDomainAvailabilityRequest(BaseModel):
    DomainName: StrictStr
    IdnLangCode: StrictStr | None = None

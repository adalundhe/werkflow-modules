from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsGetDomainPricesRequest(BaseModel):
    DomainName: StrictStr

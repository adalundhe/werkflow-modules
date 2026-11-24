from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsGetDomainDetailRequest(BaseModel):
    DomainName: StrictStr

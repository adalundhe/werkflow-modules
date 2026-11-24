from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsDisassociateDelegationSignerFromDomainRequest(BaseModel):
    DomainName: StrictStr
    Id: StrictStr

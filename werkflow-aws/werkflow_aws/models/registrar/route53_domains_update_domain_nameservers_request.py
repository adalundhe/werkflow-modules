from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_nameserver import Route53DomainsNameserver


class Route53DomainsUpdateDomainNameserversRequest(BaseModel):
    DomainName: StrictStr
    Nameservers: list[Route53DomainsNameserver]
    FIAuthKey: StrictStr | None = None

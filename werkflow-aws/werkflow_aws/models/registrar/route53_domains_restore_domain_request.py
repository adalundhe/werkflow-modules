from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_consent import Route53DomainsConsent


class Route53DomainsRestoreDomainRequest(BaseModel):
    DomainName: StrictStr
    Consent: Route53DomainsConsent | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_domains_consent import Route53DomainsConsent


class Route53DomainsRenewDomainRequest(BaseModel):
    DomainName: StrictStr
    CurrentExpiryYear: StrictInt
    DurationInYears: StrictInt | None = None
    Consent: Route53DomainsConsent | None = None

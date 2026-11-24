from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_consent import Route53DomainsConsent
from .route53_domains_contact_detail import Route53DomainsContactDetail


class Route53DomainsUpdateDomainContactRequest(BaseModel):
    DomainName: StrictStr
    AdminContact: Route53DomainsContactDetail | None = None
    RegistrantContact: Route53DomainsContactDetail | None = None
    TechContact: Route53DomainsContactDetail | None = None
    Consent: Route53DomainsConsent | None = None
    BillingContact: Route53DomainsContactDetail | None = None

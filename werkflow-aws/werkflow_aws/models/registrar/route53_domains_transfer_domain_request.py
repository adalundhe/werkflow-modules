from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_domains_consent import Route53DomainsConsent
from .route53_domains_contact_detail import Route53DomainsContactDetail
from .route53_domains_nameserver import Route53DomainsNameserver


class Route53DomainsTransferDomainRequest(BaseModel):
    DomainName: StrictStr
    AdminContact: Route53DomainsContactDetail
    RegistrantContact: Route53DomainsContactDetail
    TechContact: Route53DomainsContactDetail
    IdnLangCode: StrictStr | None = None
    DurationInYears: StrictInt | None = None
    Nameservers: list[Route53DomainsNameserver] | None = None
    AuthCode: StrictStr | None = None
    AutoRenew: StrictBool | None = None
    PrivacyProtectAdminContact: StrictBool | None = None
    PrivacyProtectRegistrantContact: StrictBool | None = None
    PrivacyProtectTechContact: StrictBool | None = None
    BillingContact: Route53DomainsContactDetail | None = None
    PrivacyProtectBillingContact: StrictBool | None = None
    Consent: Route53DomainsConsent | None = None

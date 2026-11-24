from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_domains_consent import Route53DomainsConsent
from .route53_domains_contact_detail import Route53DomainsContactDetail


class Route53DomainsRegisterDomainRequest(BaseModel):
    DomainName: StrictStr
    DurationInYears: StrictInt
    AdminContact: Route53DomainsContactDetail
    RegistrantContact: Route53DomainsContactDetail
    TechContact: Route53DomainsContactDetail
    IdnLangCode: StrictStr | None = None
    AutoRenew: StrictBool | None = None
    PrivacyProtectAdminContact: StrictBool | None = None
    PrivacyProtectRegistrantContact: StrictBool | None = None
    PrivacyProtectTechContact: StrictBool | None = None
    BillingContact: Route53DomainsContactDetail | None = None
    PrivacyProtectBillingContact: StrictBool | None = None
    Consent: Route53DomainsConsent | None = None

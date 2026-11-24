from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class Route53DomainsUpdateDomainContactPrivacyRequest(BaseModel):
    DomainName: StrictStr
    AdminPrivacy: StrictBool | None = None
    RegistrantPrivacy: StrictBool | None = None
    TechPrivacy: StrictBool | None = None
    BillingPrivacy: StrictBool | None = None

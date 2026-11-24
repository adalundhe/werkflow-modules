from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_extra_param import Route53DomainsExtraParam


class Route53DomainsContactDetail(BaseModel):
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
    ContactType: StrictStr | None = None
    OrganizationName: StrictStr | None = None
    AddressLine1: StrictStr | None = None
    AddressLine2: StrictStr | None = None
    City: StrictStr | None = None
    State: StrictStr | None = None
    CountryCode: StrictStr | None = None
    ZipCode: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    Email: StrictStr | None = None
    Fax: StrictStr | None = None
    ExtraParams: list[Route53DomainsExtraParam] | None = None

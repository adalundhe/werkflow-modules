from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_domains_contact_detail import Route53DomainsContactDetail
from .route53_domains_dnssec_key import Route53DomainsDnssecKey
from .route53_domains_nameserver import Route53DomainsNameserver


class Route53DomainsGetDomainDetailResponse(BaseModel):
    DomainName: StrictStr | None = None
    Nameservers: list[Route53DomainsNameserver] | None = None
    AutoRenew: StrictBool | None = None
    AdminContact: Route53DomainsContactDetail | None = None
    RegistrantContact: Route53DomainsContactDetail | None = None
    TechContact: Route53DomainsContactDetail | None = None
    AdminPrivacy: StrictBool | None = None
    RegistrantPrivacy: StrictBool | None = None
    TechPrivacy: StrictBool | None = None
    RegistrarName: StrictStr | None = None
    WhoIsServer: StrictStr | None = None
    RegistrarUrl: StrictStr | None = None
    AbuseContactEmail: StrictStr | None = None
    AbuseContactPhone: StrictStr | None = None
    RegistryDomainId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    UpdatedDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    Reseller: StrictStr | None = None
    DnsSec: StrictStr | None = None
    StatusList: list[StrictStr] | None = None
    DnssecKeys: list[Route53DomainsDnssecKey] | None = None
    BillingContact: Route53DomainsContactDetail | None = None
    BillingPrivacy: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None

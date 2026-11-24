from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_domain_scope import ACMDomainScope
from .acm_resource_record import ACMResourceRecord


class ACMDnsPrevalidationDetails(BaseModel):
    DomainScope: ACMDomainScope | None = None
    HostedZoneId: StrictStr | None = None
    ResourceRecord: ACMResourceRecord | None = None

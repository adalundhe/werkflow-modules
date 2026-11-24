from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_http_redirect import ACMHttpRedirect
from .acm_resource_record import ACMResourceRecord


class ACMDomainValidation(BaseModel):
    DomainName: StrictStr | None = None
    ValidationEmails: list[StrictStr] | None = None
    ValidationDomain: StrictStr | None = None
    ValidationStatus: StrictStr | None = None
    ResourceRecord: ACMResourceRecord | None = None
    HttpRedirect: ACMHttpRedirect | None = None
    ValidationMethod: StrictStr | None = None

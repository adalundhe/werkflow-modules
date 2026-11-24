from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_domain_validation import ACMDomainValidation


class ACMRenewalSummary(BaseModel):
    RenewalStatus: StrictStr | None = None
    DomainValidationOptions: list[ACMDomainValidation] | None = None
    RenewalStatusReason: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None

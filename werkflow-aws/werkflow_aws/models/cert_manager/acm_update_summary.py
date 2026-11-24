from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_domain_validation_method_update_summary import ACMDomainValidationMethodUpdateSummary


class ACMUpdateSummary(BaseModel):
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    DomainValidationMethodUpdateSummary: ACMDomainValidationMethodUpdateSummary | None = None
    RequestedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None

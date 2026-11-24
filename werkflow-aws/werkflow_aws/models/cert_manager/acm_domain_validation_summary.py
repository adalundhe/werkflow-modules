from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_validation_configuration import ACMValidationConfiguration


class ACMDomainValidationSummary(BaseModel):
    DomainName: StrictStr | None = None
    ActiveValidationConfiguration: ACMValidationConfiguration | None = None
    RequestedValidationConfiguration: ACMValidationConfiguration | None = None

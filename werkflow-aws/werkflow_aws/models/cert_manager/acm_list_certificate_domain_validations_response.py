from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acm_domain_validation_summary import ACMDomainValidationSummary


class ACMListCertificateDomainValidationsResponse(BaseModel):
    DomainValidationSummaryList: list[ACMDomainValidationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

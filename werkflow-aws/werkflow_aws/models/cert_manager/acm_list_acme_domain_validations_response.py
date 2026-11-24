from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acme_domain_validation_summary import AcmeDomainValidationSummary


class ACMListAcmeDomainValidationsResponse(BaseModel):
    AcmeDomainValidations: list[AcmeDomainValidationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

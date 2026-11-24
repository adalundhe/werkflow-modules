from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acme_domain_validation import AcmeDomainValidation as _AcmeDomainValidationType


class ACMDescribeAcmeDomainValidationResponse(BaseModel):
    AcmeDomainValidation: _AcmeDomainValidationType | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acm_certificate_summary import ACMCertificateSummary


class ACMListCertificatesResponse(BaseModel):
    NextToken: StrictStr | None = None
    CertificateSummaryList: list[ACMCertificateSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

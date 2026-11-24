from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acm_certificate_search_result import ACMCertificateSearchResult


class ACMSearchCertificatesResponse(BaseModel):
    Results: list[ACMCertificateSearchResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acm_certificate_detail import ACMCertificateDetail


class ACMDescribeCertificateResponse(BaseModel):
    Certificate: ACMCertificateDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None

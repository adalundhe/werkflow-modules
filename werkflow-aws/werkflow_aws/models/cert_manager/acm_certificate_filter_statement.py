from __future__ import annotations
from pydantic import BaseModel
from .acm_certificate_filter import ACMCertificateFilter


class ACMCertificateFilterStatement(BaseModel):
    And: list[ACMCertificateFilterStatement] | None = None
    Or: list[ACMCertificateFilterStatement] | None = None
    Not: ACMCertificateFilterStatement | None = None
    Filter: ACMCertificateFilter | None = None

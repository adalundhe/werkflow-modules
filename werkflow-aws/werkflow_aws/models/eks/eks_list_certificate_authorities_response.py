from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_certificate_authority_summary import EKSCertificateAuthoritySummary


class EKSListCertificateAuthoritiesResponse(BaseModel):
    certificateAuthorities: list[EKSCertificateAuthoritySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

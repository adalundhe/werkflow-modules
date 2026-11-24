from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_certificate_authority import EKSCertificateAuthority


class EKSDescribeCertificateAuthorityResponse(BaseModel):
    certificateAuthority: EKSCertificateAuthority | None = None
    ResponseMetadata: dict[str, Any] | None = None

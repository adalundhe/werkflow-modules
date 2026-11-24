from __future__ import annotations
from pydantic import BaseModel
from .acm_public_certificate_authority import ACMPublicCertificateAuthority


class ACMCertificateAuthority(BaseModel):
    PublicCertificateAuthority: ACMPublicCertificateAuthority | None = None

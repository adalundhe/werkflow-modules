from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_active_certificate_authority import EKSActiveCertificateAuthority


class EKSCertificate(BaseModel):
    data: StrictStr | None = None
    active: EKSActiveCertificateAuthority | None = None

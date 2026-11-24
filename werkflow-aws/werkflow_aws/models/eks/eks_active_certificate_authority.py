from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_certificate_authority_activated_by import EKSCertificateAuthorityActivatedBy


class EKSActiveCertificateAuthority(BaseModel):
    id: StrictStr | None = None
    activatedBy: EKSCertificateAuthorityActivatedBy | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_active_certificate_authority_model import EKSActiveCertificateAuthorityModel


class EKSCertificateModel(BaseModel):
    data: StrictStr | None = None
    active: EKSActiveCertificateAuthorityModel | None = None

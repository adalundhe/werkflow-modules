from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSActiveCertificateAuthorityModel(BaseModel):
    id: StrictStr | None = None
    activatedBy: StrictStr | None = None

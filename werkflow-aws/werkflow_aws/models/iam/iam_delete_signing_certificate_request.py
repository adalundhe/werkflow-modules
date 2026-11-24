from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteSigningCertificateRequest(BaseModel):
    CertificateId: StrictStr
    UserName: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUploadSigningCertificateRequest(BaseModel):
    CertificateBody: StrictStr
    UserName: StrictStr | None = None

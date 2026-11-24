from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamCertificateBasedAuthProperties(BaseModel):
    Status: StrictStr | None = None
    CertificateAuthorityArn: StrictStr | None = None

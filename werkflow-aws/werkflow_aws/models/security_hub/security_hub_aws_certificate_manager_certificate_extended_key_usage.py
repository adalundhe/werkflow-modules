from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCertificateManagerCertificateExtendedKeyUsage(BaseModel):
    Name: StrictStr | None = None
    OId: StrictStr | None = None

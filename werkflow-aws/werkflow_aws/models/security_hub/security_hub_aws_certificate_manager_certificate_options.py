from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCertificateManagerCertificateOptions(BaseModel):
    CertificateTransparencyLoggingPreference: StrictStr | None = None

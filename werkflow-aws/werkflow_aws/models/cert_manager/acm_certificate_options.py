from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMCertificateOptions(BaseModel):
    CertificateTransparencyLoggingPreference: StrictStr | None = None
    Export: StrictStr | None = None
    ValidationMethod: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTIssuerCertificateIdentifier(BaseModel):
    issuerCertificateSubject: StrictStr | None = None
    issuerId: StrictStr | None = None
    issuerCertificateSerialNumber: StrictStr | None = None

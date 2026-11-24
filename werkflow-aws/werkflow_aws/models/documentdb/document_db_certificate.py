from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DocumentDBCertificate(BaseModel):
    CertificateIdentifier: StrictStr | None = None
    CertificateType: StrictStr | None = None
    Thumbprint: StrictStr | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidTill: datetime.datetime | StrictStr | None = None
    CertificateArn: StrictStr | None = None

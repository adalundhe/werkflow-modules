from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESIdentityCertificate(BaseModel):
    FromAddress: StrictStr | None = None
    Status: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    CertificateExpiryTime: datetime.datetime | StrictStr | None = None

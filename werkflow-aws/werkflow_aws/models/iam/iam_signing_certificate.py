from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMSigningCertificate(BaseModel):
    UserName: StrictStr | None = None
    CertificateId: StrictStr | None = None
    CertificateBody: StrictStr | None = None
    Status: StrictStr | None = None
    UploadDate: datetime.datetime | StrictStr | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceCertificateInfo(BaseModel):
    CertificateId: StrictStr | None = None
    CommonName: StrictStr | None = None
    State: StrictStr | None = None
    ExpiryDateTime: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None

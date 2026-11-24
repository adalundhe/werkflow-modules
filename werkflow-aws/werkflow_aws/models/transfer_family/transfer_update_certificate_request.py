from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TransferUpdateCertificateRequest(BaseModel):
    CertificateId: StrictStr
    ActiveDate: datetime.datetime | StrictStr | None = None
    InactiveDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None

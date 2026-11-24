from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TransferListedCertificate(BaseModel):
    Arn: StrictStr | None = None
    CertificateId: StrictStr | None = None
    Usage: StrictStr | None = None
    Status: StrictStr | None = None
    ActiveDate: datetime.datetime | StrictStr | None = None
    InactiveDate: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None

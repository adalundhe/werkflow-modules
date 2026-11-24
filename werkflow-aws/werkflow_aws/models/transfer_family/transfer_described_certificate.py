from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferDescribedCertificate(BaseModel):
    Arn: StrictStr | None = None
    CertificateId: StrictStr | None = None
    Usage: StrictStr | None = None
    Status: StrictStr | None = None
    Certificate: StrictStr | None = None
    CertificateChain: StrictStr | None = None
    ActiveDate: datetime.datetime | StrictStr | None = None
    InactiveDate: datetime.datetime | StrictStr | None = None
    Serial: StrictStr | None = None
    NotBeforeDate: datetime.datetime | StrictStr | None = None
    NotAfterDate: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[TransferTag] | None = None

from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferImportCertificateRequest(BaseModel):
    Usage: Literal['SIGNING', 'ENCRYPTION', 'TLS']
    Certificate: StrictStr
    CertificateChain: StrictStr | None = None
    PrivateKey: StrictStr | None = None
    ActiveDate: datetime.datetime | StrictStr | None = None
    InactiveDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[TransferTag] | None = None

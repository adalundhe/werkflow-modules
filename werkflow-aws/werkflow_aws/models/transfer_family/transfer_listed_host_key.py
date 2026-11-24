from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TransferListedHostKey(BaseModel):
    Arn: StrictStr | None = None
    HostKeyId: StrictStr | None = None
    Fingerprint: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    DateImported: datetime.datetime | StrictStr | None = None
    StorageType: StrictStr | None = None
    SecretId: StrictStr | None = None

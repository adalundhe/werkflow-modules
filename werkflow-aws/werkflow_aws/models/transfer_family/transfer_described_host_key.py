from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferDescribedHostKey(BaseModel):
    Arn: StrictStr | None = None
    HostKeyId: StrictStr | None = None
    HostKeyFingerprint: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    DateImported: datetime.datetime | StrictStr | None = None
    Tags: list[TransferTag] | None = None
    StorageType: StrictStr | None = None
    SecretId: StrictStr | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TransferSshPublicKey(BaseModel):
    DateImported: datetime.datetime | StrictStr | None = None
    SshPublicKeyBody: StrictStr | None = None
    SshPublicKeyId: StrictStr | None = None

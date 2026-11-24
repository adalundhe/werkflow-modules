from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TransferUpdateHostKeyRequest(BaseModel):
    ServerId: StrictStr
    HostKeyId: StrictStr
    Description: StrictStr | None = None
    StorageType: Literal['SERVICE_MANAGED', 'SECRETS_MANAGER'] | None = None
    KmsKey: StrictStr | None = None

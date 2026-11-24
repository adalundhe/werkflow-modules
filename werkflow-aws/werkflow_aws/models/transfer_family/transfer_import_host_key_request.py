from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferImportHostKeyRequest(BaseModel):
    ServerId: StrictStr
    HostKeyBody: StrictStr
    Description: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    StorageType: Literal['SERVICE_MANAGED', 'SECRETS_MANAGER'] | None = None
    KmsKey: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisChannelEncryptionConfiguration(BaseModel):
    EncryptionType: StrictStr | None = None
    KeyId: StrictStr | None = None

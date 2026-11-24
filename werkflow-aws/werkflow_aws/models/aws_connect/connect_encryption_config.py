from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEncryptionConfig(BaseModel):
    EncryptionType: StrictStr | None = None
    KeyId: StrictStr | None = None

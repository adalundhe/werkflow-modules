from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieServerSideEncryption(BaseModel):
    encryptionType: StrictStr | None = None
    kmsMasterKeyId: StrictStr | None = None

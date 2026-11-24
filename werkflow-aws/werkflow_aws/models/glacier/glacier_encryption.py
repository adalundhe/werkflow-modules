from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierEncryption(BaseModel):
    EncryptionType: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    KMSContext: StrictStr | None = None

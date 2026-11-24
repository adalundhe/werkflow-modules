from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueMLUserDataEncryption(BaseModel):
    MlUserDataEncryptionMode: StrictStr | None = None
    KmsKeyId: StrictStr | None = None

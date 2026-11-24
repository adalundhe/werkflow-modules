from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsKmsEncryptionSettings(BaseModel):
    key: StrictStr
    encryptionContext: dict[StrictStr, StrictStr] | None = None

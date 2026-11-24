from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsKmsEncryptionState(BaseModel):
    key: StrictStr | None = None
    encryptionContext: dict[StrictStr, StrictStr] | None = None

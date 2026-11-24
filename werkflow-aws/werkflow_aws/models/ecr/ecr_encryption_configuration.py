from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECREncryptionConfiguration(BaseModel):
    encryptionType: StrictStr | None = None
    kmsKey: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDataLakeEncryptionConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None

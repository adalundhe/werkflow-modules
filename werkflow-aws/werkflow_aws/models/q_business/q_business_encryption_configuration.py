from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessEncryptionConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None

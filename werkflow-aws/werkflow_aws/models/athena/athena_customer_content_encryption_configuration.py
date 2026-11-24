from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaCustomerContentEncryptionConfiguration(BaseModel):
    KmsKey: StrictStr | None = None

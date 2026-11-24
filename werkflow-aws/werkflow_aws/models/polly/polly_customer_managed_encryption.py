from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyCustomerManagedEncryption(BaseModel):
    KmsKeyArn: StrictStr | None = None
    EncryptionContext: dict[StrictStr, StrictStr] | None = None

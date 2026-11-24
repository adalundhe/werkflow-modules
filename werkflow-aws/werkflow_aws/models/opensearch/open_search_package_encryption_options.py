from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchPackageEncryptionOptions(BaseModel):
    KmsKeyIdentifier: StrictStr | None = None
    EncryptionEnabled: StrictBool | None = None

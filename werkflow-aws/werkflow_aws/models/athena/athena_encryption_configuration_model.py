from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaEncryptionConfigurationModel(BaseModel):
    EncryptionOption: StrictStr | None = None
    KmsKey: StrictStr | None = None

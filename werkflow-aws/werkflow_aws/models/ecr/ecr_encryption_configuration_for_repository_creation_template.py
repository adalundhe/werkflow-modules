from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECREncryptionConfigurationForRepositoryCreationTemplate(BaseModel):
    encryptionType: StrictStr | None = None
    kmsKey: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractEncryptionConfiguration(BaseModel):
    KmsKeyId: StrictStr | None = None
    KmsEncryptionContext: dict[StrictStr, StrictStr] | None = None

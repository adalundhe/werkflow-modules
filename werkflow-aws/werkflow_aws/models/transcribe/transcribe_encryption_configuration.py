from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeEncryptionConfiguration(BaseModel):
    KMSEncryptionContext: dict[StrictStr, StrictStr] | None = None
    KMSKey: StrictStr | None = None

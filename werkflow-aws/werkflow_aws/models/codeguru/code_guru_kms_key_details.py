from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruKMSKeyDetails(BaseModel):
    KMSKeyId: StrictStr | None = None
    EncryptionOption: StrictStr | None = None

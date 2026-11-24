from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchEncryptionAtRestOptions(BaseModel):
    Enabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    EncryptionMode: StrictStr | None = None

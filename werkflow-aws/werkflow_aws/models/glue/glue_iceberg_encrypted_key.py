from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIcebergEncryptedKey(BaseModel):
    KeyId: StrictStr
    EncryptedKeyMetadata: StrictStr
    EncryptedById: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None

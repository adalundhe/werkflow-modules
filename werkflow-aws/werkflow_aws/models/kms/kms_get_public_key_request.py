from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSGetPublicKeyRequest(BaseModel):
    KeyId: StrictStr
    GrantTokens: list[StrictStr] | None = None

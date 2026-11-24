from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSEnableKeyRequest(BaseModel):
    KeyId: StrictStr

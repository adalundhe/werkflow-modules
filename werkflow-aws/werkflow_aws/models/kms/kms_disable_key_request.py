from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSDisableKeyRequest(BaseModel):
    KeyId: StrictStr

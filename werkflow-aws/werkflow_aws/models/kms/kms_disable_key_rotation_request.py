from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSDisableKeyRotationRequest(BaseModel):
    KeyId: StrictStr

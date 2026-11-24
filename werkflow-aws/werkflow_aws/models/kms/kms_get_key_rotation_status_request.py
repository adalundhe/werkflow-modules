from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSGetKeyRotationStatusRequest(BaseModel):
    KeyId: StrictStr

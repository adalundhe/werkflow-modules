from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSEnableKeyRotationRequest(BaseModel):
    KeyId: StrictStr
    RotationPeriodInDays: StrictInt | None = None

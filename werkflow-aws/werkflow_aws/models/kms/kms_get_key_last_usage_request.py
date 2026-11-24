from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSGetKeyLastUsageRequest(BaseModel):
    KeyId: StrictStr

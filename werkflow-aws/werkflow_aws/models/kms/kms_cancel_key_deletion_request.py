from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSCancelKeyDeletionRequest(BaseModel):
    KeyId: StrictStr

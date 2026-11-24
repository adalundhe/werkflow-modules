from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSUpdateKeyDescriptionRequest(BaseModel):
    KeyId: StrictStr
    Description: StrictStr

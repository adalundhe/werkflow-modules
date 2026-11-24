from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetCustomDataIdentifierRequest(BaseModel):
    id: StrictStr

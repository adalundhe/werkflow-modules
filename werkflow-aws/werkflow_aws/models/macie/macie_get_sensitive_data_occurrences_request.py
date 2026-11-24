from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetSensitiveDataOccurrencesRequest(BaseModel):
    findingId: StrictStr

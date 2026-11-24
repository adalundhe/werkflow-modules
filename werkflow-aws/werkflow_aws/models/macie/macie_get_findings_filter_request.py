from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetFindingsFilterRequest(BaseModel):
    id: StrictStr

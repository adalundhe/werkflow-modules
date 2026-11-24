from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDeleteFindingsFilterRequest(BaseModel):
    id: StrictStr

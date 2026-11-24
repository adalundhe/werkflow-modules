from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetMemberRequest(BaseModel):
    id: StrictStr

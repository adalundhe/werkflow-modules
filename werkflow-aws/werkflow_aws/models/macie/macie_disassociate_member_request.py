from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDisassociateMemberRequest(BaseModel):
    id: StrictStr

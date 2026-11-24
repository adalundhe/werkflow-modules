from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamExpireSessionRequest(BaseModel):
    SessionId: StrictStr

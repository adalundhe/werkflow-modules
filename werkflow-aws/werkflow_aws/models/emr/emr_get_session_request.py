from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRGetSessionRequest(BaseModel):
    ClusterId: StrictStr
    SessionId: StrictStr

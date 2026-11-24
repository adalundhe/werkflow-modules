from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMResumeSessionRequest(BaseModel):
    SessionId: StrictStr

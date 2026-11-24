from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMTerminateSessionRequest(BaseModel):
    SessionId: StrictStr

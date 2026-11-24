from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRTerminateSessionRequest(BaseModel):
    ClusterId: StrictStr
    SessionId: StrictStr

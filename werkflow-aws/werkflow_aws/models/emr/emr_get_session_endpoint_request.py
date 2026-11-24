from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRGetSessionEndpointRequest(BaseModel):
    ClusterId: StrictStr
    SessionId: StrictStr

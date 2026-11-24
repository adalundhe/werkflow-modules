from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetSessionEndpointRequest(BaseModel):
    SessionId: StrictStr

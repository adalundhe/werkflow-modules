from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayCancelTraceRetrievalRequest(BaseModel):
    RetrievalToken: StrictStr

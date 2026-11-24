from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetJobRequest(BaseModel):
    JobId: StrictStr

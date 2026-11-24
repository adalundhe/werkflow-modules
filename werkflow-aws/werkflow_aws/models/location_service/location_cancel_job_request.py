from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationCancelJobRequest(BaseModel):
    JobId: StrictStr

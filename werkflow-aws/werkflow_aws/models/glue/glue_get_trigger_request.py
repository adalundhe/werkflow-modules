from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetTriggerRequest(BaseModel):
    Name: StrictStr

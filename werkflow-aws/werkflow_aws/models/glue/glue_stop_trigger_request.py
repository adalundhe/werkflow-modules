from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopTriggerRequest(BaseModel):
    Name: StrictStr

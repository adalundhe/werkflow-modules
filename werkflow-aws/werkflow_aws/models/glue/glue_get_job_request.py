from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetJobRequest(BaseModel):
    JobName: StrictStr

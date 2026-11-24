from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteJobRequest(BaseModel):
    JobName: StrictStr

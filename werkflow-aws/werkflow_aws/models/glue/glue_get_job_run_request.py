from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetJobRunRequest(BaseModel):
    JobName: StrictStr
    RunId: StrictStr
    PredecessorsIncluded: StrictBool | None = None

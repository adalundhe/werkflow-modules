from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetSystemLogsForJobRunRequest(BaseModel):
    JobName: StrictStr
    RunId: StrictStr

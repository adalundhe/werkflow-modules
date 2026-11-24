from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetMLTaskRunRequest(BaseModel):
    TransformId: StrictStr
    TaskRunId: StrictStr

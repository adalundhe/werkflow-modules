from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCancelMLTaskRunRequest(BaseModel):
    TransformId: StrictStr
    TaskRunId: StrictStr

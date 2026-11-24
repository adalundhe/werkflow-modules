from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchStopJobRunRequest(BaseModel):
    JobName: StrictStr
    JobRunIds: list[StrictStr]

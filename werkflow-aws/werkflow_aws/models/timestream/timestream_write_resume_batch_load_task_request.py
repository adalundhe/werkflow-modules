from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteResumeBatchLoadTaskRequest(BaseModel):
    TaskId: StrictStr

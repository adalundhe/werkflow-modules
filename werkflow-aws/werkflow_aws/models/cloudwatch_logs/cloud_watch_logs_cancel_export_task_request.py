from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCancelExportTaskRequest(BaseModel):
    taskId: StrictStr

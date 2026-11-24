from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCancelImportTaskRequest(BaseModel):
    importId: StrictStr

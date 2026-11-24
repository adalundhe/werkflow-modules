from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncCancelTaskExecutionRequest(BaseModel):
    TaskExecutionArn: StrictStr

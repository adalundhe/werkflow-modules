from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_options import DataSyncOptions


class DataSyncUpdateTaskExecutionRequest(BaseModel):
    TaskExecutionArn: StrictStr
    Options: DataSyncOptions

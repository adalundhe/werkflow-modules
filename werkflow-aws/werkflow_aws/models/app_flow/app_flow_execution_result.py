from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .app_flow_error_info import AppFlowErrorInfo


class AppFlowExecutionResult(BaseModel):
    errorInfo: AppFlowErrorInfo | None = None
    bytesProcessed: StrictInt | None = None
    bytesWritten: StrictInt | None = None
    recordsProcessed: StrictInt | None = None
    numParallelProcesses: StrictInt | None = None
    maxPageSize: StrictInt | None = None

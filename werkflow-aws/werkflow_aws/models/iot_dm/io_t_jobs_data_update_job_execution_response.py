from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_jobs_data_job_execution_state import IoTJobsDataJobExecutionState


class IoTJobsDataUpdateJobExecutionResponse(BaseModel):
    executionState: IoTJobsDataJobExecutionState | None = None
    jobDocument: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

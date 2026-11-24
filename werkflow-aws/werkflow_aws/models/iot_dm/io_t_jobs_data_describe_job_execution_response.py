from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_jobs_data_job_execution import IoTJobsDataJobExecution


class IoTJobsDataDescribeJobExecutionResponse(BaseModel):
    execution: IoTJobsDataJobExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None

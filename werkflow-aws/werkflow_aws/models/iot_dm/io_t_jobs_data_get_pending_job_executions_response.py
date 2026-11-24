from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_jobs_data_job_execution_summary import IoTJobsDataJobExecutionSummary


class IoTJobsDataGetPendingJobExecutionsResponse(BaseModel):
    inProgressJobs: list[IoTJobsDataJobExecutionSummary] | None = None
    queuedJobs: list[IoTJobsDataJobExecutionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

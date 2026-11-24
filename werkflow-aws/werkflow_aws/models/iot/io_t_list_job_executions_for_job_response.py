from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_job_execution_summary_for_job import IoTJobExecutionSummaryForJob


class IoTListJobExecutionsForJobResponse(BaseModel):
    executionSummaries: list[IoTJobExecutionSummaryForJob] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

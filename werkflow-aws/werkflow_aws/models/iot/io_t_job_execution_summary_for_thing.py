from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_job_execution_summary import IoTJobExecutionSummary


class IoTJobExecutionSummaryForThing(BaseModel):
    jobId: StrictStr | None = None
    jobExecutionSummary: IoTJobExecutionSummary | None = None

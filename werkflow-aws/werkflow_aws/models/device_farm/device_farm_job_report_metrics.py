from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DeviceFarmJobReportMetrics(BaseModel):
    jobsTotal: StrictInt | None = None
    jobsPassed: StrictInt | None = None
    jobsFailed: StrictInt | None = None
    jobsSkipped: StrictInt | None = None
    jobsErrored: StrictInt | None = None
    jobsStopped: StrictInt | None = None
    jobsPassedPercentage: StrictFloat | StrictInt | None = None
    totalJobExecutionDurationSeconds: StrictFloat | StrictInt | None = None
    averageJobExecutionDurationSeconds: StrictFloat | StrictInt | None = None
    medianJobExecutionDurationSeconds: StrictFloat | StrictInt | None = None

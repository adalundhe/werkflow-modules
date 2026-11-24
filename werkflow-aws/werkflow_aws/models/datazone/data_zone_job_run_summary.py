from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_job_run_error import DataZoneJobRunError


class DataZoneJobRunSummary(BaseModel):
    domainId: StrictStr | None = None
    jobId: StrictStr | None = None
    jobType: StrictStr | None = None
    runId: StrictStr | None = None
    runMode: StrictStr | None = None
    status: StrictStr | None = None
    error: DataZoneJobRunError | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None

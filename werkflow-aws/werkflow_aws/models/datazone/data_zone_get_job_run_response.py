from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_job_run_details import DataZoneJobRunDetails
from .data_zone_job_run_error import DataZoneJobRunError


class DataZoneGetJobRunResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    jobId: StrictStr | None = None
    jobType: StrictStr | None = None
    runMode: StrictStr | None = None
    details: DataZoneJobRunDetails | None = None
    status: StrictStr | None = None
    error: DataZoneJobRunError | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

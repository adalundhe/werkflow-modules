from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_report_job import BackupReportJob


class BackupListReportJobsResponse(BaseModel):
    ReportJobs: list[BackupReportJob] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

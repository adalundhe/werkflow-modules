from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_report_job import BackupReportJob


class BackupDescribeReportJobResponse(BaseModel):
    ReportJob: BackupReportJob | None = None
    ResponseMetadata: dict[str, Any] | None = None

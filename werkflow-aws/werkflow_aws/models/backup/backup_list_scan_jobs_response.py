from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_scan_job import BackupScanJob


class BackupListScanJobsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ScanJobs: list[BackupScanJob] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_scan_job_summary import BackupScanJobSummary


class BackupListScanJobSummariesResponse(BaseModel):
    ScanJobSummaries: list[BackupScanJobSummary] | None = None
    AggregationPeriod: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

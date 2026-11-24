from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_job_summary import BackupJobSummary


class BackupListBackupJobSummariesResponse(BaseModel):
    BackupJobSummaries: list[BackupJobSummary] | None = None
    AggregationPeriod: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

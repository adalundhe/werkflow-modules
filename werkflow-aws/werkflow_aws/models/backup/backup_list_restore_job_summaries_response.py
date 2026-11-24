from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_restore_job_summary import BackupRestoreJobSummary


class BackupListRestoreJobSummariesResponse(BaseModel):
    RestoreJobSummaries: list[BackupRestoreJobSummary] | None = None
    AggregationPeriod: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

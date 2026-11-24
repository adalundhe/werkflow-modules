from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_copy_job_summary import BackupCopyJobSummary


class BackupListCopyJobSummariesResponse(BaseModel):
    CopyJobSummaries: list[BackupCopyJobSummary] | None = None
    AggregationPeriod: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

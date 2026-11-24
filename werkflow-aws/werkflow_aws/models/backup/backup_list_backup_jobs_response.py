from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_job import BackupJob


class BackupListBackupJobsResponse(BaseModel):
    BackupJobs: list[BackupJob] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

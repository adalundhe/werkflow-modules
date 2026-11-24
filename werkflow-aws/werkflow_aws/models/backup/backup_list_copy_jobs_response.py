from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_copy_job import BackupCopyJob


class BackupListCopyJobsResponse(BaseModel):
    CopyJobs: list[BackupCopyJob] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

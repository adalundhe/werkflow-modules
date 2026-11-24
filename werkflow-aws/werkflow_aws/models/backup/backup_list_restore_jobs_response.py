from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_restore_jobs_list_member import BackupRestoreJobsListMember


class BackupListRestoreJobsResponse(BaseModel):
    RestoreJobs: list[BackupRestoreJobsListMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

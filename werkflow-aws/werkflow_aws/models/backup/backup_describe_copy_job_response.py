from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_copy_job import BackupCopyJob


class BackupDescribeCopyJobResponse(BaseModel):
    CopyJob: BackupCopyJob | None = None
    ResponseMetadata: dict[str, Any] | None = None

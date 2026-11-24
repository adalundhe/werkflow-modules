from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_backup import FSxBackup


class FSxCreateBackupResponse(BaseModel):
    Backup: FSxBackup | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_plan import BackupPlan as _BackupPlanType


class BackupGetBackupPlanFromJSONResponse(BaseModel):
    BackupPlan: _BackupPlanType | None = None
    ResponseMetadata: dict[str, Any] | None = None

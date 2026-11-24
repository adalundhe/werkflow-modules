from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_plan import BackupPlan


class BackupGetBackupPlanFromTemplateResponse(BaseModel):
    BackupPlanDocument: BackupPlan | None = None
    ResponseMetadata: dict[str, Any] | None = None

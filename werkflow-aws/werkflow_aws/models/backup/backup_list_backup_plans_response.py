from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_plans_list_member import BackupPlansListMember


class BackupListBackupPlansResponse(BaseModel):
    NextToken: StrictStr | None = None
    BackupPlansList: list[BackupPlansListMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_plan_templates_list_member import BackupPlanTemplatesListMember


class BackupListBackupPlanTemplatesResponse(BaseModel):
    NextToken: StrictStr | None = None
    BackupPlanTemplatesList: list[BackupPlanTemplatesListMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None

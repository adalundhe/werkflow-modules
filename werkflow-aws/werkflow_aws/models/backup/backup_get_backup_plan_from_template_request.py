from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetBackupPlanFromTemplateRequest(BaseModel):
    BackupPlanTemplateId: StrictStr

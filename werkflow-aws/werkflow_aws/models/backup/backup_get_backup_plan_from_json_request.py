from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetBackupPlanFromJSONRequest(BaseModel):
    BackupPlanTemplateJson: StrictStr

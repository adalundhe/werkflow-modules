from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupScanJobCreator(BaseModel):
    BackupPlanArn: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    BackupPlanVersion: StrictStr | None = None
    BackupRuleId: StrictStr | None = None

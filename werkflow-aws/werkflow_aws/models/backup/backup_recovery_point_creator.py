from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupRecoveryPointCreator(BaseModel):
    BackupPlanId: StrictStr | None = None
    BackupPlanArn: StrictStr | None = None
    BackupPlanName: StrictStr | None = None
    BackupPlanVersion: StrictStr | None = None
    BackupRuleId: StrictStr | None = None
    BackupRuleName: StrictStr | None = None
    BackupRuleCron: StrictStr | None = None
    BackupRuleTimezone: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsBackupRecoveryPointCreatedByDetails(BaseModel):
    BackupPlanArn: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    BackupPlanVersion: StrictStr | None = None
    BackupRuleId: StrictStr | None = None

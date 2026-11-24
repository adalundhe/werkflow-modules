from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_backup_backup_plan_backup_plan_details import SecurityHubAwsBackupBackupPlanBackupPlanDetails


class SecurityHubAwsBackupBackupPlanDetails(BaseModel):
    BackupPlan: SecurityHubAwsBackupBackupPlanBackupPlanDetails | None = None
    BackupPlanArn: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    VersionId: StrictStr | None = None

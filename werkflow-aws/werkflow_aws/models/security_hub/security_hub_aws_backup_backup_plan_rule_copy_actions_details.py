from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_backup_backup_plan_lifecycle_details import SecurityHubAwsBackupBackupPlanLifecycleDetails


class SecurityHubAwsBackupBackupPlanRuleCopyActionsDetails(BaseModel):
    DestinationBackupVaultArn: StrictStr | None = None
    Lifecycle: SecurityHubAwsBackupBackupPlanLifecycleDetails | None = None

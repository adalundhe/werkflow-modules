from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_backup_backup_plan_advanced_backup_settings_details import SecurityHubAwsBackupBackupPlanAdvancedBackupSettingsDetails
from .security_hub_aws_backup_backup_plan_rule_details import SecurityHubAwsBackupBackupPlanRuleDetails


class SecurityHubAwsBackupBackupPlanBackupPlanDetails(BaseModel):
    BackupPlanName: StrictStr | None = None
    AdvancedBackupSettings: list[SecurityHubAwsBackupBackupPlanAdvancedBackupSettingsDetails] | None = None
    BackupPlanRule: list[SecurityHubAwsBackupBackupPlanRuleDetails] | None = None

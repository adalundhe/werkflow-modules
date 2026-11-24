from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_backup_backup_plan_lifecycle_details import SecurityHubAwsBackupBackupPlanLifecycleDetails
from .security_hub_aws_backup_backup_plan_rule_copy_actions_details import SecurityHubAwsBackupBackupPlanRuleCopyActionsDetails


class SecurityHubAwsBackupBackupPlanRuleDetails(BaseModel):
    TargetBackupVault: StrictStr | None = None
    StartWindowMinutes: StrictInt | None = None
    ScheduleExpression: StrictStr | None = None
    RuleName: StrictStr | None = None
    RuleId: StrictStr | None = None
    EnableContinuousBackup: StrictBool | None = None
    CompletionWindowMinutes: StrictInt | None = None
    CopyActions: list[SecurityHubAwsBackupBackupPlanRuleCopyActionsDetails] | None = None
    Lifecycle: SecurityHubAwsBackupBackupPlanLifecycleDetails | None = None

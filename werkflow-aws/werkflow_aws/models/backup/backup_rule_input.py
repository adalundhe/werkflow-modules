from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_copy_action import BackupCopyAction
from .backup_index_action import BackupIndexAction
from .backup_lifecycle import BackupLifecycle
from .backup_scan_action import BackupScanAction


class BackupRuleInput(BaseModel):
    RuleName: StrictStr
    TargetBackupVaultName: StrictStr
    TargetLogicallyAirGappedBackupVaultArn: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    StartWindowMinutes: StrictInt | None = None
    CompletionWindowMinutes: StrictInt | None = None
    Lifecycle: BackupLifecycle | None = None
    RecoveryPointTags: dict[StrictStr, StrictStr] | None = None
    CopyActions: list[BackupCopyAction] | None = None
    EnableContinuousBackup: StrictBool | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    IndexActions: list[BackupIndexAction] | None = None
    ScanActions: list[BackupScanAction] | None = None

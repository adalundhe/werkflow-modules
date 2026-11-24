from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_advanced_backup_setting import BackupAdvancedBackupSetting
from .backup_rule_input import BackupRuleInput
from .backup_scan_setting import BackupScanSetting


class BackupPlanInput(BaseModel):
    BackupPlanName: StrictStr
    Rules: list[BackupRuleInput]
    AdvancedBackupSettings: list[BackupAdvancedBackupSetting] | None = None
    ScanSettings: list[BackupScanSetting] | None = None

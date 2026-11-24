from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_advanced_backup_setting import BackupAdvancedBackupSetting
from .backup_rule import BackupRule
from .backup_scan_setting import BackupScanSetting


class BackupPlan(BaseModel):
    BackupPlanName: StrictStr | None = None
    Rules: list[BackupRule] | None = None
    AdvancedBackupSettings: list[BackupAdvancedBackupSetting] | None = None
    ScanSettings: list[BackupScanSetting] | None = None

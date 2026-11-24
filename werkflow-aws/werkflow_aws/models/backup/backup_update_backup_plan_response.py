from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_advanced_backup_setting import BackupAdvancedBackupSetting
from .backup_scan_setting import BackupScanSetting


class BackupUpdateBackupPlanResponse(BaseModel):
    BackupPlanId: StrictStr | None = None
    BackupPlanArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    VersionId: StrictStr | None = None
    AdvancedBackupSettings: list[BackupAdvancedBackupSetting] | None = None
    ScanSettings: list[BackupScanSetting] | None = None
    ResponseMetadata: dict[str, Any] | None = None

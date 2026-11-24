from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .backup_advanced_backup_setting import BackupAdvancedBackupSetting


class BackupPlansListMember(BaseModel):
    BackupPlanArn: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    DeletionDate: datetime.datetime | StrictStr | None = None
    VersionId: StrictStr | None = None
    BackupPlanName: StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    AdvancedBackupSettings: list[BackupAdvancedBackupSetting] | None = None

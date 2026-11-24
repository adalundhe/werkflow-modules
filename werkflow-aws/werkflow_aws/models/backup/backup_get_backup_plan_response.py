from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_advanced_backup_setting import BackupAdvancedBackupSetting
from .backup_plan import BackupPlan as _BackupPlanType
from .backup_scheduled_plan_execution_member import BackupScheduledPlanExecutionMember


class BackupGetBackupPlanResponse(BaseModel):
    BackupPlan: _BackupPlanType | None = None
    BackupPlanId: StrictStr | None = None
    BackupPlanArn: StrictStr | None = None
    VersionId: StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    DeletionDate: datetime.datetime | StrictStr | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    AdvancedBackupSettings: list[BackupAdvancedBackupSetting] | None = None
    ScheduledRunsPreview: list[BackupScheduledPlanExecutionMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None

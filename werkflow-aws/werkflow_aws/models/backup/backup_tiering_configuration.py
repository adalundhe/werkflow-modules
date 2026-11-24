from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .backup_resource_selection import BackupResourceSelection


class BackupTieringConfiguration(BaseModel):
    TieringConfigurationName: StrictStr | None = None
    TieringConfigurationArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    ResourceSelection: list[BackupResourceSelection] | None = None
    CreatorRequestId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None

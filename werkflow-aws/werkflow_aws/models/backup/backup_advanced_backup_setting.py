from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupAdvancedBackupSetting(BaseModel):
    ResourceType: StrictStr | None = None
    BackupOptions: dict[StrictStr, StrictStr] | None = None

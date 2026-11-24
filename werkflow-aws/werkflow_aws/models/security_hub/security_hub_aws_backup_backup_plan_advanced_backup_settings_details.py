from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsBackupBackupPlanAdvancedBackupSettingsDetails(BaseModel):
    BackupOptions: dict[StrictStr, StrictStr] | None = None
    ResourceType: StrictStr | None = None

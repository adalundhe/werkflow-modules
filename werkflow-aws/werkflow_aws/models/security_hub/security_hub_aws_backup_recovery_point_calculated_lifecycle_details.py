from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsBackupRecoveryPointCalculatedLifecycleDetails(BaseModel):
    DeleteAt: StrictStr | None = None
    MoveToColdStorageAt: StrictStr | None = None
